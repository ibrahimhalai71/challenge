# FastAPI and Nuxt.js Application
This is a simple application that consists of a FastAPI backend and a Nuxt.js frontend. The backend provides an API endpoint that accepts a string input and returns the string reversed. The frontend provides a user interface for users to input the string and display the reversed output obtained from the backend.

## Getting Started
To get started with the application, you'll need to have Docker installed on your machine.

- Clone the repository: git clone https://github.com/example/fastapi-nuxt-app.git
- Navigate to the project directory: cd fastapi-nuxt-app
- Build and start the Docker containers: docker-compose up --build
- Access the application in your web browser at http://localhost:3000
## Backend
The backend is implemented using Python and FastAPI. The main.py file defines a single API endpoint, /reverse, that accepts a string input and returns the string reversed. The endpoint is implemented using the reverse_string function defined in the same file. The requirements.txt file lists the Python dependencies required by the backend.

## Frontend
The frontend is implemented using Nuxt.js and Bootstrap. The pages/index.vue file defines the user interface for the application. It includes a form that allows users to input the string, and a section to display the reversed output obtained from the backend. The axios library is used to send requests to the backend API.

## Packaging
The application is packaged using Docker. The Dockerfile defines a Docker image for the backend that starts from an official Python 3.9 slim image, installs the Python dependencies listed in requirements.txt, and runs the FastAPI application using uvicorn. The docker-compose.yml file defines two services, backend and frontend, each built from their respective directories (. and ./frontend). The backend service exposes port 8000, which is where the FastAPI application will be listening, and the frontend service exposes port 3000, which is where the Nuxt.js application will be served.
