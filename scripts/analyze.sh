#!/bin/bash
# -------------------------------------------------------
# Copyright (c) [2022] Nadege Lemperiere
# All rights reserved
# -------------------------------------------------------
# Module to deploy an aws permission set with all the secure
# components required
# Bash script to launch module static analysis
# -------------------------------------------------------
# Nadège LEMPERIERE, @13 january 2022
# Latest revision: 13 january 2022
# -------------------------------------------------------

# Retrieve absolute path to this script
script=$(readlink -f $0)
scriptpath=`dirname $script`

# Launch tests in docker container
docker run  -it --rm \
            --volume $scriptpath/../:/home/test/module:rw \
            --workdir /home/test/module \
            nadegelemperiere/terraform-python-awscli:v3.0.0 \
            ./scripts/lint.sh $@