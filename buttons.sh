#!/usr/bin/env bash
printf "Copying CI_JOB_ID: ""$CI_JOB_ID"" to TRAVIS_JOB_ID\n"
export TRAVIS_JOB_ID="$CI_JOB_ID"
printf "TRAVIS_JOB_ID: ""$TRAVIS_JOB_ID"

coveralls
