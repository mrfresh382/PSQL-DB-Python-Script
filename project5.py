#!usr/bin/python

# Project 5 Logs Analysis for IPND
# Submitted by Doug McDonald
# Used Python 2.7.13, Vagrant 2.2.2, VirtualBox 5.2.2
# System Specs: Windows 7, 64 bit
# Used GitBash as the terminal, Windows Powershell 5.1
# Used VM provided Ubuntu 16.04, PSQL 9.5.4

import datetime
import psycopg2

db_name = 'news'

query_1 = '''
    SELECT b.title, a.num_views
    FROM
        (SELECT regexp_replace(path,('\\/article\\/'), '') AS top3,
            count(path) AS num_views
        FROM log
        WHERE path LIKE '\\/article\\/%'
        GROUP BY path
        ORDER BY num_views DESC
        LIMIT 3) AS a ,
        articles AS b
    WHERE b.slug LIKE a.top3
    ORDER BY a.num_views DESC;
'''
# Query 1 finds the instances where the begining of the path is "\article\"

query_2 = '''
    SELECT authors.name,  sum(rawcount.num_views)
    FROM
        articles
        JOIN
        authors ON authors.id = articles.author
        JOIN rawcount ON rawcount.title = articles.title
    GROUP BY authors.name
    ORDER BY sum(rawcount.num_views) DESC;
'''

# Query 2 finds the number of authors by joining all three tables
# , formating the path with the regexp_replace function. The log table
# is linked to the articles table by the 'slug' field. I created  view_2
# 'rawcount' which is joined in Query2 on authors and articles table on the
# author id code

view_2 = '''
    CREATE VIEW rawcount AS
    SELECT b.title, a.num_views
    FROM
        (SELECT regexp_replace(path,('\\/article\\/'), '') AS top3,
            COUNT(path) AS num_views
        FROM log
        WHERE path LIKE '\\/article\\/%'
        GROUP BY path
        ORDER BY num_views DESC) AS a ,
        articles AS b
    WHERE b.slug LIKE a.top3
    ORDER BY a.num_views DESC
    LIMIT 8;
'''
# View_2 is made to make Query_2 more readable

query_3 = '''
    SELECT error_ratio_table.error_date_notime AS date,
        error_ratio_table.percent_errors AS percent
    FROM
        (SELECT success.date_value AS error_date_notime ,
            cast(errors.num_error AS real)/
                (cast(success.num_success AS real)+
                cast(errors.num_error AS real))* 100.00
            AS percent_errors
        FROM
            (SELECT DISTINCT date_trunc( 'day', time) AS date_value ,
                COUNT(*) AS num_error
            FROM log
            WHERE status LIKE '4%'
            GROUP BY date_value
            ORDER BY num_error DESC) AS errors
            JOIN
            (SELECT DISTINCT date_trunc( 'day', time) AS date_value ,
                COUNT(*) AS num_success
            FROM log
            WHERE status LIKE '2%'
            GROUP BY date_value
            ORDER BY num_success DESC ) AS success
            ON errors.date_value=success.date_value
        ORDER BY percent_errors DESC) AS error_ratio_table
    WHERE error_ratio_table.percent_errors > 1.00;
'''
# Query 3 creates two queries that count the number of 200 and 404
# codes for each day
# The Percent is derived by dividing the number of 404 codes by the
# total number of code 200's and 404's for each distinct day within the log
# All of the datetime stamps have the time removed so they read
# 00:00:00 as the time. I used this method from the Knowledge Forum

# Connection to POSGRESQL server is initiated from within the virtual machine
connection = psycopg2.connect(database=db_name)
c = connection.cursor()

# Answer 1
c.execute(query_1)
answer_1 = c.fetchall()

# A VIEW is created to more easily read the answer to question 2
# Do not run the next line if the view is already created
c.execute(view_2)

# Answer 2
c.execute(query_2)
answer_2 = c.fetchall()

# Answer 3
c.execute(query_3)
answer_3 = c.fetchall()

print ''
print 'Top Three Articles of all Time'  # Prints out answer 1,
# Article is stored in column 0 and the views are stored in column 1
top3_number = 1
for popular_articles in answer_1:
    print top3_number, ':', popular_articles[0], ': ', \
        popular_articles[1], 'views'
    top3_number = top3_number+1
print ''

print 'Authors Ranked by number of Views'  # Prints out answer 2,
# Authors are in column 0 and their views in column 1
top_authors = 1
for popular_authors in answer_2:
    print top_authors, '-', popular_authors[0], ': ', popular_authors[1]
    top_authors = top_authors+1

print ''
print 'Day(s) with errors greater than 1% of total web hits'
# Prints out the days with errors greater than 1% of total web hits
# Code 4-- represent errors ( 404 Not Found) and Code 2-- represent
# Successful page hits ( 200 Ok)
for error_days in answer_3:
    print error_days[0].date(), ': ', round(error_days[1], 3), "%"

c.execute('DROP VIEW rawcount;')  # Drops the view_2 used for Answer 2
connection.close()
