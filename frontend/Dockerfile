# Use an official Node.js runtime as a parent image
FROM node:14.18.1-alpine3.14

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the frontend code to the container
COPY . .

# Build the Nuxt.js application
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Start the Nuxt.js application
CMD ["npm", "start"]
