docker commands::
====================
docker login
docker build -t shlomowind/my-mongo-image:latest .
docker run -d --name my-mongo-container -p 8000:8000 shlomowind/my-mongo-image:latest
docker ps
docker logs <CONTAINER_ID>
docker push shlomowind/my-mongo-image:latest