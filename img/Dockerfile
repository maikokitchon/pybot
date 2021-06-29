FROM python:3

ARG GIT_USERNAME
ARG GIT_PASSWORD

RUN \
    cd / && \
    git clone http://${GIT_USERNAME}:${GIT_PASSWORD}/gerrit/DevOps_Scripts && \
    cd /DevOps_Scripts/Chatbot/Pybot && \
    python3 -m venv .venv && \
    source .venv/bin/activate && \
    pip install --no-input slack_bolt && \
    apt-get update -qq && apt-get install cron -yqq