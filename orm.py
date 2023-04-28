class Model:
    def __init__(self, *args, **kwargs): 
        # Get all class attributes aside inbuilt attributes
        attrs=[i for i in dir(self) if i[0]!='_']

        for attribute in attrs:
            print(attribute)
            self.__dict__[attribute]=getattr(self,attribute)

    #Make sure when setting fields the type matches the field
    def __setattr__(self, __name: str, __value) -> None:
        if(type(self.__dict__[__name]) is CharField):
            if(isinstance(__value,str)):
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


print(a.name.value)