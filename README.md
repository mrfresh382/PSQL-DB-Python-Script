# Project-5---Udacity IPND
# Submitted by Doug McDonald
# Used Python 2.7.13, Vagrant 2.2.2, VirtualBox 5.2.2
# System Specs: Windows 7, 64 bit
# Used GitBash as the terminal, Windows Powershell 5.1
# Used VM provided Ubuntu 16.04, PSQL 9.5.4
# Code checked with PEP8 'pycodestyle'

# To run:
# Use GitBash Shell
# Open VM- 'vagrant up'
# SSH into VM- 'vagrant ssh'
# Once SSHed into VM enter 'cd /vagrant'
# From this folder you can run the project5.py file
# If the view 'view_2' is in the system, please delete now from database
# Go into news database : 'psql news' -> 'drop view rawcount;'
# Exit news database '\q'
# Execute python file 'python project5.py'
#

# Notes/Issues - I had to update Virtual Box and Windows Management Framework 5.1
# A.k.a. Powershell 5.1
# When importing SQL queries into Python file, I had to change
# \/ to \\/ to make compatible with ASCII encoding and pycodestyle.
# In Sublime, I had to change the 'Tabs' to 'Spaces', this cleared
# out the numerous PEP warnings. 
