# Dockerfile created by Alexandre
# currently uploaded on hub.docker.com under version 2.2

ARG BASE_CONTAINER=jupyter/scipy-notebook:7d427e7a4dde
FROM $BASE_CONTAINER

# We need root for apt
USER root

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

RUN mkdir exchange
RUN chmod -R 777 exchange

# Install python-java driver (dependency for beakerx)
RUN pip install py4j
# Install beakerx with pip
RUN pip install beakerx
# Run install script
RUN beakerx install

# To initialize this nbextension in the browser every time the notebook (or other app) loads:
RUN jupyter nbextension enable beakerx --py --sys-prefix #changed from --user to --sys-prefix

# Try latest nbgrader version (v0.6.0)
RUN pip install git+https://github.com/jupyter/nbgrader

RUN jupyter nbextension install --sys-prefix --py nbgrader --overwrite
RUN jupyter nbextension enable --sys-prefix --py nbgrader
RUN jupyter serverextension enable --sys-prefix --py nbgrader

# NBGrader config file
COPY nbgrader_config.py /etc/jupyter/

EXPOSE 8888

RUN nbgrader quickstart act
CMD ["jupyter", "notebook", "--allow-root"]