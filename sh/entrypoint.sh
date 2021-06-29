#!/bin/sh

# Define work directory
WORKDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Define scripts that will run in cron
(crontab -l 2>/dev/null; echo "* * * * * /bin/bash -C ${WORKDIR}/sh/update_repository.sh > /var/log/cron.log 2>&1")|crontab

# Execute Pybot
python3 ${WORKDIR}/run.py &

exec "$@"