# Logs Analysis Project
Submitted by Doug McDonald for Udacity Full Stack Nanodegree.
I also submitted this project for the Intro to Programming Nanodegree ( BackEnd Specialization) completed in Feburary 2019 with my company AT&T. My Udacity account with AT&T is under email login **dm338t@att.com** and I submitted with GitHub user name _mrfresh382_ . I reused alot of the work, but made a few changes also. 
## System Specs
- Python 2.7.13, Vagrant 2.2.2, VirtualBox 5.2.2
- System Specs: Windows 7, 64 bit
- Used GitBash as the terminal, Windows Powershell 5.1
- Used VM provided Ubuntu 16.04, PSQL 9.5.4
- Code checked with PEP8 'pycodestyle'

## User Guide for Udacity Grader
1. Use GitBash Shell and cd to the vagrant directory
2. Open VM- `vagrant up`
3. SSH into VM- `vagrant ssh`
4. Once SSHed into VM enter `cd /vagrant`
5. From this folder you can run the project5.py file. Check to ensure it is accessible by executing `ls` command. If it is not viewable, check that you are in the '/vagrant' folder, then proceed with troubleshooting. 
6. Execute python file within VM `python project5.py`

7. (Optional) To explore the 'News' database:
```
psql news
```
7. b.  (Optional)To quit back to Vagrant:
```
\q 
```
## Notes/Issues 
- I had to update Virtual Box and Windows Management Framework 5.1 A.k.a. Powershell 5.1.
- When importing SQL queries into Python file, I had to change \/ to \\/ to make compatible with ASCII encoding and pycodestyle.
- In Sublime, I had to change the 'Tabs' to 'Spaces', this cleared out the numerous PEP warnings. 
- If the Python file is not accessible when SSHed into Vagrant, than execute the `vagrant reload` and re-attempt steps 5-6 above. If this doesn't work, then reinstall the Vagrant instance and news database on your OS using the documentation provided in the SQL lessons. 
- Ensure you have a **graceful shutdown** of vagrant instance before you shutdown or restart your OS. Use command `vagrant suspend` to prevent corrupting the news database and vagrant instance. 

## Design Notes
### Query 1
Query 1 was pretty straightforward
### Query 2
Query 2 included multiple sub-queries and required some text formatting within Python and PSQL. Articles can be joined to the Log table by striping the "/article/" path name from the Log table entry to make them join-able. This makes the output pretty and do-able. 
### Query 3
Query 3 included sub-queries and a calulation within PSQL. I converted the timestamps to remove time-of-day information. Time of day is not important and we want all the log entries on a specific day to be equal to one another for summation purposes. 
```
SELECT DISTINCT date_trunc( 'day', time) AS date_value ,
                COUNT(*) AS num_success
            FROM log
            ...
```
I had to use `cast(number AS real)` within PSQL to get the selected numbers to perform division in decimal format. Simple division '/' was easy to use. I used post-processing in Python to round the output to 3 decimal points. I tried to round the output in PSQL, but couldn't get it to work. 
```
round(error_days[1], 3)
```
- We are assuming 200 series codes are successful and 400 series produce an error. Throgh analysis of the log file, there were no 300 series or 400 series for the test server, but the python file will search for code 300 as good requests and 500 as bad requests. 


