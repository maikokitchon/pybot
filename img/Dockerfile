FROM python:3

ARG GIT_USERNAME
ARG GIT_PASSWORD

SHELL ["/bin/bash", "-c"] 

RUN \
    cd / && \
    #git clone http://${GIT_USERNAME}:${GIT_PASSWORD}/gerrit/DevOps_Scripts && \
    #cd /DevOps_Scripts/Chatbot/Pybot && \
    # Remove this later ---
    git clone https://github.com/maikokitchon/pybot.git && \
    cd /pybot && \
    # End ---
    git config core.fileMode false && \
    python3 -m venv .venv && \
    source .venv/bin/activate && \
    pip install --no-input slack_bolt && \
    apt-get update -qq && apt-get install cron -yqq && apt-get install apt-utils -yqq && apt-get install nano -yqq && \
    touch /var/log/cron.log && \
    chmod a+x sh/*.sh

# Remove this later ---
#ENTRYPOINT ["/DevOps_Scripts/Chatbot/Pybot/sh/entrypoint.sh"]
# End ---
ENTRYPOINT ["/pybot/sh/entrypoint.sh"]