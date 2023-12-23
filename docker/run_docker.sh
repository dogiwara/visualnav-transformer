#!/bin/bash

USER="docker"
WORK_DIR="$HOME/catkin_ws/src"
PKG_NAME="visualnav-transformer"
DATA_DIR="/share/private/28th/ogiwara/general_navigation"
docker run \
    --gpus all \
    --ipc=host \
    --net=host \
    --rm \
    -it \
    --privileged \
    -v $WORK_DIR/$PKG_NAME:/root/catkin_ws/src/$PKG_NAME \
    --mount type=bind,source=${DATA_DIR},target=/data \
    -w /root \
    test-visualnav-transformer \
    bash \
    --login
