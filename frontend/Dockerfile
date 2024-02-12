# Choose node image -> node version 21 based on alpine linux image
FROM node:21-alpine as BUILD_IMAGE

# create a working directory
WORKDIR /app

# Copy our package.json to our working directory
COPY package*.json ./

# install packages
RUN npm install

# copy the rest of files over > Except node_modules which are ignored in .dockerignore
COPY . .

#  build project
RUN npm run build

# Video (referenced in github task) suggests to implement a multi-stage build. 
# reduces size and doesnt expose code
FROM node:21-alpine as PRODUCTION_IMAGE

WORKDIR /app

COPY --from=BUILD_IMAGE /app/dist/ /app/dist/

EXPOSE 8080

COPY package.json .

COPY vite.config.ts .

RUN npm install typescript

# im skeptical as to why we expose the port twice. I will look into it when i have time
EXPOSE 8080

CMD ["npm", "run", "preview"]