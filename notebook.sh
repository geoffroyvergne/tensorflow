#!/usr/bin/env bash



docker run -it --rm \
    -v $HOME/.keras:/root/.keras \
    -v $PWD/notebooks:/notebooks \
    -p 8888:8888 \
    --name tensorflow \
    tensorflow/tensorflow