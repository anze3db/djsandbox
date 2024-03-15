#!/bin/bash
pushd "$(dirname "$0")"
. .venv/bin/activate
gunicorn djsandbox.wsgi
popd
