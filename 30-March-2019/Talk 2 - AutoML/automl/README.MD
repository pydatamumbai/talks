# AutoML

### Docker setup  
Download [Docker](https://hub.docker.com/search/?type=edition&offering=community)  
Docker [tutorial](https://www.dataquest.io/blog/docker-data-science)  
Docker python [images](https://hub.docker.com/_/python/)  

## Setup docker container for AutoML  
#### Build image  
`docker build --tag server .`  
#### Run container  
`docker run -it -p 8888:8888 server jupyter-lab --allow-root`  
#### Push changes to docker after running notebook experiments  
```  
docker ps -a #get image_id  
docker commit image_id name  
```  
#### Copy notebooks from docker to local  
```  
cd automl #on local  
docker cp image_id:/code/automl/notebooks .  
```
#### Local to docker  
`docker cp notebooks/. image_id:/code/automl/notebooks`  
#### Remove Docker images  
```  
docker system prune -a # Removes base image and its derivatives  
docker system prune # Removes image created over base  

docker image ls -q  
docker stop image_id    
docker rm image_id  
```  
