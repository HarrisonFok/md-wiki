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
Building the frontend
```
- npm run build

```
Tests
```
- Unit testing is for components, but here, I don't have any components. I only have views.

```
Running the container
```
- Go to the root project directory
- docker-compose up
