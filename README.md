# defl (Deflate [F]oto Library)

Command-line tool and API for searching duplicated files on user's storages.

## No error in the name of the util
"Foto" /ˈfōdō/ - is how "Photo" is pronounced anyways. Perhaps it's not a word
but the short name for the utility just looks nice this way.

# The Goal
The goal is to have a command-line utility and API to search through all user's
storages, and *intelligently* analyze them for duplicates.

# Current Functionality
The list of implemented Use Cases is available in the [Use Cases Catalog] (https://github.com/amamaenko/defl/wiki/Use-Cases-Catalog) page on project's
wiki.

# Future Plans
- Add support for online storages, such as Google Drive and DropBox.
- Add deep analyzis of image files, such as EXIFs, histograms, etc.
- Add deep learning for intelligent duplicates detection

# Installation and Usage

**NOTE** that the tool requires Python 3.5+.

There are two scenarios of installing the drive-downloader tool. For any of 
them it is highly recommended to use virtual environments. Watch, why, the 
excellent [Pycon 2016 talk](https://youtu.be/5BqAeN-F9Qs). Currently *defl* is 
a pure Python code, but it will definitely change in the future when I add the 
support for Google Drive, and similar services.

## Scenario 1: Use as a stand-alone tool or API

After setting up the environment use pip:

`pip install -e https://github.com/amamaenko/defl.git#egg=defl`

Then simply type:

`python -m defl -s "<dir1>" "<dir2>" ... "<dirn>"`

See `python -m defl -h` for more information about command line arguments.

## Scenario 2: Continue development of the tool

Clone the "https://github.com/amamaenko/defl.git" repository
using something like the command below:

`git clone https://github.com/amamaenko/defl.git defl`

then install a virtual environment there:

`virtualenv venv`

and, finally, install dependencies using

`pip install -r requirements_dev.txt`

# Licensing

**defl** is distrubuted under the BSD license. See the LICENSE file for details.

The code depends on unmodified **tqdm** package for visual representation. More 
info is available on the tqdm project's page: https://github.com/tqdm/tqdm