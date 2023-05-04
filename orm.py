class Model():
    id=None
    def __init__(self, *args, **kwargs): 
        # Get all class attributes aside inbuilt attributes
        attrs=[i for i in dir(self) if i[0]!='_']
        for attribute in attrs:
            # Ignore overriden getattribute in this class

            self.__dict__[attribute]=object.__getattribute__(self,attribute)
        
        # Add all model fields into the ModelObject attributes
        self.__dict__['objects']=ModelObject(model_name=type(self).__name__,**(self.__dict__))
            
            

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



class ModelObject:
    def __init__(self,**kwargs) -> None:
        for key in kwargs:
            self.__dict__[key]=kwargs[key]
        
        self.__dict__['objects']=[]
        print(self.__dict__)

    def all(self):
        if(len(self.objects)==0):
            name=get_plural(self.model_name)
            query=f'SELECT * FROM {name}'



        else:
            return self.objects

        
            
class Field():
    def __init__(self,**kwargs):
        
        if('value' in kwargs):
            print(kwargs)
            self.value=kwargs['value']
        else:
            print(self.value)
    
    

class CharField(Field):  
    value=''
    

class IntField(Field):  
    value=0


class Person(Model):
    name=CharField()


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
person=Person(name='David')
print(person.objects.model_name)
