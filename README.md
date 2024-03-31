+**mini-test-app**
**Version**
**1**
      o
     oeo
    oeçoe
   oeoçoeo
  
# requirements
Python 3.8+

# features

- you can create a mini test environment with a simple folder:

- place the script you want to test and its ressources directly in the folder

- run TestApp.py to test your script 

# what TesatApp does

- runs your script using python module 'subprocess'
- captures the Standard output and Standard error  of the app under test
- You can set a timeout after which this process is ended (default = 10s)
- TestApp creates a log file : test_app_myApp.log

# details

Here's a brief overview of the key files and their functions in this project.

## files and Their Functions

### `TestApp.py`
- **Run this to test your scripts/apps** 

### `test_tools.py`
- **Tools to run your tests** 

### `test_app.log`
- **Log file for capturing test outputs** 

### `hello.py`
- ** A sample project**

### `{Resources}`
- **for the script under test's ressources, including assets, data files, etc.** 

# Sample output of TestApp for hello.py
![test_app_hello.log](https://github.com/tlsLizard/mini-test-app/blob/main/test_app_hello_log_file.png "test_app_hello.log")

# licence notes
I chose MIT for v1, mainly because of the strong disclaimer section

#github
https://github.com/tlsLizard
 
