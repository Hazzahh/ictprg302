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
    This python code demonstrats that if there is an issue within the code it
    will send a error message. 
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
    This python code demonstrats on how it uses a smtp server in which it sends a alert
    to your google email account that a error occurred. 
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
    This Python code demonstrates on how it backup a file or directory to the command line.
    While specifiying the jobs context in the backupcfg.py file.
    While displaying errors on the screen, sending emails to the adminstrator, sending emails on errors and
    written the process of success and failures in log file backup.log
    """
    try:
        if len(sys.argv) != 2:
            errorProcessing("Job name missing")
        else:
            jobname = sys.argv[1]
            
            if not jobname in jobs:
                errorProcessing("Job "+jobname+" Not Found In Dictionary ")
            else:
                
                source = jobs[jobname]
            
                if not os.path.exists(source):
                    errorProcessing("Source does not exist ")
                else: 
                    
                    destPath = pathlib.PurePath(source)
                    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                    dest = destDir + "/" + destPath.name + "-" + dateTimeStamp 
                    if not os.path.exists(destDir):
                        errorProcessing("Destination does not exist ")
                    else: 
                        
                        if pathlib.Path(source).is_dir():  
                            shutil.copytree(source, dest)
                            
                        else:
                            shutil.copy2(source, dest)
                        
                        
                        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                        file = open("backups/logs.txt", "a")
                        file.write("SUCCESS "+ dateTimeStamp +" " +"Successfully backed up " + source + "\n")                   
                        file.close()
                        #open file and close file with message saying it succced
                        pass
    except:
        
        print("ERROR: Programmed failed")
    
if __name__ == "__main__":
    main()