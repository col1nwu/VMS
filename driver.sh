#!/bin/bash

echo "Welcome to the vehicle monitoring system of PUP vehicles"

echo -n > gps_data.txt
echo -n > rpm_data.txt
echo -n > temp_data.txt

echo "Please identify your vehicle ID"
read vid

sudo pigpiod 2> /dev/null
echo -n > ./data/pid.txt

python3 pupgps.py $vid &
echo $! >> ./data/pid.txt
echo "GPS sensor started successfully"

python3 temp.py $vid &
echo $! >> ./data/pid.txt
echo "Temperature sensor started successfully"

python3 read_RPM.py $vid &
echo $! >> ./data/pid.txt
echo "RPM sensor started successfully"

echo "You're good to go!"

while true; do
    sleep 10

    scp -i ~/.ssh/bitnami ./data/gps_data.txt bitnami@34.70.16.172:/opt/bitnami/apache/htdocs/data
    scp -i ~/.ssh/bitnami ./data/rpm_data.txt bitnami@34.70.16.172:/opt/bitnami/apache/htdocs/data
    scp -i ~/.ssh/bitnami ./data/temp_data.txt bitnami@34.70.16.172:/opt/bitnami/apache/htdocs/data

    echo -n > gps_data.txt
    echo -n > rpm_data.txt
    echo -n > temp_data.txt
done