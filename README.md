# Azure Serverless Web Application

A serverless Azure web application demonstrating CI/CD, REST APIs, secure cloud storage, and frontend-backend integration using free-tier services.

## Architecture
- **Frontend**: Azure Static Web Apps (HTML, CSS, JavaScript)
- **Backend**: Azure Functions (Python, HTTP-triggered)
- **Storage**: Azure Blob Storage (private container)
- **CI/CD**: GitHub Actions (auto-deploy on every push)

## Features
- Serverless architecture with zero idle cost
- REST APIs for application status and runtime metrics
- Secure backend access to private Blob Storage
- Environment-based secret management
- Automated build and deployment pipeline

## API Endpoints
- `/api/status` — Returns application status data stored in Blob Storage
- `/api/metrics` — Returns runtime telemetry and versioned build metadata

## Security
- Private storage containers
- No credentials committed to source control
- Secrets managed via Azure environment variables
- Resource group isolation

## Technologies
Azure Static Web Apps, Azure Functions, Azure Blob Storage, GitHub Actions, Python, JavaScript
