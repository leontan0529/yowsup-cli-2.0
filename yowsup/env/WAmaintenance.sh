#This file to be added to cronjob, interval of cronjob is up to developer

#! /bin/bash

python3 env_scrape.py

python3 env_utilities.py
