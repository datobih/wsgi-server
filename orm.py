class Model():
    id=None
    def __init__(self, *args, **kwargs): 
        # Get all class attributes aside inbuilt attributes
        attrs=[i for i in dir(self) if i[0]!='_']
        for attribute in attrs:
            # Ignore overriden getattribute in this class
            self.__dict__[attribute]=object.__getattribute__(self,attribute)
            
            

    #Return Field value instead of object reference
    def __getattribute__(self, __name: str,**kwargs):
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

    def all(self):
        # Get table name using model name 
        name=get_plural(type(self).__name__)
        query=f'SELECT * FROM {name}'
        print(query)

            
class Field():
    def __init__(self,**kwargs):
        
        if('value' in kwargs):
            self.value=kwargs['value']
    
    

class CharField(Field):  
    value=''
    

class IntField(Field):  
    value=0


class Person(Model):
    name=CharField(value='ds')


def create_database(model):
    #Get table name using model name
    name=get_plural(model.__name__)
    query=f'''CREATE TABLE IF NOT EXISTS {name}(
        id INTEGER PRIMARY KEY,
        '''
    for attribute in model.__dict__:
        if attribute[0]!='_':
            field=object.__getattribute__(model,attribute)
            if(isinstance(field,CharField)):
                query+=f'{attribute} TEXT,'
                
    query+=')'
    print(query)

def get_plural(name):
    name=name.lower()
    if(not name.endswith('s')):
        name+='s'
    return name


# create_database(Person)
Person().all()