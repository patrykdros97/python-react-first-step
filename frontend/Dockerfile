FROM node:19.5.0-alpine

WORKDIR /app

COPY package*.json /app

RUN npm config set strict-ssl false
RUN npm i --silent
RUN npm i -g react-scripts@5.0.1
RUN npm install axios

COPY . ./

CMD [ "npm", "start" ]