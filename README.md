# MentorSkool


1  error occured while working on sql is that Host localhost is not allowed to connect to this MYsql or MariaDB server (error:- 1130) . To overcome this ,

Go to Xampp Folder -> go to mysql folder -> select my.ini file and write skip-grant-tables as mentioned below

[mysqld] 
port=3306 
skip-grant-tables 

save the file and restart your server.
