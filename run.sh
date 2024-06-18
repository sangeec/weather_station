#!/bin/bash

echo 'Please ensure your Weather Station HAT is connected to your Raspberry Pi, with the battery installed.'
echo 'Please ensure your Raspberry Pi is connected to the Internet'




## Setup rc.local to start weatherstaion daemon
sudo sed -i '/exit 0/d' /etc/rc.local
echo 'echo "Starting Weather Station daemon..."' | sudo tee -a /etc/rc.local
echo '/home/sangeetha/Documents/weather_station/weather_final/interrupt_daemon_v2.py start' | sudo tee -a /etc/rc.local
echo 'exit 0' | sudo tee -a /etc/rc.local


## Alter crontab for periodic uploads
crontab < crontab.save

echo 'After executing cron'
