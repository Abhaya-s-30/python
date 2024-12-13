class BaseLogger:
    def log(self, message):
        print(f"Info: {message}")
class ErrorLogger(BaseLogger):
    def log(self, message):
        try:
            if "error" in message.lower():
                raise ValueError("An error occurred while logging.")
            else:
                print(f"Error: {message}")
        except Exception as e:
            print(f"ErrorLogger Exception: {str(e)}")
            print(f"Error message could not be logged: {message}")
base_logger = BaseLogger()
error_logger = ErrorLogger()
base_logger.log("This is a general log.")
error_logger.log("This is an error log.")
error_logger.log("This is an error message that causes an exception error.")
