#!/bin/bash

# Define branch to pull
BRANCH='master'

# Check if the branch that is being monitored is ahead
IS_AHEAD=$(git fetch --dry-run 2>&1)
if [ -z "${IS_AHEAD}" ]
then
    # No updates. Do nothing here.
    exit 0
else
    echo "[INFO] Updates detected. Pulling new changes..."
    git pull origin "${BRANCH}"
fi