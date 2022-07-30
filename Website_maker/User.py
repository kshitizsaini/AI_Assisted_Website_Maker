import re
from random import seed
from random import randint
import string
import Website
class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.email = None
        self.userId = None
        self.ProjectList = []
        self.currentlyWorkingWebsite = None

    def addToProjectList(self, website):
        self.ProjectList.append(website)

    def removeFromProjectList(self, website):
        self.ProjectList.remove(website)
    
    def setUsername(self, name):
        self.username = name
    
    def getUsername(self):
        return self.username

    def setPassword(self,password):
        self.password = password
    
    def getPassword(self):
        return self.password
    
    def setEmail(self, email):
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" # Email Validation
        if re.match(pattern, email):
            self.email = email
            return 0
        else:
            return 1
    
    def getEmail(self):
        return self.email
    
    def setUserId(self, globalCount):
        self.userId = globalCount + 1
        globalCount = globalCount + 1
        """
        seed(1)
        value = randint(0,1000000)
        self.userId = int(value)
        """
    
    def getUserId(self):
        return self.userId
    
    def fetchProject(self,projectName):
        for x in self.ProjectList:
            if x.websiteName == projectName:
                websiteString = self.getWebsiteString(projectName)
                website = self.stringToWebsite(websiteString)
                self.currentlyWorkingWebsite = website
            else:
                return 0


    def getWebsiteString(self, websiteName):
        """Needs to be implemented"""
        return 0
    def stringToWebsite(self, StringifiedWebsite):
        """Needs to be implemented"""
        return 0 
