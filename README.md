# md-wiki

```
Running the backend
```
- cd wiki-backend-second/
- source bin/activate
- uvicorn main:app --reload
    - Note: wiki-backend-second/ is a virtual environment
    - Note: wiki-backend/ stopped working after running "docker-compose up" in root

```
Running the frontend
```
- cd wiki-frontend/
- npm run serve

```
Running the container
```
- Go to the root project directory
- docker-compose up
    - Note: frontend doesn't work (but still runnable) in the container for some reasons..