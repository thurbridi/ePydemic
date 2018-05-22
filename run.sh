#!/bin/bash

function usage {
    echo "usage: $./run.sh [epydemic|epydemic-compare]"
    echo "  epydemic                executes with GUI"
    echo "  epydemic-compare        uses fixed parameters and compares the result with (MELOTTI, 2009)"
    exit 1
}

if [  $# -eq 0 ]
then
    usage
    exit 1
fi

if [[ ! -e .venv ]]
then
    python3 -m venv .venv
    .venv/bin/pip install .
fi

COMMAND="$1"
shift

.venv/bin/"${COMMAND}" "$@"