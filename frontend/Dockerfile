FROM node:20
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=optional && npm cache clean --force
COPY . .
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
