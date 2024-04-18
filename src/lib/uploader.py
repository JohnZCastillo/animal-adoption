from abc import ABC, abstractmethod

class Uploader(ABC):
    
    @abstractmethod
    def upload(file):
        pass
    