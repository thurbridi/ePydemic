#!/usr/bin/bash

if [[ ! -e .venv ]]
then
    python3 -m venv .venv
    .venv/bin/pip install .
fi

COMMAND="$1"
shift

.venv/bin/"${COMMAND}" "$@"