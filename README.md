# Vehicle Monitoring System

### PUP-2, 2021 Capstone Project

#### Agricultural and Biological Engineering Department, Purdue University

---

In the first part, the team creates data fetchers to integrate data collected from
different sensors. The goal of this part is to collect data from different sources and output data in a readable and
processable format for storage (currently in charge of PUP-1) and analysis.


**Data Acquisition**:
- GPS
- Engine temperature
- Engine RPM

In the second part of this project, the team analyzes the raw data and
interacts with the driver about the vehicle status and routing.

**Data Analysis**:
- Job scheduler (click [here](http://35.224.122.42/scheduler.php) for a preview)
- Status checker
- Trendline generator

*The team has decided to move most of the data analysis features to the webpage which can be found in PUP-1's project.
More details are given at the end.*

**How to Use This Project?**
- Download or clone the repository to your local machine.
- Go inside the directory.
- Type "./main" to run the project.
- To stop the project, press Enter as instructed on the screen.

**Prerequisite of Your Local Machine**
- All sensors are connected correctly to the Raspberry Pi following the guideline
- The operating system is **Linux**
- **Terminal** is available for typing in commands
- Install the required Python modules: GPS
- To acquire GPS and RPM data, users need to configure the Linux system based on the tutorials provided for each data
  acquisition tools. Failed to do so may result in running the project unsuccessfully. 

---
We would also like to share PUP-1 team's [repository](https://github.com/oscarhzf/pup) here. Their project is about
the webpage and data representation.

If you have any questions or comments, feel free to contact us! We are more than happy to help you and improve our code
meanwhile.

Colin Wu, wu1418@purdue.edu
