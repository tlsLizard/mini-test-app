+**mini-test-app**
**Version**
**1**

      o
     oeo
    oeçoe
   oeoçoeo
  oeoççoeoe


# overview

| File                    | Function                                |
|-------------------------------------------------------------------|
| TestApp.py              | run this to test your scripts / apps    |
| test_tools.py           | tools to run your tests                 |
| test_app.log            |                                         |
|    hello.py.py          | a sample project                        |
|    main.py              | the script/app you want to test         |
|    {ressources}         |                                         |

# features

with mini-test-app
you can create a mini test environment with a simple folder:
place the script you want to test and its ressources directly in the folder

run TestApp.py to test your script 

what it does

- TestApp runs your script using python module 'subprocess'
- TestApp captures the Standard output and Standard error  of the app under test
- You can set a timeout after which this process is ended (default = 10s)
- TestApp creates a log file : test_app_myApp.log'

#WIP picture of sample output (test_app_hello.log)

# licence notes
i chose MIT for v1, mainly because of the strong disclaimer section

#github
https://github.com/tlsLizard
 
