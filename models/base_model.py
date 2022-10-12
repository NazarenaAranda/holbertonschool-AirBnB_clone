#!/usr/bin/python3
from uuid import uuid4 """uuid genera identificadores unicos,
uuid4 genera un UUID aleatorio, el cual como dije anteriormente
va a ser unico"""
from datetime import datetime """libreria para manejar fechas, incorpora tipos
de datos date, time y datetiime para representar fechas y
funciones para manejarlas"""


class BaseModel():
    """class BaseModel"""
   def __init__(self, *args, **kwargs):
       """Initialize attributes"""
       if len(kwargs) == 0:
           self.id = str(uuid4()) """id convertido a string"""
           self.created_at = datetime.now() """fecha actual cuando se crea una instancia"""
           self.updete_at = datetime.now() """fecha actualizada cada vez que se cambia el objeto"""
       else:
           for key in kwargs:
               if key is not "_clas_":
                   setattr(self, key, kwargs[key])

    def _str_(self):
        """string with information about the model"""
        return (f"[{self._class.name}] ({self.id}) {self.dict_}")

    def save(self):
        """updating the updated_at attribute with the current date"""
        self.updated_at = datetime.now

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dicc = {}



