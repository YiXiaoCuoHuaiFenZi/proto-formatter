#!/usr/bin/env bash

source .venv/bin/activate

python3 setup.py sdist

pip install dist/proto-formatter-0.1.8.tar.gz

deactivate