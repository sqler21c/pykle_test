'''
Created on 2012. 6. 18.

@author: KIM SUN GHU
CM Server State Information

#cs ===============================================================================================================================================

    
    Connect :      http://192.168.7.2:4330/condata?id=UML295_67806c06-2c9b-435e-8650-febe215ce711&action=connect
    Disconnect :  http://192.168.7.2:4330/condata?id=UML295_67806c06-2c9b-435e-8650-febe215ce711&actoin=disconnect
    
    <id>UML295_67806c06-2c9b-435e-8650-febe215ce711</id>
    
    Hotme
    
    
#ce ===============================================================================================================================================

'''
import wx
import const
import httplib
import xml.dom.minidom
import wx.xrc.XmlNode
import mainUI


def GetSRVConnState(self,testtype=const.TEST_TYPE_CONDIS):
    try:
        conHTTP = httplib.HTTPConnection(const.SERVER_URL)
        conHTTP.request("GET", testtype)
        consource = conHTTP.getresponse()
    except httplib.HTTPException :
        return consource.reason
             
    readsource = consource.read()
        #self.dom2 = self.SelectDOM(self.readsource,testtype=const.TEST_TYPE_CONDIS)
        
    return readsource
def XmlDOM(self,testtype=const.TEST_TYPE_CONDIS):

    pass
    
def GetsrvID(self, testtype):
    pass
def ActionSRV(self,strURL):
    pass
    
def SrvURL(self):
    pass
    
def SrvStateChng(self,strSRVState):
    pass
    
def SelectDOM(self,httpsoruce,testtype=const.TEST_TYPE_CONDIS):
     #   datasource = xml.dom.minidom.parseString(httpsoruce)
    pass

   
def ConnectionHTTP(self, testtype=const.TEST_TYPE_CONDIS):
    try:
        conHTTP = httplib.HTTPConnection(const.SERVER_URL)
        conHTTP.request("GET",testtype)
        consource = conHTTP.getresponse()
    except httplib.HTTPException :
        pass