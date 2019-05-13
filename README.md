# Logs Analysis

This is one of Udacity's Full Stack Web Developer Nanodegree Program 's projects using Python and PSQL. 
The project involves displaying insights from a news data stored in a database.

### To run the project:

1. Have [Vagrant](https://www.vagrantup.com/), [Visual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and a [VM Configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) installed.
2. Being inside the VM Configuration folder, get the virtual machine working by running in your terminal 'vagrant up' and log in with 'vagrant ssh'.
3. Download the database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and move the 'newsdata'.sql file in the 'vagrant' folder inside the VM Configuration Folder.
4. To load the data ‘cd’ into the ‘vagrant’ folder as stated in the terminal and run 'psql -d news -f newsdata.sql'

To create views, run 'psql -d news' in the terminal and add the following code...:

```
CREATE VIEW existinglogs AS
SELECT time as Date, count(*) as countAllLogs
FROM log
GROUP BY Date
```

```
CREATE VIEW failedlogs AS
SELECT time as Date, count(*) as countFailedLogs
FROM log
WHERE STATUS like '%4%' 
OR STATUS like '%5%'
GROUP BY Date
```

...and exit with '\q'

6. Inside the 'vagrant' folder add the 'logsAnalysis.py’ and run 'python logsAnalysis.py' in the terminal to see the results. 
