"""
mini-test-app-v1
     |_____________mini-test-app_tools

tools:
   - a decorator
          |___ calculate_duration,
               -> gets the execution time of a function                             
   - some functions
          |___ setup_logger -> returns a logger object
          |___ 3 helper functions to format string, tags, etc      
          |      
          |___introducing TestTemplate class, unused for now
"""
import time

def calculate_duration(func):
    """ simple decorator
        Arg: a function
        Return: a tuple ( function output, duration_time)
        resource: time.time()"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        return result, duration
    return wrapper    


import logging

def setup_logger(log_file='report_test_app_hello.log', level=logging.DEBUG):
    """Args: log_file (default: test_app_hello.log)
             level should be in [logging.INFO, 
                                logging.WARNING,
                                logging.DEBUG)
        Return: logger object"""
    logger = logging.getLogger()
    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # adjust if needed
    
    # Add formatter to handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def format_raw_ms_tag(raw_tag):
    """
    :param string         ex:    raw_tag = '0.017794132232666016'
    :return: string       ex:    new_tag = '18ms'
    """
    milliseconds = float(raw_tag)
    seconds = milliseconds / 1000.0

    # Convert milliseconds to seconds and milliseconds
    minutes = int(seconds // 1000)
    remaining_seconds = seconds % 60

    # Construct the formatted tag string
    if minutes > 0:
        new_tag = f"{minutes} minutes, {remaining_seconds:.2f} seconds"
    else:
        new_tag = f"{remaining_seconds:.2f} seconds"

    return new_tag


def round_to_x_decimals(number, x):
    """Args: float, int
       Return: string
       example: 
       number = 0.017794132232666016
       x = 3
       output= str(0.018)"""
    rounded_number = round(float(number) * 10 ** x) / (10 ** x)
    return rounded_number


"""   unused for now, for later
class TestTemplate:
    def __init__(self, test_tag='myTest', status=False):
        self.tag = test_tag
        self.status = status

    def run(self):
        :return: test status
        #
        #   test instructions
        #
        if True: # if your test conditions for pass are met 
            self.status = True
        return self.status
"""


if __name__ == "__main__":

    # test your tools here
    print("Testing tools...")

    # test round_to_x_decimals
    duration_unit = 's'
    fake_duration_raw = float(0.017794132232666016)
    print("fake_duration_raw", fake_duration_raw, duration_unit)
    fake_duration = round_to_x_decimals(fake_duration_raw, 3)
    print("fake_duration", fake_duration, duration_unit)
    # test round_to_x_decimals ok
    


