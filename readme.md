# Docker

docker build -t cobanov-homepage .

docker run -d -p 5000:5000 cobanov-homepage

docker-compose up -d

docker tag my-flask-app your-dockerhub-username/my-flask-app
docker push your-dockerhub-username/my-flask-app
