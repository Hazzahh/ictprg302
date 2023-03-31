#1/usr/bin/python3

import sys
import os 
from backupcfg import jobs, destDir
from datetime import datetime
import pathlib
import shutil

def errorProcessing(errorMessage):
    print("ERROR: " + errorMessage)
    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file = open("backups/logs.txt", "a")
    file.write("FAILURE "+ dateTimeStamp +" " +errorMessage + "\n")
    file.close()
    #open file and close file with message saying it failed
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
                errorProcessing("Job Not Found In Dictionary")
            else:
                
                source = jobs[jobname]
            
                if not os.path.exists(source):
                    errorProcessing("Source does not exist")
                else: 
                    
                    destPath = pathlib.PurePath(source)
                    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                    dest = destDir + "/" + destPath.name + "-" + dateTimeStamp 
                    
                    if pathlib.Path(source).is_dir():  
                        shutil.copytree(source, dest)
                        
                    else:
                        shutil.copy2(source, dest)
                    
                    
                    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                    file = open("backups/logs.txt", "a")
                    file.write("SUCCESS "+ dateTimeStamp +" " +"Successfully backed up file" + "\n")                   
                    file.close()
                    #open file and close file with message saying it succced
                    pass
    except:
        
        print("ERROR: Programmed failed")
    
if __name__ == "__main__":
    main()