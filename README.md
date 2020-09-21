The test application for the Libertex group

# Overview
No CORS policies applied
No another URL restrictions applied

# Running
## Docker-compose
Build and run the system with command
```docker-compose up -d```

## Manual debugging
If you need very close debugging capabilities, run the application locally
1. Run the database Docker image with command
```docker-compose up -d database```
2. Edit the .env file and apply local environment source
```set -a && source .env && set +a```
3. Run the Django application with ./manage.py runserver
