"""This module contains x11 utils"""
import functools

import ueberzug.tmux_util as tmux_util
import ueberzug.terminal as terminal
import ueberzug.process as process
import ueberzug.X as X


PREPARED_DISPLAYS = []
DISPLAY_SUPPLIES = 1


class Events:
    """Async iterator class for x11 events"""

    def __init__(self, loop, display: X.Display):
        self._loop = loop
        self._display = display

    @staticmethod
    async def wait_for_event(loop, display: X.Display):
        """Waits asynchronously for an x11 event and returns it"""
        return await loop.run_in_executor(None, display.wait_for_event)

    def __aiter__(self):
        return self

    async def __anext__(self):
        return await Events.wait_for_event(self._loop, self._display)


class TerminalWindowInfo(terminal.TerminalInfo):
    def __init__(self, window_id, fd_pty=None):
        super().__init__(fd_pty)
        self.window_id = window_id


@functools.lru_cache()
def get_parent_pids(pid):
    """Determines all parent pids of this process.
    The list is sorted from youngest parent to oldest parent.
    """
    pids = []
    next_pid = pid

    while next_pid > 1:
        pids.append(next_pid)
        next_pid = process.get_parent_pid(next_pid)

    return pids


def get_pid_window_id_map(display: X.Display):
    """Determines the pid of each mapped window.

    Returns:
        dict of {pid: window_id}
    """
    return {
        display.get_window_pid(window_id): window_id
        for window_id in display.get_child_window_ids()}


def sort_by_key_list(mapping: dict, key_list: list):
    """Sorts the items of the mapping
    by the index of the keys in the key list.

    Args:
        mapping (dict): the mapping to be sorted
        key_list (list): the list which specifies the order

    Returns:
        list: which contains the sorted items as tuples
    """
    key_map = {key: index for index, key in enumerate(key_list)}
    return sorted(
        mapping.items(),
        key=lambda item: key_map.get(item[0], float('inf')))


def key_intersection(mapping: dict, key_list: list):
    """Creates a new map which only contains the intersection
    of the keys.

    Args:
        mapping (dict): the mapping to be filtered
        key_list (list): the keys to be used as a whitelist

    Returns:
        dict: which only contains keys which are also in key_list
    """
    key_map = {key: index for index, key in enumerate(key_list)}
    return {key: value for key, value in mapping.items()
            if key in key_map}


def get_first_pty(pids: list):
    """Determines the pseudo terminal of
    the first process in the passed list which owns one.
    """
    for pid in pids:
        pty_slave_file = process.get_pty_slave(pid)
        if pty_slave_file:
            return pty_slave_file

    return None


def get_parent_window_infos(display: X.Display):
    """Determines the window id of each
    terminal which displays the program using
    this layer.

    Returns:
        list of TerminalWindowInfo
    """
    window_infos = []
    client_pids = {}

    if tmux_util.is_used():
        client_pids = tmux_util.get_client_pids()
    else:
        client_pids = {process.get_own_pid()}

    if client_pids:
        pid_window_id_map = get_pid_window_id_map(display)

        for pid in client_pids:
            ppids = get_parent_pids(pid)
            ppid_window_id_map = key_intersection(pid_window_id_map, ppids)
            try:
                window_pid, window_id = next(iter(sort_by_key_list(
                    ppid_window_id_map, ppids)))
                window_children_pids = ppids[:ppids.index(window_pid)][::-1]
                pty = get_first_pty(window_children_pids)
                window_infos.append(TerminalWindowInfo(window_id, pty))
            except StopIteration:
                # Window needs to be mapped,
                # otherwise it's not listed in _NET_CLIENT_LIST
                pass

    return window_infos
