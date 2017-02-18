l#!/usr/bin/env bash

buildkite-agent artifact download '*.dockerimg'
docker image load *.dockerimg
make dockerenvdist
buildkite-agent artifact upload 'dist/*.whl'
buildkite-agent artifact upload 'dist/*.tar.gz'
