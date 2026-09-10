# MLOps Continuous Delivery Activity 1

A lightweight Flask inference API demonstrating Continuous Delivery (CD) principles, container packaging with Docker, and automated delivery pipelines using GitHub Actions and GitHub Container Registry (GHCR).

## Project Structure

```
mlops-cd-activity1/
+-- .github/
¦   +-- workflows/
¦       +-- cd.yml
+-- .gitignore
+-- app.py
+-- compose.yaml
+-- Dockerfile
+-- pytest.ini
+-- requirements.txt
+-- VERSION
+-- tests/
    +-- conftest.py
    +-- test_app.py
```

## API Endpoints

- `GET /`: Service status
- `GET /health`: Returns application version, model version, and health status
- `POST /predict`: Accepts a JSON payload `{"value": <number>}` and returns prediction

## Local Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .\.venv\Scripts\Activate.ps1
   # Linux/macOS:
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Run tests:
   ```bash
   pytest
   ```

## Docker

Build and run the container locally:

```bash
docker build -t mlops-cd-activity1:local .
docker run --rm -p 5000:5000 mlops-cd-activity1:local
```

Verify endpoint:
```bash
curl http://localhost:5000/health
```

## Continuous Delivery Pipeline

The CD pipeline (`.github/workflows/cd.yml`) triggers on semantic version tags (`v*.*.*`):

1. **Test**: Runs automated unit tests with `pytest`.
2. **Build**: Extracts the version from the Git tag, authenticates with GHCR, builds the image, and pushes both the specific version tag and `latest`.
3. **Deploy Staging**: Automatically deploys the container to the staging environment and runs an automated smoke test.
4. **Deploy Production**: Requires manual approval on the `production` environment before deploying the tested container image to production.
