#1/usr/bin/python3

import sys
from backupcfg import jobs 

def errorProcessing(errorMessage):
    print("ERROR: " + errorMessage)
    
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
                errorProcessing("Job not found in dictionary")
            else:
                print(jobs)
    except:
        print("ERROR: Programmed failed")
    
if __name__ == "__main__":
    main()