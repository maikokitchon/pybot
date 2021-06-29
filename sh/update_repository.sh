# !/bin/bash

# Define branch to pull
BRANCH='develop'

# Check if the branch that is being monitored is ahead
IS_AHEAD=$(git status -uno | grep 'Your branch is up to date with')
echo "${IS_AHEAD}"
if [ ! -z "${IS_AHEAD}" ]
then
    echo "[INFO] Updates detected. Pulling new changes..."
    git pull origin "${BRANCH}"
fi