#!/bin/bash
set -e
pushd "$(dirname "$0")"
export PATH=$PATH:.venv/bin
git pull
python -m pip install -r requirements.txt
# python manage.py collectstatic --noinput
# python manage.py migrate
sudo kill -hup `cat gunicorn.pid`
echo `date "+%Y-%m-%d %H:%M:%S.%3N"` ' Updated' >> djsandbox_update.log
popd
