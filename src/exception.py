import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Gets traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get filename where error occurred
    error_message = "Error occurred in Python script: [{0}], Line Number: [{1}], Error Message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message  # Return the formatted error message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Corrected the super() call
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Generate detailed error message

    def __str__(self):
        return self.error_message  # Print the detailed error when exception is raised

# Example Usage:
