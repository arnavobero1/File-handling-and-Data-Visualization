#!/usr/bin/env python

#Objective of the program is to copy a file or move a file or delete a file and to log the data.
#The other objectives of the program is to rename a file or analyze the content of a file.
#we have used several input calls to create a user friendly code as well as environment. 
#The code focuses on the response given by the user for whether to delete a file , copy a file or move a file to another directory or renaming a file or analyzing its content.
#Down in the program we use logging.INFO  to append data to the log file named FileHandlingRecord whereas print to display the output to the user. 
#Imported necessary libraries to allow necessary functions to be called.
#Python uses OS and OS.PATH to work inbuilt functions related to os.
#We imported time to use time related function like asctime.
#We imported logging library to use log based functions.
#We use logging.info to tell user that the logging level is INFO.
#We imported Collections library to use the counter function.
#Pandas is a data sciences library used to form dataframes and make the data presentable. 
#Further more libraries like seaborn and matplotlib have been used to create visualization from given data.
#Plotly and cufflinks are used to create interactive visualizations.

"""
Till now the file types supported for renaming are-

1 - .txt
2 - .bmp
3 - .pptx
4 - .xlsx
5 - .PNG
6 - .jpeg
7 - .rtf
8 - .docx
9 - .pdf
10 - .py
11 - .c
12 - .gif
13 - .java
14 - .jpg

"""

#Importing the libraries
import os
import logging
from collections import Counter
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
try:
    print("\n")
    print("Welcome user,feel free to explore our program and utilise it!")
    print("Enter 1 for copy , 2 for move , 3 for delete, 4 for Data analysis ")
    print("5 for Renaming a file , 6 for Data visualization")
    print("WARNING : FOR VIUSALIZATION THE CODE SO FAR SUPPORTS ONLY JUPYTER NOTEBOOK,WORK IN PROGRESS FOR CMD.\n")
    function = int(input("What is the function you want to perform:"))
except ValueError:
    sys.exit()

#Variables declared for further use in dataframes 
functiondetails = ''
labels = ['File Previous Location','Function Number','New location']
labels2 = ['Filepath','Function Number','Number of files being read','Word seached']
labels3 = ['File Destination','Function Number','Old name','New name']
labels4 = ['File Destination','Function Number','Type of graph']

if function == 1:

    function == 'copy'
    #Program asking for inputs
    filepath = input("Enter the file path : ")
    location_to_transfer_to = input(" Enter the location to copy to : ") 

    #Program is copying the file to another location and logging.
    os.system("copy {} {}".format(filepath,location_to_transfer_to))
    print('The file - {} is now copied to the location - {} '.format(filepath,location_to_transfer_to))

    #The log file is created or appended here with the same message as in print
    logging.info('This log was created at {}'.format(time.asctime()))
    logging.info(" 1 - Copy , 2 - Move , 3 - Delete, 4 - Data analysis , 5 - File renaming , 6 - Data Visualization")
    d = pd.DataFrame([filepath,function,location_to_transfer_to],labels,[functiondetails]) #Here the dataframe is being formed
    logging.info(d)                                                                        #Dataframe is being logged here
    logging.info('This log ended at {}'.format(time.asctime()))
    
elif function == 2:
    
    function == 'move'
    
    #Program asking for inputs
    filepath = input("Enter the file path : ")
    destfolder = input("Enter the location to transfer to : ")
        
    #Program is moving the file from one folder to another and logging.
    os.system("move {} {}".format(filepath,destfolder))
    print('The file - {} is now moved to the location - {} '.format(filepath,destfolder))

    #The log file is created or appended here with the same message as in print .
    logging.info('This log was created at {}'.format(time.asctime()))
    logging.info(" 1 - Copy , 2 - Move , 3 - Delete, 4 - Data analysis , 5 - File renaming , 6 - Data Visualization")
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
    os.system(" DEL /A {} ".format(file_to_delete))
    print('The file- {} is now deleted '.format(filepath))

    #The log file is created or appended here with the same message as in print 
    logging.info('This log was created at {}'.format(time.asctime()))
    logging.info(" 1 - Copy , 2 - Move , 3 - Delete, 4 - Data analysis , 5 - File renaming , 6 - Data Visualization")
    d = pd.DataFrame([file_to_delete,function,filelocation],labels,[functiondetails])   #Here the dataframe is being formed
    logging.info(d)                                                                     #Dataframe is being logged here
    logging.info('This log ended at {}'.format(time.asctime()))


