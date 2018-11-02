#!/usr/bin/env bash

docker run -it --rm -v $HOME/.keras:/root/.keras -v $PWD:/workspace -w /workspace tensorflow/tensorflow:latest-py3 python $1
