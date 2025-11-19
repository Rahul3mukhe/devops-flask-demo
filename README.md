# DevOps Flask Demo

Simple Flask app for DevOps demo with Docker and Jenkins pipeline.

Run locally:
1. Build: `docker build -t devops-flask-demo:local ./app`
2. Run: `docker run -p 5000:5000 devops-flask-demo:local`
3. Visit: http://localhost:5000

Using docker-compose:
`docker-compose up --build`
