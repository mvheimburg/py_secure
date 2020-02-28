# base-image for python on any machine using a template variable,
# see more about dockerfile templates here: https://www.balena.io/docs/learn/develop/dockerfile/
# FROM balenalib/raspberrypi3-python:3.7.6-latest
# FROM balenalib/raspberrypi3-python:3-build
FROM balenalib/raspberrypi3-python:3.7-build

# use `install_packages` if you need to install dependencies,
# for instance if you need git, just uncomment the line below.
# RUN install_packages git


RUN python --version
RUN apt update
RUN apt upgrade
RUN apt install apt-utils && \
    apt install rpi.gpio && \
    apt install python3-gpiozero

ENV APP_DEV = /usr/src/app

# Set our working directory
WORKDIR "${APP_DEV}"

# Copy requirements.txt first for better cache on later pushes
COPY requirements.txt requirements.txt

# pip install python deps from requirements.txt on the resin.io build server
RUN pip install -U pip && \
    pip install -U setuptools && \
    pip install -U wheel

RUN pip install -r requirements.txt

# This will copy all files in our root to the working  directory in the container
COPY . ./

# Enable udevd so that plugged dynamic hardware devices show up in our container.
ENV UDEV=1

# main.py will run when container starts up on the device
CMD ["python","-u","src/main.py"]