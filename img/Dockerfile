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
    python3 -m venv .venv && \
    source .venv/bin/activate && \
    pip install --no-input slack_bolt && \
    apt-get update -qq && apt-get install cron -yqq && apt-get install apt-utils -yqq && \
    touch /var/log/cron.log && \
    ls -la && \
    chmod a+x sh/*.sh && \
    ls -la sh/

# Remove this later ---
#ENTRYPOINT ["/DevOps_Scripts/Chatbot/Pybot/sh/entrypoint.sh"]
# End ---
ENTRYPOINT ["/pybot/sh/entrypoint.sh"]