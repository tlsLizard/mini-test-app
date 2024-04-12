"""
**mini-test-app**
**Version**
**1**

mini-test-app-v1
      |____________MiniTestApp.py
"""
import sys
import logging
try:
    import mini-test-app_tools
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)


class MiniTestApp:
    """
    Args
    app_under_test (default = 'hello.py')
    app_under_test_main_command (default = ('python3', 'hello.py'))

    Methods
    run()
       runs the command to launch the app under test using subprocess
       kills it after a timeout
       logs test info, the stdout and stderr of the app under test
        into log file (default= testapp_yourApp.log)
        returns test status (True, False)    
    """
    def __init__(self,
                 tag="test_app",
                 app_under_test="hello.py",
                 app_under_test_main_command=('python3', 'hello.py'),  # adjust here 
                 timeout_s=10,
                 local_logger=None
                 ) -> None:
        self.tag = tag
        self.app_under_test = app_under_test
        self.app_under_test_main_command = list(app_under_test_main_command)
        #  print("info: ")
        #  print(self.tag, self.app_under_test_main_command)
        self.timeout_s = timeout_s
        self.logger = local_logger
        self.duration = 0
        self.status = False
        if logger:
            logger.info("TestApp instance created")

    @mini-test-app_tools.calculate_duration
    def run(self):
        import os
        import signal
        import subprocess
        import sys

        cmd = ['python3', 'hello.py']  # the external command to run
        # TODO test ['py', 'hello.py']
        # TODO test cmd = self.app_under_test_main_command

        try:
            p = subprocess.Popen(
                                cmd,
                                start_new_session=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE
                                )
            stdout, stderr = p.communicate(timeout=self.timeout_s)
            stdout_str = stdout.decode('utf-8')
            stderr_str = stderr.decode('utf-8')

            # Check if the command was successful
            if p.returncode == 0:
                logger.info("command executed successfully!")
                self.status = True
            else:
                logger.error("error occurred during command execution")
            logger.info(f"Standard Output of app under test:\n{stdout_str}")
            logger.info(f"Error Output of app under test:\n{stderr_str}")
        except subprocess.TimeoutExpired:
            logger.warning(f'Timeout for {cmd} ({self.timeout_s}s) expired')
            logger.info('Terminating the whole process group...')
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
        return self.status


if __name__ == "__main__":

    print("Welcome to minitest-app!")
    command = ['python3', 'hello.py']  # Define a valid command to run hello.py
    #  todo: test other commands = ['py','hello.py'], ...

    #  tells user what testapp is about to do and offers to abort
    command_tag = command[0] + " " + command[1]
    while True:
        user_answer = input(f"testapp is about to run : >{command_tag}"
                            + '\n'
                            + 'do you want to continue? y/n  _'
                            )
        if user_answer.lower() == 'n':
            sys.exit(0)
        elif user_answer.lower() == 'y':
            break
        else:
            print("please enter a valid answer")

    # Configure test tools
    logger = test_tools.setup_logger('report_test_app_hello.log', logging.INFO)
    logger.info("logger configured")

    test = MiniTestApp(
                   tag='mini-test-app-v1 : testing hello.py',
                   app_under_test='hello.py',
                   app_under_test_main_command=('python3', 'hello.py'),
                   local_logger=logger
                   )

    (duration, status) = test.run()

    if status:
        logging.info("TestApp hello.py OK")
    else:
        logging.error("TestApp hello.py NOK")
    logging.info(f"test duration: {test.duration}")

    print("check log file for more details")
    print("bye")
    del test
