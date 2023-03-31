# LAFFTrackCapture

Authors: (c) Andrea Chavez Munoz <chavezmunoz.a@northeastern.edu>, Artem Lutov &lt;&#108;&#97;v&commat;lumais&#46;&#99;om&gt;  
Date: 2023-03  
License:  [Apache License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)  

This project is forked from https://gitlab.com/Chavezmunoz.a/anttracking/-/blob/main/Camera 

## Deployment
Clone this repository, change directory to its root, create a virtual environment and install project dependencies from `requirements.txt`.  
Those steps can be performed using `pipenv`, `pyenv`, `mambe`/`conda`, or a standard Python's `venv`:
```sh
REPO_ROOT$ pip install pipenv
REPO_ROOT$ pipenv --python 3.8
REPO_ROOT$ pipenv install -r requirements.txt
REPO_ROOT$ pipenv shell
```
Those commands result in the creation of a new virtual environment with Python 3.8 (you can specify any newer version),  
installation of the dependencies from `requirements.txt`,
and opening a shell in the prepared environment.

Then, the application can be started as `./run.sh`.

## Building a Single Executable File
The whole Python application with all modules and dependencies can be packed into a single executable file using PyInstaller or its alternatives. PyInstaller can be installed by executing `$ pip install -U pyinstaller`.  
Then, this app with all its dependencies can be packed into a single executable file located in `./dist/` by the following command:
```sh
$ pyinstaller -F -n ltcap ./run.py
```
See the [generation options in the PyInstaller docs](https://pyinstaller.org/en/stable/usage.html#what-to-generate).

## Settings Saving/Loading
Settings are saved/loaded only for the selected cameras considering the sequence of their plugging to the grabber.  
Thus, a Hikvision camera settings saved from the first port of the grabber will not be loaded for that camera plugged to another port, which is essential to guarantee the deterministic camera setup and avoid issues when occasionally plugging cameras in different order, which are physically installed at the same places.
