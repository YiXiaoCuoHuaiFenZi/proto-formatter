#!/usr/bin/env bash

source .venv/bin/activate
# build dist files
#python3 -m build
python3 setup.py sdist

# use default twine config, upload package to pypi https://upload.pypi.org/legacy/
python3 -m twine upload --repository pypi dist/*
deactivate