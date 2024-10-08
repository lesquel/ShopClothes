from abc import ABC

class Validator(ABC):
    @staticmethod
    def validate_type(obj:any,type:any, message:str):
        if not isinstance(obj,type):
            print(type(obj))
            raise ValueError(message)
        return obj
    @staticmethod
    def validate_length(value, min_length, message):
        if len(value) < min_length:
            raise ValueError(message)
        return value
    
    @staticmethod
    def validate_type_list(listt:list,type:any, message:str):
        if not isinstance(listt,list):
            raise ValueError(message)
        for obj in listt:
            if not isinstance(obj,type):
                raise ValueError(message)
        return listt