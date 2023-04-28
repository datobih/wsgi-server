from typing import Any


class Model():
    def __init__(self, *args, **kwargs): 
        # Get all class attributes aside inbuilt attributes
        attrs=[i for i in dir(self) if i[0]!='_']
        for attribute in attrs:
            # Ignore overriden getattribute in this class
            self.__dict__[attribute]=object.__getattribute__(self,attribute)
            

    #Return Field value instead of object reference
    def __getattribute__(self, __name: str,**kwargs) -> Any:
        attr=object.__getattribute__(self,__name)
        if(isinstance(attr,Field)):
            return attr.value
        else:
            return attr


    #Make sure when setting fields the type matches the field
    def __setattr__(self, __name: str, __value) -> None:

        if(isinstance(self.__dict__[__name],Field)):
            #Set the value of field from object attribute dictionary
            self.__dict__[__name].value=__value
            

class Field():
    def __init__(self,**kwargs):
        
        if('value' in kwargs):
            self.value=kwargs['value']
    
    

class CharField(Field):  
    value=''
    

class IntField(Field):  
    value=0


class Person(Model):
    name=CharField()

    

    
    

    
    


    

a=Person()
a.name="DWW"
print(a.name)