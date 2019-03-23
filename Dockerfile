FROM node:11-stretch

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

RUN apt-get update && \
    apt-get install -qy less vim-nox git tmux net-tools && \
    rm -rf /var/lib/apt/lists/* && apt-get autoremove -y && apt-get clean

WORKDIR /loyaltytoken

RUN yarn global add @vue/cli
RUN pwd && ls -l && yarn install

EXPOSE 8080
CMD tmux new-session -d -c '/loyaltytoken/ui' 'yarn serve' && \
    while true; do sleep 3600; done
