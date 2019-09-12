# TP-ACT

Unil's ACT TP repository

# Installation

## Disclaimer

The installation has only been tested on Ubuntu 18.04 and OSx.

Docker being ubiquitous for all linux flavours, it should not be a problem on other Linux distributions. However, Windows might be an issue, therefore, a Windows specific documentation could be required.

## Prerequisites

-   [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
-   [Docker](https://docs.docker.com/v17.12/manuals/)

## Build

### Pull jupyter image

    sudo docker pull jupyter/scipy-notebook

(It might take a while, we are installing the whole JAVA JDK)

    sudo docker build -t act .

## Run

### /!\ Only tested on linux and OSX, add equivalent to \$PWD for Windows

    sudo docker run -v "$PWD/source:/home/jovyan/source/" -p 8888:8888 act

# Use nbgrader

## Access

Once your Docker image is running, you can access it in your browser through http://localhost:8888. You will be prompted for a token, it can be found by reading at the command line output of your docker image.


