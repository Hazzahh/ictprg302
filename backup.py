#1/usr/bin/python3
"""
Backup.py 
Harry Marlais
30013327@students.sunitafe.edu.au
Version 1.0
This Python code demonstrates on how it backup a file or directory to the command line.
While specifiying the jobs context in the backupcfg.py file.
While displaying errors on the screen, sending emails to the adminstrator, sending emails on errors and
written the process of success and failures in log file backup.log
"""
import sys
import os 
from backupcfg import jobs, destDir, smtp
from datetime import datetime
import pathlib
import shutil
import smtplib

def errorProcessing(errorMessage):
    """
    If there is an issue within the program this function 
    will send a error message to the screen, with date and time while also sending
    an email and writing to the log file. 
    """
    print("ERROR: " + errorMessage)
    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file = open("backups/logs.txt", "a")
    file.write("FAILURE "+ dateTimeStamp +" " +errorMessage + "\n")
    file.close()
    #open file and close file with message saying it failed
    sendEmail(errorMessage + dateTimeStamp)
    
def sendEmail(message):
    """
    This python code uses a smtp server in which it sends a alert
    to a google email account when a error occurred. 
    """

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")    
        
def main():
    """
    This Python code backups a file or directory from the command line.
    While specifiying the jobs context in the backupcfg.py file.
    While displaying errors on the screen, sending emails to the adminstrator, sending emails on errors and
    written the process of success and failures in log file backup.log
    """
    try:
        #Checks if job specifying in the command line
        if len(sys.argv) != 2:
            errorProcessing("Job name missing")
        else:
            jobname = sys.argv[1]
            
            #Checks if jobname is defined in the dictionary 
            if not jobname in jobs:
                errorProcessing("Job "+jobname+" Not Found In Dictionary ")
            else:
                
                #Check if source file exist
                source = jobs[jobname]
            
                if not os.path.exists(source):
                    errorProcessing("Source does not exist ")
                else: 
                    
                    #Check if destination exist
                    destPath = pathlib.PurePath(source)
                    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                    dest = destDir + "/" + destPath.name + "-" + dateTimeStamp 
                    if not os.path.exists(destDir):
                        errorProcessing("Destination does not exist ")
                    else: 
                        
                        #This copy directory
                        if pathlib.Path(source).is_dir():  
                            shutil.copytree(source, dest)
                        
                        #This copy file    
                        else:
                            shutil.copy2(source, dest)
                        
                        #This sends a success message in the logs 
                        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                        file = open("backups/logs.txt", "a")
                        file.write("SUCCESS "+ dateTimeStamp +" " +"Successfully backed up " + source + "\n")                   
                        file.close()
                        
    except:
        
        print("ERROR: Programmed failed")
    
if __name__ == "__main__":
    main()