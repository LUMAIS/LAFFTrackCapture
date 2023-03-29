# LAFFTrackCapture

Authors: (c) Andrea Chavez Munoz <chavezmunoz.a@northeastern.edu>, Artem Lutov &lt;&#108;&#97;v&commat;lumais&#46;&#99;om&gt;  
Date: 2023-03  

This project is forked from https://gitlab.com/Chavezmunoz.a/anttracking/-/blob/main/Camera 

## Deployment
Clone this repository, change directory to its root, create a virtual environment and install project dependencies from `requirements.txt`.  
Those steps can be performed using `pipenv`:
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
