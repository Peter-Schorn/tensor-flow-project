#!/bin/bash

aws ecr-public get-login-password --region us-east-1 | \
docker login --username AWS --password-stdin public.ecr.aws/h4z3r8p2

docker build . -t public.ecr.aws/h4z3r8p2/tensor:latest
docker push public.ecr.aws/h4z3r8p2/tensor:latest
