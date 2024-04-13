+**mini-test-app**
**Version**
**1**
  
# requirements
Python 3.8+

# features

- you can create a mini test environment with a simple folder:

- place the script you want to test and its ressources directly in the folder

- run MiniTestApp.py to test your script 

creates a log file : test_app_myApp.log

# what MiniTestApp does

- runs your script/python app using python module 'subprocess'
- captures the Standard output and Standard error  of the app/script under test
- You can set a timeout after which this process is ended (default = 10s)
- MiniTestApp creates a log file : report-test_app_myApp.log

## files and Their Functions
Here's a brief overview of the files and their functions in this project:

### `MiniTestApp.py`
- **Run this to test your scripts/apps** 

### `mini_test_app_tools.py`
- **Tools to run your tests** 

### `report_test_app_youApp.log`
- **Log file for capturing test outputs** 

### `hello.py`
- ** A sample project**

### `test_project.py`
pytest checking the environment

### CI
### `.github/workflows/python_app.yml`
automated test adapted from github actions' template for python app CI test
for each push to main, it builds a temporary environment with
latest ubuntu, python 3.10, 
updates pip
runs ```pip install -r requirements.txt``` if any
runs ```pytest test_project.py```
you can add more tests using the prefix test_ ,
or test under dirrefent environments by creating new .yml files

# Sample output of MiniTestApp for hello.py
![report_test_app_hello.log](https://github.com/tlsLizard/mini-test-app/blob/main/report_test_app_hello_log_file.png "report_test_app_hello.log")

# licence notes
#WIP
I chose MIT for v1, mainly because of the strong disclaimer section

#github
https://github.com/tlsLizard
 
