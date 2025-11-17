This project implements a secure FastAPI user service with:

SQLAlchemy models

Pydantic schemas

Password hashing (bcrypt)

Unique email + username validation

Docker containerization

Automated testing with pytest

CI/CD pipeline using GitHub Actions

Automatic Docker Hub deployment

This repository is part of the multi-module project that continues in later modules.
How to Run the App Locally
1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
2. Install dependencies
pip install -r requirements.txt
3. Start PostgreSQL (use Docker)

If you don't already have a running DB container:
docker run --name module10db \
  -e POSTGRES_USER=calcuser \
  -e POSTGRES_PASSWORD=calcpass \
  -e POSTGRES_DB=module10db \
  -p 5432:5432 -d postgres:16
4. Export your DATABASE_URL
export DATABASE_URL="postgresql+psycopg2://calcuser:calcpass@localhost:5432/module10db"
5. Run the API
uvicorn app.main:app --reload

Open browser:
http://127.0.0.1:8000/docs

How to Run Tests Locally
Make sure you set the test database URL:
export DATABASE_URL="postgresql+psycopg2://calcuser:calcpass@localhost:5432/module10db"
Run tests:
pytest -v
All tests should pass (unit + integration)

Docker Hub Repository

Your Docker image is automatically built and uploaded by GitHub Actions.

Docker Hub URL

https://hub.docker.com/repository/docker/nishitanadimpalli/module10-fastapi-secure-user/general

To pull your image:
docker pull nishitanadimpalli/module10-fastapi-secure-user:latest

To run your image:
docker run -p 8000:8000 \
  -e DATABASE_URL="postgresql+psycopg2://calcuser:calcpass@host.docker.internal:5432/module10db" \
  nishitanadimpalli/module10-fastapi-secure-user:latest

GitHub Actions CI/CD Pipeline

This repo includes a complete CI/CD pipeline that:

Runs tests
Builds Docker image
Logs in to Docker Hub
Pushes the image (latest tag)
Stops containers after job finishes

You can find the workflow under:
.github/workflows/ci.yml

Reflection

The docs/reflection.md file contains:

What I learned about FastAPI

Challenges in setting up SQLAlchemy + Pydantic

How Dockerization helped deployment

What I learned from GitHub Actions CI/CD automation

Issues faced and how I solved them