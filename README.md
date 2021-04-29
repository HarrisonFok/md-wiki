# md-wiki

```
Running the backend
```
- cd wiki-backend/
- source bin/activate
- uvicorn main:app --reload
- Note: wiki-backend/ is a virtual environment

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