import traceback

class ErrorHandler:
    def __init__(self, message=None, code=None):
        self.message = message
        self.code = code

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error = {
                    "error": True,
                    "message": str(e),
                    "code": self.code
                }
                
                if self.message:
                    error["message"] = f"{self.message}: {str(e)}"
    
                return error
        return wrapper
