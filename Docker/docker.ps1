docker pull nginx:1.25
docker pull nginx:stable
docker ps # lists running containers
docker image # lists pulled images

docker run nginx:stable

docker run -d nginx:1.25 # run detached
docker logs 1700e09923f2 # {container_id}
docker ps 

# We can also run an images that hasn`t been pulled. If the image is not available locally, it will be pulled automatically
docker run nginx:bookworm-perl
docker stop 1700e09923f2

docker run -d -p 9000:80 nginx:stable # -p flag means publish, and we specify {HOST_PORT}:{CONTAINER_PORT}

docker pd -a # lists all the containers, also stopped ones

docker start 7d75ac40efd6 # {container_id} in order to start container that was stopped, without creating new one

docker stop 6e537b1f3de2 trusting_jackson # you can also use container name
docker run --name alicjas_container -d -p 9000:80 nginx:stable # creating image with a name
docker logs alicjas_container

# Now create your own app in Gradio that will print a Pandas dataframe
docker build -t first_python_docker:1.0 .
docker run -p 7860:7860 -d first_python_docker:1.0


