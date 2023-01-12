# Release Notes for ueberzug

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
