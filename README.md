# Vehicle Monitoring System

### PUP-2, 2021 Capstone Project

#### Agricultural and Biological Engineering Department, Purdue University

---

In the first part, the team created programs to integrate data collected from different sensors. The goal of this part
is to collect data from different sensors and output data in a readable and processable format for storage (currently
in charge of PUP-1) and analysis. The current output format is *txt*.


**Data Acquisition**:
- GPS
- Engine temperature
- Engine RPM

In the second part of this project, the team analyzed the raw data and interacted with the driver about the vehicle
status and routing.

**Data Analysis**:
- Job scheduler (click [here](http://35.224.122.42/scheduler.php) for preview)
- Status checker

The job scheduler will output the nearest farm based on the current location. By using this feature, the driver will
be aware of the optimal farm to go to next.

The status checker will show alerts to the driver if the temperature or RPM is above the threshold.


**Cautions:**
- The team has decided to move most of the data analysis features to the webpage for better accessibility.
More details about the webpage are given at the end.

- Fields that can be manually changed are *highlighted* in the source code.

**How to Use This Project?**
- Create a new folder and initialize a local git repo there.
- Add this repo as the remote repo.  
- Download or clone the repository to your local machine.
- Type "./main" to run the project.
- To stop the project, press Enter. This will stop the program firmly.

**Prerequisite of Your Raspberry Pi**
- All sensors are connected correctly to the Raspberry Pi following the guideline
- Install the required Python modules: GPS
- To acquire GPS and RPM data, users need to configure the OS based on the tutorials provided for each data
  acquisition tools. Failed to do so may result in running the project unsuccessfully. 

---
We would like to share PUP-1 team's [repository](https://github.com/oscarhzf/pup) here. Their project is about
the webpage and data representation.

We want to express our genuine thanks to our instructor, Dr. John Lumkes, our instructor, Mr. David Wilson, and the PUP-1
team for cooperating with us this whole year. We can't finish this project without the help from you guys.

If you have any questions or comments, feel free to contact us! We are more than happy to help you and improve our project
meanwhile.

- Rundong Peng, peng209@purdue.edu
- Colin Wu, wu1418@purdue.edu
- Tianzhang Zhao, zhao770@purdue.edu
