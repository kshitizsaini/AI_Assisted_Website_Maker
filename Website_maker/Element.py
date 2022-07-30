import re
class Element(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.orientation = None
        self.size = None
        self.elementColor = None
        self.padding = None
        self.tagList = []
    
    def setX(self, xCoord):
        self.x = xCoord

    def setY(self, YCoord):
        self.x = YCoord
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setOrient(self,orient):
        self.orientation = orient
    
    def getOrient(self,orient):
        return self.orientation
    
    def setSize(self,size):
        self.size = size
    
    def setColor(self,color):
        pattern = "[a-fA-f0-9]{6}"
        if re.match(pattern,color):
            color = "#" + color
            self.elementColor = color
        else:
            return 1
    
    def getColor(self):
        return self.elementColor
    
    def ElementToString(self):
        """Needs to be implemented"""
        return 0
    
    def addTag(self,tag):
        self.tagList.append(tag)
    
    
