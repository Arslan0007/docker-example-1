FROM node:10-alpine

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY package*.json ./home/node/app

USER node

RUN npm install

COPY --chown=node:node . /home/node/app

EXPOSE 80

CMD [ "node", "app.js"]

