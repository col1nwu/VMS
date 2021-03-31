#!/bin/bash

echo "Welcome to the vehicle monitoring system for PUP vehicles"

python3 pupgps.py &
echo "GPS sensor started successfully"

python3 temp.py &
echo "Temperature sensor started successfully"

python3 read_RPM.py &
echo "RPM sensor started successfully"

echo "You're good to go!"

while true; do
    scp -i ~/.ssh/bitnami ./data/gps_data.txt bitnami@34.70.16.172:/opt/bitnami/apache/htdocs/data
    scp -i ~/.ssh/bitnami ./data/rpm_data.txt bitnami@34.70.16.172:/opt/bitnami/apache/htdocs/data
    scp -i ~/.ssh/bitnami ./data/temp_data.txt bitnami@34.70.16.172:/opt/bitnami/apache/htdocs/data

    echo -n > gps_data.txt
    echo -n > rpm_data.txt
    echo -n > temp_data.txt

    sleep 5m
done
