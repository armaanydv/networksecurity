import sys
import networksecurity.logging.logger as logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.errors_message = error_message
        _, _, exc_tb = error_details.exc_info()

        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_no = exc_tb.tb_lineno

    def __str__(self):
        return f"Error occurred in script: [{self.file_name}] at line number: [{self.line_no}] with error message: [{self.errors_message}]"
    


  