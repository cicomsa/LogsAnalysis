# Logs Analysis

This is one of Udacity's Full Stack Web Developer Nanodegree Program 's projects using Python and PSQL. 
The project involves displaying insights from a news data stored in a database.

### To run the project:

1. Have [Vagrant](https://www.vagrantup.com/), [Visual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and a [VM Configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) installed.
2. Being inside the VM Configuration folder, get the virtual machine working by running in the terminal ```vagrant up``` and log in with ```vagrant ssh```.
3. Download the database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and move the ```newsdata.sql``` file in the ```vagrant``` folder inside the ```VM Configuration``` folder.
4. To load the data ```cd``` into the ```vagrant``` folder as stated in the terminal and run ```psql -d news -f newsdata.sql```

To create views, run ```psql -d news``` in the terminal and add the following code...:

```
CREATE VIEW article_authors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;
```

```
CREATE OR REPLACE VIEW viewed_articles AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;
```

```
CREATE OR REPLACE VIEW errors_table AS 
SELECT date(time) AS date, count(*) AS total, 
sum(case when status != '200 OK' then 1 else 0 end) AS error 
FROM log 
GROUP BY date(time) 
ORDER BY error;
```

```
CREATE OR REPLACE VIEW failed_logs AS 
SELECT date, round(100.0*error/total,2) AS percent
FROM errors_table 
GROUP BY date, percent 
ORDER BY percent;
```

...and exit with ```\q```

6. Inside the ```vagrant``` folder add the ```logsAnalysis.py``` and run ```python logsAnalysis.py``` in the terminal to see the results. 
