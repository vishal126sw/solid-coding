# Interface Segregation Principle


from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def voice(self):
        pass

class Text(ABC):
    @abstractmethod
    def text_message(self):
        pass


class Camera(ABC):
    @abstractmethod
    def photo(self):
        pass


class BestMobilePhoneEver(Phone, Text, Camera):
    def voice(self):
        pass
    def text_message(self):
        pass

    def photo(self):
        pass

class OldSchoolMobilePhone(Phone, Text):
    def voice(self):
        pass
    def text_message(self):
        pass