#DevOps Flask Demo 
This project showcases a fully automated CI/CD pipeline using Jenkins, Docker, GitHub, and a Flask-based web application. It demonstrates how modern DevOps workflows enable continuous integration, automated testing, containerized deployments, and zero‑downtime delivery. The system rebuilds and deploys the application automatically whenever new changes are pushed to GitHub.

#1. Project Overview
The DevOps Flask Demo is a CRUD‑based web application built using Flask and SQLAlchemy. It includes a modern UI with HTML, CSS, and JavaScript to provide an interactive interface. The major focus of this project is DevOps, where we implement an end‑to‑end automated pipeline capable of building, testing, pushing, and deploying the application without any manual steps.
2. What This Project Demonstrates
Fully automated Jenkins CI/CD pipeline
GitHub Webhooks for auto‑triggered builds
Dockerized Flask application
CRUD API endpoints with SQLAlchemy database
Frontend (HTML/CSS/JS) integrated with REST API
Automatic Docker image creation and versioning
Deployment using Docker containers
Scalable and production‑ready folder structure

#3. Features Implemented
Home page UI with interactive design
RESTful API with GET, POST, PUT, DELETE operations
Database operations with SQLAlchemy
Real‑time response endpoints (/health, /version)
Front‑end + back‑end integration
Advanced Jenkinsfile with multiple stages such as tests, build, push, deployment
Automatic new version deployment on every commit

#4. Folder Structure

app/
  ├── static/
  │     ├── style.css
  │     └── script.js
  ├── templates/
  │     └── index.html
  ├── app.py
  ├── Dockerfile
  ├── requirements.txt
docker-compose.yml
Jenkinsfile
README.md

#5. CI/CD Pipeline Flow
1. Developer pushes code to GitHub.
2. GitHub Webhook notifies Jenkins.
3. Jenkins automatically pulls the latest code.
4. Jenkins installs dependencies and runs tests.
5. Jenkins builds a new Docker image from the application.
6. Jenkins tags and pushes the image to Docker Hub.
7. Jenkins deploys the latest container on the host.
8. Application becomes live instantly with zero downtime.

#6. Jenkins Pipeline Stages 
1.Checkout – Pulls latest code from GitHub.
2.Run Tests – Installs required packages and (optional) runs automated tests.
3.Build Docker Image – Creates a versioned Docker image using Dockerfile.
4.Push to Docker Hub – Uploads the image to your Docker registry.
5.Deploy – Stops previous container and runs the new version automatically.

#7. Deployment Workflow
The deployment process is completely automated. Each commit results in a new container being deployed. This ensures reliability, consistency, and rapid updates without any manual intervention.

#8. Technologies Used
Flask (Python Web Framework)
SQLAlchemy (Database ORM)
Docker (Containerization)
Jenkins (CI/CD Orchestration)
GitHub (Source Control + Webhooks)
HTML/CSS/JavaScript (Frontend)
