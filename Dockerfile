FROM node:18

WORKDIR /app

COPY . /app

RUN npm install

COPY package*.json /app

RUN ["node", "test.js"]

CMD ["npm", "start"]