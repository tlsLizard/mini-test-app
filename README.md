+**mini-test-app**
**Version**
**1**

      o
     oeo
    oeçoe
   oeoçoeo
  oeoççoeoe
     |||

# overview

mini-test-app   __run this to test your new scripts
│              /                                              
├── TestAppp.py     
├── hello.py                <--- a sample project
├── main.py                   \         
├── requirements.txt           |----Your project
│ └── { Project Resources }   /
│
└── logs                        \_____  your log files
├── test_app_hello.log           |
└── ...

# features
with mini-testapp
you can create a mini test environment with a simple folder:
place the script you want to test and its ressources directly in the folder

run TestApp.py to test your script 

features:
TestApp runs your script using python module 'subprocess'
TestApp captures the Standard output and Standard error  of the app under test
You can set a timeout after which this process is ended (default = 10s)
TestApp created a log file : test_app_myApp.log'

#WIP picture of sample output (test_app_hello.log)

# licence notes
#WIP

#github
https://github.com/tlsLizard
 
