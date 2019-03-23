FROM node:11-stretch

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

RUN apt-get update && \
    apt-get install -qy less vim-nox git tmux net-tools && \
    rm -rf /var/lib/apt/lists/* && apt-get autoremove -y && apt-get clean

WORKDIR /loyaltytoken

EXPOSE 8000

CMD tmux new-session -d -c '/loyaltytoken' 'bash' && \
    while true; do sleep 3600; done
