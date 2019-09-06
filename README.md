# TP-ACT  
Unil's ACT TP repository

# Installation  

## Prerequisites  
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Docker](https://docs.docker.com/v17.12/manuals/)

## Build 
### Pull jupyter image  
    sudo docker pull jupyter/scipy-notebook
(It might take a while, we are installing the whole JAVA JDK)  

    sudo docker build -t act .

## Run  

### /!\ Only tested on linux, add equivalent to $PWD for OSx and Windows 

    sudo docker run -v "$PWD/source:/home/jovyan/source/" -p 8888:8888 act


# Use nbgrader

## Access
Once your Docker image is running, you can access it in your browser through http://localhost:8888. You will be prompted for a token, it can be found by reading at the command line output of your docker image.