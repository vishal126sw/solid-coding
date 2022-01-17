#Open Closed Principle

from abc import ABC, abstractmethod

class Auth(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class Uploader(ABC):
    @abstractmethod
    def upload_file(self):
        pass

class AWS(Auth,Uploader):
    def authenticate(self):
        pass
    def upload_file(self,filename):
        pass
    

class Azure(Auth,Uploader):
    def authenticate(self):
        pass
    def upload_file(self,filename):
        pass
    