if function == 4:
    
    sort = input("Do you want to open one file or multiple?")
    
    if sort == "one": 
        #The program is asking for input for the folder of the files to be analysed.
        try:    
            folderdest = input("Enter folder destination: ")
            files = os.listdir('{}'.format(folderdest))
            print(files)
        except ValueError:
            sys.exit()  
        #Replay function for while loop further ahead in code is being created
        def replay():
            return input('Do you want to analyse another file? Enter Yes or No: ').lower().startswith('y')
        def replay2():
                return input('Do you want to search another word?Enter Yes or No: ').lower().startswith('y')
        #The files are now being stored in a dictionary and the content of the chosen file is being read.
        while True:
            list1 = []
            filename = input()
            if filename in files:
                dict_with_files_data = {}
                with open('{}\{}'.format(folderdest,filename)) as f:
                    dict_with_files_data[filename] = f.read()
                for i, j in dict_with_files_data.items():
                    print(f'Content of file  {i} is : {j}')
                    #Content of each file is being stored into a list for further use in program.
                    list1 = j.split()
            else:
                print('Whoop! try again.')
                break
            #Here the program uses counter which helps us find the number of times an element in the list occurs with the element beside it
            from collections import Counter
            c = Counter(list1)
            print("The number of time each element was used is = ")
            for word, count in c.most_common(): 
                print (word,count)
            print('\n')

            #Here we are finding the number of times the word occured depending on the word chosen by the user.
            while True:
    
                #Programs asks for word input
                word=input("Enter word or number to be searched:")    
                ck = 0
                for letter in list1:
                    if(letter == word):
                        ck = ck+1
                   
                print("Occurrences of the word or number {} :".format(word))
                print(ck)        

                if not replay2():
                    break
            if not replay():
                break
    
    elif sort == "multiple":
        
        list1 = []
        #The program is asking for input for the folder of the files to be analysed.
        folderdest = input("Enter folder destination: ")
        files = os.listdir('{}'.format(folderdest))
        print(files)
        #The files are now being stored in a dictionary and their content is being read.
        dict_with_files_data = {}
        for i in files:
            with open('{}\{}'.format(folderdest,i)) as f:
                dict_with_files_data[i] = f.read()
        for i, j in dict_with_files_data.items():
            print(f'Content of file  {i} is : {j}')
            list1.append(j)
            
            #Content of each file is being stored into a list for further use in program.
            my_file = open('test.txt','w+')
            my_file.write('{}'.format(list1))
            my_file.seek(0)
            
        with open('C:\\Arnav\\Advancecmd\\test.txt') as f:
            split1 = f.read()
            list2 = split1.split()
            list2
        
        #Replay function for while loop further ahead in code is being created
        def replay():
            return input('Do you want to try it again? Enter Yes or No : ').lower().startswith('y')

        #Here the program uses counter which helps us find the number of times an element in the list occurs with the element beside it.
        c = Counter(list2)
        print('\n')
        print("The number of time each element was used is = ")
        for word, count in c.most_common(): 
            print (word,count)
        print('\n')
    
        #Here we are finding the number of times the word occured depending on the word chosen by the user.
        while True:
    
            #Programs asks for word input
            word=input("Enter word or number to be searched: ")    
            ck = 0
            for letter in list2:
                if(letter == word):
                    ck = ck+1
                   
            print("Occurrences of the word or number {} : ".format(word))
            print(ck)        

            if not replay():
                break
    else:
        sys.exit()

    #The log file is created or appended here with the same message as in print.
    logging.info('This log was created at {}'.format(time.asctime()))
    logging.info(" 1 - Copy , 2 - Move , 3 - Delete, 4 - Data analysis , 5 - File renaming , 6 - Data Visualization")
    d = pd.DataFrame([folderdest,function,sort,word],labels2,[functiondetails])   #Here the dataframe is being formed
    logging.info(d)                                                                     #Dataframe is being logged here
    logging.info('This log ended at {}'.format(time.asctime()))         
        
        
