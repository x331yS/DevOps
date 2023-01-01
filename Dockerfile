FROM node:12-alpine3.9

COPY src/ /app/src/

RUN npm install --production
RUN npm install express
RUN npm install mysql

EXPOSE 8080

WORKDIR /app

CMD ["node", "src/index.js"]
