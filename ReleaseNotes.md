# Release Notes for ueberzug

Überzug is a command line utility which enables drawing of images in character terminal windows by using child windows. The original project at https://github.com/seebye/ueberzug was closed by the author and this is a continuation of that project designed to serve as one of the ways [MusicPlayerPlus](https://github.com/doctorfree/MusicPlayerPlus) can display album cover art.

The method of drawing images employed here will not work in Wayland and other protocols for image dispslay in a character based terminal window have been developed. However, Überzug is still one of the most flexible and portable techniques.

This Python module gets installed automatically as part of the MusicPlayerPlus initialization process. If this module is needed outside of MusicPlayerPlus then it can be installed following the instructions below.

**[Note:]** This version of Überzug includes several improvements over the original and is necessary for the display of album cover art in tabbed terminals. If a previous version of Überzug is installed, it should be removed and replaced with this improved version.

## Installation

Download the [latest ueberzug wheel](https://github.com/doctorfree/ueberzug-mpplus/releases) for your platform.

Install the Überzug wheel by executing the command:

```bash
python3 -m pip install /path/to/ueberzug-<version>-<platform>.whl
```

## Removal

Removal of the package can be accomplished by issuing the command:

```bash
python3 -m pip uninstall ueberzug
```

## Building Überzug from source

Überzug can be compiled, packaged, and installed from the source code repository. This should be done as a normal user with `sudo` privileges:

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
