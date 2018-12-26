#Objective of the program is to copy a file or move a file or delete a file and to log the data.
#we have used several input calls to create a user friendly code as well as environment. 
#The code focuses on the response given by the user for whether to delete a file , copy a file or even move a file to another directory.
#Down in the use logging.INFO  to append data to the log file named FileHandlingRecord whereas print to display the output to the user. 
#Imported necessary libraries to allow necessary functions to be called.
#Python uses OS and OS.PATH to work inbuilt functions related to os.
#We imported time to use time related function like asctime.
#We imported logging library to use log based functions.
#We use logging.info to tell user that the logging level is INFO.
#Pandas is a data sciences library used to form dataframes and make the data presentable. 

#Importing the libraries
import os
import os.path
import logging
import time
import pandas as pd

#Creation of log file using logging.basicConfig to define its log level to info and to define its name and format
logging.basicConfig(filename='FileHandlingRecord.log' , level=logging.INFO,
                   format='%(process)d : %(processName)s :%(message)s')

#Program is asking you ,which function do you want to perform     
function = int(input("What is the function you want to perform, Enter 1 for copy , 2 for move , 3 for delete : "))

#Variables declared for further use in dataframe 
functiondetails = ''
labels = ['File Previous Location','Function Number','New location']

if function == 1:

    function == 'copy'
    #Program asking for inputs
    filepath = input("Enter the file path : ")
    location_to_transfer_to = input(" Enter the location to copy to : ") 

    #Program is copying the file to another location and logging.
    os.popen("xcopy {} {}".format(filepath,location_to_transfer_to))
    print('The file - {} is now copied to the location - {} '.format(filepath,location_to_transfer_to))

    #The log file is created or appended here with the same message as in print
    logging.info('This log was created at {}'.format(time.asctime()))
    logging.info(" 1 - Copy , 2 - Move , 3 - Delete -> Function Number reference")
    d = pd.DataFrame([filepath,function,location_to_transfer_to],labels,[functiondetails]) #Here the dataframe is being formed
    logging.info(d)                                                                        #Dataframe is being logged here
    logging.info('This log ended at {}'.format(time.asctime()))
    
elif function == 2:
    
    function == 'move'
    
    #Program asking for inputs
    filepath = input("Enter the file path : ")
    destfolder = input("Enter the location to transfer to : ")
        
    #Program is moving the file from one folder to another and logging.
    os.popen("move {} {}".format(filepath,destfolder))
    print.info('The file - {} is now moved to the location - {} '.format(filepath,destfolder))

    #The log file is created or appended here with the same message as in print 
    logging.info('This log was created at {}'.format(time.asctime()))
    logging.info(" 1 - Copy , 2 - Move , 3 - Delete")
    d = pd.DataFrame([filepath,function,destfolder],labels,[functiondetails])   #Here the dataframe is being formed
    logging.info(d)                                                             #Dataframe is being logged here
    logging.info('This log ended at {}'.format(time.asctime()))
    
elif function == 3:
    
    function = 'delete'
    #Program asking for input
    file_to_delete = input("Enter the path of the file you want to delete : ")
    
    #Variable declared for dataframe to be created in log file
    filelocation = 'deleted'
        
    #Program is deleting the file from the location location and logging.
    os.popen(" DEL /A {} ".format(file_to_delete))
    print('The file- {} is now deleted '.format(filepath))

    #The log file is created or appended here with the same message as in print 
    logging.info('This log was created at {}'.format(time.asctime()))
    logging.info(" 1 - Copy , 2 - Move , 3 - Delete")
    d = pd.DataFrame([file_to_delete,function,filelocation],labels,[functiondetails])   #Here the dataframe is being formed
    logging.info(d)                                                                     #Dataframe is being logged here
    logging.info('This log ended at {}'.format(time.asctime()))
    