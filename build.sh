#!/bin/bash

set -e

docker compose down --volumes --remove-orphans

docker compose build

docker compose up -d
