#!/bin/bash

# Define work directory
SHDIR="${0%/*}"
WORKDIR=$(dirname "${SHDIR}")

# Define scripts that will run in cron
(crontab -l 2>/dev/null; echo "* * * * * /bin/bash -C ${SHDIR}/update_repository.sh > /var/log/cron.log 2>&1")|crontab

# Execute Pybot
cd "${WORKDIR}"
python3 -m venv .venv
source .venv/bin/activate
python3 "${WORKDIR}"/run.py

exec "$@"