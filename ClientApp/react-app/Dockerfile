FROM node:20
WORKDIR /app
COPY ClientApp/react-app/package*.json ./
RUN npm install
COPY ClientApp/react-app/ .
RUN npm run build
ENV NODE_ENV production
CMD ["npm", "start"]