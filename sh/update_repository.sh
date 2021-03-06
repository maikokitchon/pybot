#!/bin/bash

# Define work directory
SHDIR="${0%/*}"
WORKDIR=$(dirname "${SHDIR}")

# Define date var
NOW=$(date)

# Go to workdir
cd "${WORKDIR}"

# Define branch to pull
BRANCH='master'

# Check if the branch that is being monitored is ahead
IS_AHEAD=$(git fetch --dry-run 2>&1)
if [ -z "${IS_AHEAD}" ]
then
    # No updates. Do nothing here.
    exit 0
else
    echo "${NOW} [INFO] Updates detected. Pulling new changes..."
    git pull origin "${BRANCH}"
fi