docker network create mongo-network
docker network ls
$ docker network rm mongo-network

docker run -d \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=supersecret \
--network mongo-network \
--name mongodb \
mongo

docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=supersecret \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
--network mongo-network \
--name mongo-express \
mongo-express

docker-compose -f docker-compose.yaml up -d
docker-compose -f docker-compose.yaml down # stops and removes the containers

# Sometimes you made changes in the db and you want to keep it, and thus you do not want to remove the container, 
# but rather stop it
docker-compose -f docker-compose.yaml stop
docker-compose -f docker-compose.yaml start 