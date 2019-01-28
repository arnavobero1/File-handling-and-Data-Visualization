#This program is a connection between an excel file and python and generator for interactive plots.
#The program uses few data science libraries.
#Pandas is imported for formation of dataframes.
#Pandas is also imported for the reason of importing excel file data in form of dataframes.
#Plotly is the library used to make the plots interactive.
#We imported time to use time related function like asctime.

#Importing the libraries
import os
import logging
import time
import pandas as pd
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import cufflinks as cf
cf.go_offline()


#Creation of log file using logging.basicConfig to define its log level to info and to define its name and format
logging.basicConfig(filename='FileHandlingRecord.log' , level=logging.INFO,
                   format='%(process)d : %(processName)s :%(message)s')

#Program is asking you ,which function do you want to perform     
print("\n")
print("WARNING : FOR VIUSALIZATION THE CODE SO FAR SUPPORTS ONLY JUPYTER NOTEBOOK,WORK IN PROGRESS FOR CMD.\n")
   
#The program is asking for input for location of file to be opened.
filepath = input("Enter the excel file path along with the file you want to open : ")
#Example path - C:\Arnav\Excel visualization\Visualizationsheet.xlsx

#List for labels for dataframe further made in program.
labels = ['File Destination','Type of graph']
functiondetails = ' '    

#Replay function for while loop further ahead in code is being created.
def replay():
    
    return input('Do you want to do it again? Enter Yes or No: ').lower().startswith('y')
    
#The program is opening and displaying the excel file data and storing it as a dataframe.
con = pd.read_excel('{}'.format(filepath))
print(con)

#Here the program is asking for input for the kind of graph the user wants based on the given options.
while True:
    Type = input("What kind of graph do you want ?Bar?Line?Histogram?Boxplot?")
    if Type == "bar":
        con.iplot(kind = 'bar')
    if Type == "line":
        con.iplot(kind = 'line')
    if Type == "histogram":   
        con.iplot(kind = 'histogram')
    if Type == "box":
        con.iplot(kind = 'box')
        
	#The log file is created or appended here with the a message.
	logging.info('This log was created at {}'.format(time.asctime()))
	d = pd.DataFrame([filepath,Type],labels,[functiondetails])   		  #Here the dataframe is being formed
	logging.info(d)                                                       #Dataframe is being logged here
	logging.info('This log ended at {}'.format(time.asctime())) 
        
    if not replay():
        break
print("Thank you for using our program!")