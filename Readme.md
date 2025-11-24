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
astAPI Secure User + Calculation Model (Module 10 & Module 11)

This repository contains the implementation for:

Module 10: Secure User Management

Module 11: Calculation Model, Pydantic Validation, Factory Pattern, Unit Tests, Integration Tests, and CI/CD with Docker Hub.

All code is structured using FastAPI, SQLAlchemy, Pydantic, and fully containerized with GitHub Actions CI/CD.

🚀 Module 11 – What Was Added
1. SQLAlchemy Calculation Model

Located in: app/models.py

Fields:

id

user_id (optional FK)

a (float)

b (float)

type (enum: ADD, SUBTRACT, MULTIPLY, DIVIDE)

result (optional)

created_at

2. Pydantic Schemas

Located in: app/schemas.py

Schemas created:

CalculationBase

CalculationCreate

CalculationRead

Includes full validation:

No division by zero

Valid calculation types only

Typed inputs for a, b, and type

3. Calculation Factory Pattern

Located in: app/services/calculation_factory.py

Implements:

Add operation

Subtract operation

Multiply operation

Divide operation

Error handling for invalid operations

Factory pattern makes it easy to extend operations later.

4. Testing (Unit + Integration)

Located in: tests/

Added:

test_calculation_unit.py

test_calculation_integration.py

Also includes:

Schema tests

Security tests

User integration tests

All tests pass (12 passed):

pytest -v

5. CI/CD Pipeline

In GitHub Actions:

Runs unit + integration tests

Builds Docker image using Dockerfile

Pushes image automatically to Docker Hub

Ensures no image is pushed if tests fail

Screenshot provided in /docs/Screenshots.

6. Docker Deployment

Image is automatically pushed to Docker Hub.

Docker Hub Repository:
https://hub.docker.com/repository/docker/nishitanadimpalli/module10-fastapi-secure-user

Latest image shows:
“Pushed: a few minutes ago” ✔️

🛠 How to Run Locally
1. Clone the repository
git clone https://github.com/nishitanadimpalli/module10-fastapi-secure-user
cd module10-fastapi-secure-user

2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run FastAPI
uvicorn app.main:app --reload


Open the API docs:
👉 http://127.0.0.1:8000/docs

🧪 How to Run Tests
pytest -v


All tests must pass before Docker builds and pushes.

🐳 Docker Instructions
Pull the image:
docker pull nishitanadimpalli/module10-fastapi-secure-user:latest

Run the container:
docker run -p 8000:8000 nishitanadimpalli/module10-fastapi-secure-user

📁 Project Structure (Important)
app/
 ├── models.py
 ├── schemas.py
 ├── database.py
 ├── main.py
 ├── security.py
 ├── crud_users.py
 └── services/
       └── calculation_factory.py
tests/
docs/
Dockerfile
requirements.txt

📝 Module 11 Reflection

Reflection is included inside:

docs/reflection_module11.md

📤 Submission Requirements Checklist
✔ GitHub Repo Link

https://github.com/nishitanadimpalli/module10-fastapi-secure-user

✔ GitHub Actions Screenshot

Located in docs/Screenshots/

✔ Docker Hub Screenshot

Located in docs/Screenshots/

✔ Reflection Document

docs/reflection_module11.md

✔ All Tests Passing

pytest -v → 12 passed