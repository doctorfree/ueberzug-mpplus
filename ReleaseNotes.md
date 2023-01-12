# Release Notes for ueberzug

Überzug is a command line utility which enables drawing of images in character terminal windows by using child windows. The original project at https://github.com/seebye/ueberzug was closed by the author and this is a continuation of that project designed to serve as one of the ways [MusicPlayerPlus](https://github.com/doctorfree/MusicPlayerPlus) can display album cover art.

The method of drawing images employed here will not work in Wayland and other protocols have been developed that make this method somewhat obsolete. However, it is still used by some projects so its continued availability is provided here.

This Python module gets installed automatically as part of the MusicPlayerPlus initialization process. If this module is needed outside of MusicPlayerPlus then it can be installed following the instructions below.

## Installation

Download the [latest ueberzug wheel](https://github.com/doctorfree/ueberzug-mpplus/releases) for your platform.

Install the ueberzug wheel by executing the command:

```bash
python3 -m pip install /path/to/ueberzug-<version>-<platform>.whl
```

## Removal

Removal of the package can be accomplished by issuing the command:

```bash
python3 -m pip uninstall ueberzug
```

## Building ueberzug from source

ueberzug can be compiled, packaged, and installed from the source code repository. This should be done as a normal user with `sudo` privileges:

```
# Retrieve the source code from the repository
git clone https://github.com/doctorfree/ueberzug-mpplus.git
# Enter the mppcava source directory
cd ueberzug-mpplus
# Compile ueberzug and create an installation wheel
./mkwheel
# Install ueberzug and its dependencies
python3 -m pip install dist/ueberzug*.whl
```
