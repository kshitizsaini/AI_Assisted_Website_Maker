import datetime
import re
from PIL import Image
from numpy import asarray
import Element
class Webpage:
    def __init__(self):
        self.webpageName = None
        self.webpageDate = datetime.datetime.now()
        self.webElementsList = []
        self.webpageImage = None
        self.backgroundColor = None
    
    def setWebpageName(self,name):
        self.webpageName = name
    
    def getWebpageName(self):
        return self.webpageName
    
    def setWebpageDate(self):
        self.webpageDate = datetime.datetime.now()
    
    def getWebpageDate(self):
        return self.webpageDate
    
    def addWebpageElement(self,element):
        self.webElementsList.append(element)
    
    def removeWebpageElement(self,element):
        self.webElementsList.remove(element)
    
    def setBackgroundColor(self,colorhex):
        pattern = "[a-fA-f0-9]{6}"
        if re.match(pattern,colorhex):
            color = "#" + colorhex
            self.backgroundColor = color
        else:
            return 1
    
    def webpageToString(self):
        """Needs to be implemented"""
        return 0
        
    def stringToElement(self):
        """Needs to be implemented"""
        return 0
    
    def setImage(self, Image):
        self.webpageImage = Image
    
    def getImage(self, Image):
        return self.webpageImage

    def uploadImage(self, image):
        """image --- is path to the image... can change depending on if its local or on server but the code should remain the same"""
        im = Image.open(image)
        data = asarray(image)
        self.setImage(data)
    
        