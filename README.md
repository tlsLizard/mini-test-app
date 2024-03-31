+**mini-test-app**
**Version**
**1**

      o
     oeo
    oeçoe
   oeoçoeo
  oeoççoeoe


# overview

File                  Function                                
-------------------------------------------------------------------
TestApp.py            run this to test your scripts / apps    
test_tools.py         tools to run your tests                 
test_app.log                                                     
      hello.py.py     a sample project                        
      main.py         the script/app you want to test         
      {ressources}    and its ressources
--------------------------------------------------------------------

# features

you can create a mini test environment with a simple folder:

place the script you want to test and its ressources directly in the folder

run TestApp.py to test your script 

what TesatApp does

- runs your script using python module 'subprocess'
- captures the Standard output and Standard error  of the app under test
- You can set a timeout after which this process is ended (default = 10s)
- TestApp creates a log file : test_app_myApp.log

# Sample output of TestApp for hello.py
![Alt text]([URL_to_image](https://github.com/tlsLizard/mini-test-app/blob/main/test_app_hello_log_file.png) "test_app_hello.log")

# licence notes
i chose MIT for v1, mainly because of the strong disclaimer section

#github
https://github.com/tlsLizard
 
