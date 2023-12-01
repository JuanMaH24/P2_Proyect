import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from abc import ABC, abstractmethod

class ICrud (ABC) :
    @abstractmethod
    def create (self,**kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def read (self,**kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def buscar (self,**kwargs):
        raise NotImplementedError
    
    def update(self,**kwargs):
        raise NotImplementedError
    

    def delete (self,**kwargs):
        raise NotImplementedError
    