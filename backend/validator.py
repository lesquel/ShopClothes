from abc import abstractmethod
# @abstractclass
class Validator:
    @abstractmethod
    def validate_type(object:any,type:any, message:str):
        if not isinstance(object,type):
            raise ValueError(message)
        return object