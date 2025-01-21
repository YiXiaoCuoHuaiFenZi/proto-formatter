#!/usr/bin/env bash

command -v pyenv >/dev/null 2>&1 || { echo "Installing pyenv" >&2; brew install pyenv; }

echo "-> Installing python from .python-version with pyenv <-"
pyenv install

eval "$(pyenv init -)"
pip install virtualenv

echo "-> Creating virtualenv..."
virtualenv --setuptools 57.4.0 --prompt="(${PWD##*/}) " -p python .venv

echo "-> Activating virtualenv..."
source .venv/bin/activate

echo "-> Installing development dependencies...!"
make install-dev
deactivate
echo "-> Dependencies install complete!"

echo "Done!"