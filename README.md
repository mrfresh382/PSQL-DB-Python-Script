# Project-5---Udacity IPND
# Used Python 2.7.13, Vagrant 2.2.2, VirtualBox 5.2.2
# System Specs: Windows 7, 64 bit
# Used GitBash as the terminal, Windows Powershell 5.1
# Used VM provided Ubuntu 16.04, PSQL 9.5.4
# Code checked with PEP8 'pycodestyle'

# To run:
# Use GitBash Shell and 'cd' to the vagrant directory
# Open VM- 'vagrant up'
# SSH into VM- 'vagrant ssh'
# Once SSHed into VM enter 'cd /vagrant'
# From this folder you can run the project5.py file
# If the view 'view_2' is in the news database, please delete now from database
# To delete: Go into news database : 'psql news' -> 'drop view rawcount;'
# Exit news database '\q'
# Execute python file within VM 'python project5.py'
#
# I have created a view HOWEVER, it will create itself in the python file.
# To create the view: please enter this query in the "news" database:
#       
    CREATE VIEW rawcount AS
    SELECT b.title, a.num_views
    FROM
        (SELECT regexp_replace(path,('\/article\/'), '') AS top3,
            COUNT(path) AS num_views
        FROM log
        WHERE path LIKE '\/article\/%'
        GROUP BY path
        ORDER BY num_views DESC) AS a ,
        articles AS b
    WHERE b.slug LIKE a.top3
    ORDER BY a.num_views DESC
    LIMIT 8;
 # My Python file project5.py will delete the view after running the code
 # If you use the above view before running the Python file, 
 # Please make LINE 109 a comment!!!

# Notes/Issues - I had to update Virtual Box and Windows Management Framework 5.1
# A.k.a. Powershell 5.1
# When importing SQL queries into Python file, I had to change
# \/ to \\/ to make compatible with ASCII encoding and pycodestyle.
# In Sublime, I had to change the 'Tabs' to 'Spaces', this cleared
# out the numerous PEP warnings. 
