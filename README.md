# TestProblem
This repo is for a test problem to gain experience and test if applicant like TheRealSeat workflow. Problems will be assigned via this readme.

# Problem
TheRealSeat will be pulling data continuously and storing the data in S3. The data will be in csv format like example "TestData.csv". TheRealSeat needs to process, clean and store the data in a database. Additionally we will be putting summary statistics into a different table.

# Tasks
Write a python lambda function that will read the following csv, clean the data and summarize the data. Questions include
1) What is the total resale value?
2) What is the total resale value by item

# Recommendations
Attempt to solve first and then integrating to AWS. Write a pure local executable and thereafter work to port to the cloud. 
The executable should be able to read a file, process all the columns and output (to file) the answers (each a separate file)
The schema of the inputs will be consistent, assume you are writing to ingest many files.

