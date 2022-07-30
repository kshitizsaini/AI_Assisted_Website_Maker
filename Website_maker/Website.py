import datetime
import Webpage
class Website:
    def __init__(self):
        self.websiteName = None
        self.websiteDate = datetime.datetime.now()
        self.WebpageList = []
        self.answers = []
        self.currentlyWorkingWebpage = None
    
    def websiteToString(self):
        """Needs to be implemented"""
        return 0
    
    def setWebsiteName(self, name):
        self.websiteName = name
    
    def getWebsiteName(self):
        return self.websiteName
    
    def setWebsiteDate(self):
        self.websiteDate = datetime.datetime.now()
    
    def getWebsiteDate(self):
        return self.websiteDate
    
    def addWebpage(self,webpage):
        self.WebpageList.append(webpage)
    
    def removeWebpage(self,webpage):
        self.WebpageList.remove(webpage)
    
    def addAnswer(self,Answer):
        self.answers.append(Answer)
    
    def removeAnswer(self, Answer):
        self.answers.remove(Answer)
    
    def stringToWebpage(self,webpageString):
        """Needs to be implemented"""
        return 0
    
    