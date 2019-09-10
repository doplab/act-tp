FROM node:10

WORKDIR /serve/

COPY . .

RUN npm install

EXPOSE 3010

CMD ["node", "serve_images.js"]