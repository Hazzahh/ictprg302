#1/usr/bin/python3

jobs = {"job1" : "/home/ec2-user/environment/ictprg302/work/file1.txt",
        "job2" : "/home/ec2-user/environment/ictprg302/work/dir1",
        "job3" : "/home/ec2-user/environment/ictprg302/work/missing.txt",
        "job4" : "/home/ec2-user/environment/ictprg302/work/invalid.txt"
}

destDir = "/home/ec2-user/environment/ictprg302/backups"

smtp = {"sender": "30013327@students.sunitafe.edu.au",
        "recipient": "marlgamiing@gmail.com",
        "server": "smtp.gmail.com",
        "port": 587,
        "user": "marlgamiing@gmail.com", # need to specify a gmail email address with an app password setup
        "password": "pnojpvbghjobtigy"}   # need a gmail app password     