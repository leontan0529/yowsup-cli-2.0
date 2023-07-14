#!/usr/bin/bash
export PATH=$PATH:/usr/bin
cd /home/ec2-user/yowsup-cli-2.0/yowsup/env

python3 env_scrape.py
python3 env_utilities.py WhatsApp.apk