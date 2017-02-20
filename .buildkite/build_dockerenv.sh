#!/bin/bash

make writeversion
KOLIBRI_VERSION=`cat kolibri/VERSION`
KOLIBRI_DOCKER_IMAGE_NAME=kolibri-$KOLIBRI_VERSION.dockerimg

make dockerenvbuild
docker image save learningequality/kolibri:$KOLIBRI_VERSION -o $KOLIBRI_DOCKER_IMAGE_NAME
buildkite-agent artifact upload $KOLIBRI_DOCKER_IMAGE_NAME