elif function == 5:
    
    #The program is asking for the destination of the folder.
    folderdest = input("Enter folder destination: ")
    #C:\Users\msobe\Desktop\Newproject -----> sample folder address.
    try:
        #Using os.chdir() method to perform command line commands.
        os.chdir("{}".format(folderdest))
    except FileNotFoundError:
        print('Whoops! The file wasnt foundor its the wrong path.')
        sys.exit()
    
    os.system("dir >result.txt")
    #Here filepath variable is declared to help the computer read the new text file.
    filepath = '{}\\result.txt'.format(folderdest)
    filepath
    
    file = open(filepath)
    file.read()
    file.seek(0)
    
    #file content assigned to split1.
    split1 = file.read()
    #content of split one is split using .split() and turning into a list of seperated content of split1 or original file.
    list1 = split1.split()
    list1
    
    #Using for loops we are trying to make the program understand while files can be supported.
    #Rest of the content of the result.txt file is then ignored and not printed.
    for elements in list1:
        if elements[-3:] == 'txt':
            print(elements)
        elif elements[-4:] == 'pptx':
            print(elements)
        elif elements[-4:] == 'xlsx':
            print(elements)
        elif elements[-3:] == 'bmp':
            print(elements)
        elif elements[-3:] == 'PNG':
            print(elements)    
        elif elements[-4:] == 'jpeg':
            print(elements)
        elif elements[-3:] == 'rtf':
            print(elements)
        elif elements[-4:] == 'docx':
            print(elements)   
        elif elements[-4:] == 'pdf':
            print(elements)
        elif elements[-2:] == 'py':
            print(elements)
        elif elements[-1:] == 'c': 
            print(elements)    
        elif elements[-3:] == 'gif':
            print(elements)
        elif elements[-3:] == 'jpg':
            print(elements)    
        elif elements[-3:] == 'java':
            print(elements)

    print('\n')

    #Replay function for while loop further ahead in code is being created
    def replay():
        return input('Do you want to try again? Enter Yes or No: ').lower().startswith('y')
    condition = True
    #The program is asking the user for which file they want to rename.
    while condition:
        
        file1=input("Enter file you want to rename:")  #Remember to input the extension as well.
        file1
        if file1 != elements:
            break
        if not replay():
            break
        condition = False    

    
    #The program is asking the user for the new name of the chosen file.
    condition = True
    while condition:
        
        file2=input("what is the new name? ")  #Remember to input the extension as well.
        file2
        if not replay():
            break
        condition = False   
    #Using os.system , the program renames the file.
    os.system("ren {} {}".format(file1,file2))
    #The log file is created or appended here with the same message as in print.
    logging.info('This log was created at {}'.format(time.asctime()))
    logging.info(" 1 - Copy , 2 - Move , 3 - Delete, 4 - Data analysis , 5 - File renaming , 6 - Data Visualization")
    d = pd.DataFrame([folderdest,function,file1,file2],labels3,[functiondetails])   #Here the dataframe is being formed
    logging.info(d)                                                                     #Dataframe is being logged here
    logging.info('This log ended at {}'.format(time.asctime()))
    
elif function == 6:
    
    #The program is asking for input for location of file to be opened.
    filepath = input("Enter the excel file path along with the file you want to open : ")
    #C:\Arnav\Excel visualization\Visualizationsheet.xlsx
    
    #Replay function for while loop further ahead in code is being created.
    def replay():
    
        return input('Do you want to do it again? Enter Yes or No: ').lower().startswith('y')
    
    #The program is opening and displaying the excel file data and storing it as a dataframe.
    con = pd.read_excel('{}'.format(filepath))
    print(con)

    #Here the program is asking for input for the kind of graph the user wants based on the given options.
    while True:
        Type = input("What kind of graph do you want ? Bar?Line?Histogram?Boxplot?")
    
        if Type == "bar":
            con.iplot(kind = 'bar')
        if Type == "line":
            con.iplot(kind = 'line')
        if Type == "histogram":   
            con.iplot(kind = 'histogram')
        if Type == "box":
            con.iplot(kind = 'box')
        
        #The log file is created or appended here with the same message as in print.
        logging.info('This log was created at {}'.format(time.asctime()))
        logging.info(" 1 - Copy , 2 - Move , 3 - Delete, 4 - Data analysis , 5 - File renaming , 6 - Data Visualization")
        d = pd.DataFrame([filepath,function,Type],labels4,[functiondetails])   #Here the dataframe is being formed
        logging.info(d)                                                                     #Dataframe is being logged here
        logging.info('This log ended at {}'.format(time.asctime())) 
        
        if not replay():
            break
print("Thank you for using our program!")