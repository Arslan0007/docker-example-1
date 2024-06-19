FROM node:10-alpine

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY package*.json ./home/node/app

USER node

RUN npm install

COPY --chown=node:node . /home/node/app

EXPOSE 80

CMD [ "node", "app.js"]

# FROM nginx:alpine

# COPY . /usr/share/nginx/html

# FROM node:latest

# COPY package.json package.json
# COPY package-lock.json package-lock.json

# RUN npm install
# RUN npm i cors
# RUN npm install require


# RUN apt-get install -y git-core curl build-essential openssl libssl-dev \
#  && git clone https://github.com/nodejs/node.git \
#  && cd node \
#  && ./configure \
#  && make \
#  && sudo make install

