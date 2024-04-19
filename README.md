# Overview
- The project demo use fast API framework

# Create Environment
- Window: py -3 -m venv venv
- MacOs: python3 -m venv venv

# Active & Deactive environment:
- Active: \venv\Scripts\active.bat
- Deactive: deactive

# Install fastapi library
- pip install -r requirements.txt

# Create Postgres DB:
- Go to docker folder, run command: sh postgres.sh
- `host`: localhost
- `DB`: postgres
- `User`: postgres
- `Password`: 123456

# Execute Fast API
- https://fastapi.tiangolo.com/tutorial/first-steps/
- uvicorn app.main:app --reload

# api
- POST  /posts
- GET   /posts/:id
        /posts
- PUT   /posts/:id
- DELETE /posts/:id

