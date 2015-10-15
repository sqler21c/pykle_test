#-*- coding: cp949-*-
#Boa:Frame:MainWindow

import os  # 'posix', 'nt', 'os2', 'ce', 'java', 'riscos'.
import wx
import wx.richtext
from wx.lib.anchors import LayoutAnchors
import wx.lib.buttons
import const
import httplib
import time
import webbrowser
from ftplib import FTP
import urllib
import socket
#import xml.dom.minidom
from xml.etree.ElementTree import ElementTree, XML, ParseError
from HTMLParser import HTMLParser
import InetFTP
import random


##from wx.xrc.XmlNode import myXMLDOM



def create(parent):
    return MainWindow(parent)
[wxID_MAINWINDOW, wxID_MAINWINDOWBUTTON1, wxID_MAINWINDOWBUTTON2, 
 wxID_MAINWINDOWBUTTON3, wxID_MAINWINDOWCONCOUNTER, wxID_MAINWINDOWCONDIS, 
 wxID_MAINWINDOWLOGVIEW, wxID_MAINWINDOWPHONENUMBER, wxID_MAINWINDOWSMSCASE1, 
 wxID_MAINWINDOWSMSCASE2, wxID_MAINWINDOWSMSCASE3, wxID_MAINWINDOWSMSCASE4, 
 wxID_MAINWINDOWSMSCOUNTER, wxID_MAINWINDOWSMSTEST, wxID_MAINWINDOWSTATICBOX1, 
 wxID_MAINWINDOWSTATICBOX2, wxID_MAINWINDOWSTATICBOX3, 
 wxID_MAINWINDOWSTATICBOX4, wxID_MAINWINDOWSTATICBOX5, 
 wxID_MAINWINDOWSTATICTEXT1, wxID_MAINWINDOWSTATICTEXT10, 
 wxID_MAINWINDOWSTATICTEXT11, wxID_MAINWINDOWSTATICTEXT2, 
 wxID_MAINWINDOWSTATICTEXT3, wxID_MAINWINDOWSTATICTEXT4, 
 wxID_MAINWINDOWSTATICTEXT5, wxID_MAINWINDOWSTATICTEXT6, 
 wxID_MAINWINDOWSTATICTEXT7, wxID_MAINWINDOWSTATICTEXT8, 
 wxID_MAINWINDOWSTATICTEXT9, wxID_MAINWINDOWTEXTCTRL1, 
 wxID_MAINWINDOWTEXTCTRL2, wxID_MAINWINDOWTEXTCTRL3, wxID_MAINWINDOWTEXTCTRL4, 
 wxID_MAINWINDOWTEXTCTRL5, wxID_MAINWINDOWTEXTCTRL6, wxID_MAINWINDOWTEXTCTRL7, 
 wxID_MAINWINDOWTEXTCTRL8, wxID_MAINWINDOWTOOLCLOSE, 
] = [wx.NewId() for _init_ctrls in range(39)]


class MainWindow(wx.Frame,InetFTP.InetFTP):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINWINDOW, name=u'MainWindow',
              parent=prnt, pos=wx.Point(63, 191), size=wx.Size(1297, 581),
              style=wx.RAISED_BORDER | wx.FRAME_TOOL_WINDOW | wx.DEFAULT_FRAME_STYLE,
              title=u'Sparkle Stability tool V')
        self.SetClientSize(wx.Size(1289, 554))
        self.Bind(wx.EVT_CLOSE, self.OnMainWindowClose)

        self.staticText1 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT1,
              label=u'Connect/Disconnect  Test : Loop counter',
              name='staticText1', parent=self, pos=wx.Point(200, 16),
              size=wx.Size(230, 14), style=0)

        self.conCounter = wx.TextCtrl(id=wxID_MAINWINDOWCONCOUNTER,
              name=u'conCounter', parent=self, pos=wx.Point(456, 8),
              size=wx.Size(58, 22), style=0, value=u'10')
        self.conCounter.SetToolTipString(u'\ubc18\ubcf5\ud69f\uc218')
        self.conCounter.SetMaxLength(100000)
        self.conCounter.SetCursor(wx.STANDARD_CURSOR)
        self.conCounter.SetHelpText(u'')
        self.conCounter.SetConstraints(LayoutAnchors(self.conCounter, True,
              True, False, False))

        self.ConDis = wx.Button(id=wxID_MAINWINDOWCONDIS, label=u'TEST START',
              name=u'ConDis', parent=self, pos=wx.Point(528, 8),
              size=wx.Size(88, 24), style=0)
        self.ConDis.Bind(wx.EVT_BUTTON, self.OnConDisButton,
              id=wxID_MAINWINDOWCONDIS)

        self.ToolClose = wx.lib.buttons.GenButton(id=wxID_MAINWINDOWTOOLCLOSE,
              label=u'Tool Close', name=u'ToolClose', parent=self,
              pos=wx.Point(8, 512), size=wx.Size(616, 26), style=0)
        self.ToolClose.Bind(wx.EVT_BUTTON, self.OnToolCloseButton,
              id=wxID_MAINWINDOWTOOLCLOSE)

        self.staticBox1 = wx.StaticBox(id=wxID_MAINWINDOWSTATICBOX1,
              label=u'SMS TEST Cases', name='staticBox1', parent=self,
              pos=wx.Point(8, 48), size=wx.Size(616, 80), style=0)

        self.smsCounter = wx.TextCtrl(id=wxID_MAINWINDOWSMSCOUNTER,
              name=u'smsCounter', parent=self, pos=wx.Point(456, 80),
              size=wx.Size(57, 22), style=0, value=u'10')
        self.smsCounter.SetToolTipString(u'\ubc18\ubcf5\ud69f\uc218')
        self.smsCounter.SetMaxLength(100000)

        self.smsTest = wx.Button(id=wxID_MAINWINDOWSMSTEST, label=u'SMS TEST',
              name=u'smsTest', parent=self, pos=wx.Point(528, 80),
              size=wx.Size(83, 24), style=0)
        self.smsTest.Bind(wx.EVT_BUTTON, self.OnSmsTestButton,
              id=wxID_MAINWINDOWSMSTEST)

        self.SMSCase1 = wx.CheckBox(id=wxID_MAINWINDOWSMSCASE1,
              label='Disconnect_160byte', name='chkSMSCase1', parent=self,
              pos=wx.Point(26, 86), size=wx.Size(152, 14), style=0)

        self.SMSCase2 = wx.CheckBox(id=wxID_MAINWINDOWSMSCASE2,
              label='Disconnect_0-160byte', name=u'SMSCase2', parent=self,
              pos=wx.Point(25, 107), size=wx.Size(152, 14), style=0)

        self.SMSCase3 = wx.CheckBox(id=wxID_MAINWINDOWSMSCASE3,
              label='Connect_160byte', name=u'SMSCase3', parent=self,
              pos=wx.Point(206, 88), size=wx.Size(144, 14), style=0)

        self.SMSCase4 = wx.CheckBox(id=wxID_MAINWINDOWSMSCASE4,
              label='Disconnect_0-160byte', name=u'SMSCase4', parent=self,
              pos=wx.Point(206, 106), size=wx.Size(152, 14), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_MAINWINDOWSTATICBOX2,
              label=u'FTP TEST', name='staticBox2', parent=self, pos=wx.Point(8,
              137), size=wx.Size(616, 113), style=0)

        self.staticText2 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT2,
              label=u'Server Name', name='staticText2', parent=self,
              pos=wx.Point(24, 154), size=wx.Size(88, 14), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_MAINWINDOWTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(120, 154),
              size=wx.Size(288, 22), style=0, value=u'ftp.pantechwireless.com')

        self.textCtrl2 = wx.TextCtrl(id=wxID_MAINWINDOWTEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(456, 177),
              size=wx.Size(68, 22), style=0, value=u'10')
        self.textCtrl2.SetToolTipString(u'\ubc18\ubcf5\ud69f\uc218')
        self.textCtrl2.SetMaxLength(100000)

        self.staticText3 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT3,
              label=u'Test Directory', name='staticText3', parent=self,
              pos=wx.Point(22, 185), size=wx.Size(78, 14), style=0)

        self.textCtrl3 = wx.TextCtrl(id=wxID_MAINWINDOWTEXTCTRL3,
              name='textCtrl3', parent=self, pos=wx.Point(122, 184),
              size=wx.Size(100, 22), style=0, value=u'RAY_QE')

        self.staticText4 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT4,
              label=u'ID', name='staticText4', parent=self, pos=wx.Point(29,
              217), size=wx.Size(12, 14), style=0)

        self.textCtrl4 = wx.TextCtrl(id=wxID_MAINWINDOWTEXTCTRL4,
              name='textCtrl4', parent=self, pos=wx.Point(123, 217),
              size=wx.Size(197, 22), style=0,
              value=u'sun.kwangsoo@pantech.com')

        self.staticText5 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT5,
              label=u'Passwrod', name='staticText5', parent=self,
              pos=wx.Point(330, 221), size=wx.Size(51, 14), style=0)

        self.textCtrl5 = wx.TextCtrl(id=wxID_MAINWINDOWTEXTCTRL5,
              name='textCtrl5', parent=self, pos=wx.Point(389, 216),
              size=wx.Size(100, 22), style=0, value=u'test123')

        self.button1 = wx.Button(id=wxID_MAINWINDOWBUTTON1, label=u'FTP TEST',
              name='button1', parent=self, pos=wx.Point(536, 161),
              size=wx.Size(75, 72), style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_MAINWINDOWSTATICBOX3,
              label=u'WEB Surffing TEST', name='staticBox3', parent=self,
              pos=wx.Point(8, 258), size=wx.Size(616, 70), style=0)

        self.staticText6 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT6,
              label=u'TEST URL', name='staticText6', parent=self,
              pos=wx.Point(24, 284), size=wx.Size(55, 14), style=0)

        self.textCtrl6 = wx.TextCtrl(id=wxID_MAINWINDOWTEXTCTRL6,
              name='textCtrl6', parent=self, pos=wx.Point(93, 282),
              size=wx.Size(288, 22), style=0, value='textCtrl6')

        self.staticBox4 = wx.StaticBox(id=wxID_MAINWINDOWSTATICBOX4,
              label=u'TOTAL TEST', name='staticBox4', parent=self,
              pos=wx.Point(8, 336), size=wx.Size(616, 64), style=0)

        self.staticBox5 = wx.StaticBox(id=wxID_MAINWINDOWSTATICBOX5,
              label=u'SETT TEST', name='staticBox5', parent=self,
              pos=wx.Point(8, 408), size=wx.Size(616, 88), style=0)

        self.button2 = wx.Button(id=wxID_MAINWINDOWBUTTON2, label=u'WEB TEST',
              name='button2', parent=self, pos=wx.Point(536, 288),
              size=wx.Size(75, 24), style=0)

        self.button3 = wx.Button(id=wxID_MAINWINDOWBUTTON3, label=u'TEST',
              name='button3', parent=self, pos=wx.Point(536, 360),
              size=wx.Size(75, 24), style=0)

        self.staticText7 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT7,
              label=u'\uc5f0\uad6c\uc18c \ud68c\uc2e0 \ub300\uae30\uc911',
              name='staticText7', parent=self, pos=wx.Point(248, 448),
              size=wx.Size(104, 14), style=0)

        self.LogView = wx.TextCtrl(id=wxID_MAINWINDOWLOGVIEW, name=u'LogView',
              parent=self, pos=wx.Point(640, 8), size=wx.Size(640, 536),
              style=wx.TE_MULTILINE | wx.HSCROLL | wx.VSCROLL | wx.TE_READONLY,
              value=u'')
        self.LogView.SetToolTipString(u'LogView')

        self.staticText8 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT8,
              label=u'Input MIN', name='staticText8', parent=self,
              pos=wx.Point(399, 287), size=wx.Size(55, 14), style=0)

        self.textCtrl7 = wx.TextCtrl(id=wxID_MAINWINDOWTEXTCTRL7,
              name='textCtrl7', parent=self, pos=wx.Point(464, 288),
              size=wx.Size(60, 22), style=0, value='textCtrl7')
        self.textCtrl7.SetMaxLength(100000)

        self.staticText9 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT9,
              label=u'Loop counter', name='staticText9', parent=self,
              pos=wx.Point(370, 184), size=wx.Size(74, 14), style=0)

        self.textCtrl8 = wx.TextCtrl(id=wxID_MAINWINDOWTEXTCTRL8,
              name='textCtrl8', parent=self, pos=wx.Point(424, 360),
              size=wx.Size(100, 22), style=0, value='textCtrl8')

        self.staticText10 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT10,
              label='staticText10', name='staticText10', parent=self,
              pos=wx.Point(342, 365), size=wx.Size(69, 16), style=0)

        self.staticText11 = wx.StaticText(id=wxID_MAINWINDOWSTATICTEXT11,
              label=u'Phone Number : ', name='staticText11', parent=self,
              pos=wx.Point(33, 67), size=wx.Size(94, 14), style=0)

        self.PhoneNumber = wx.TextCtrl(id=wxID_MAINWINDOWPHONENUMBER,
              name=u'PhoneNumber', parent=self, pos=wx.Point(128, 61),
              size=wx.Size(240, 24), style=0, value=u'01038250940')

    def __init__(self, parent):
        self._init_ctrls(parent)

        self.srtprelog = self.SetPreLog()
        try:
            self.oFile = open(self.srtprelog+".log", "a")
        except IOError:
            wx.MessageBox("cannot file open")
            return False
        
        
    def OnConDisLeftUp(self, event):
        event.Skip()
        pass
    
    def OnMainWindowClose(self, event):
        event.Skip()
        pass
    
    def OnToolCloseButton(self, event):
        self.Destroy()
        event.Skip()

    def OnConDisButton(self, event):
        self.WriteLog("Connect Disconnect : Start ")
    
        n = 1
        counter = self.conCounter.GetValue()
        
 
        while n <= int(counter):
            self.srvstate = self.GetSRVConnState()
            
            if self.srvstate == const.SRV_STATE_IDLE:
                self.vbool = self.SrvStateChange(self.srvstate)
                if not self.vbool : 
                    self.WriteLog("server state change  : fail")
                    return False
            elif self.srvstate == const.SRV_STATE_CONNECTED or self.srvstate == const.SRV_STATE_DORMANT :
                self.vbool = self.SrvStateChange(self.srvstate)
                if not self.vbool : 
                    self.WriteLog("server state change  : fail")
                    return False
            elif self.srvstate == const.SRV_STATE_INACTIVE:
                self.WriteLog("Server state :  %s device Check" %self.srvstate)
                return False
            elif self.srvstate == const.SRV_STATE_SEARCHING:
                self.WriteLog("Server state :  %s device Check" %self.srvstate)
                return False
            elif self.srvstate == const.SRV_STATE_UNAVAILABLE:
                self.WriteLog("Server state :  %s device Check" %self.srvstate)
                return False
            elif self.srvstate == const.SRV_STATE_UPDATING:
                self.WriteLog("Server state :  %s device Check" %self.srvstate)
                return False
            
            self.WriteLog("Connedt Disconnect ::::  " + str(n))
            n = n +1
        self.WriteLog("Connect Disconnect : End")
        return True
    
    
    def WriteLog(self,logString):
        self.prelog = self.SetPreLog()
        self.setlogstring = self.prelog + logString + "\n"
        self.LogView.AppendText(self.setlogstring)
                    
        try:
            self.oFile.write(self.setlogstring)
        except IOError:
            return False
        
        return True
            
    def SetPreLog(self):
        self.tempTime = time.localtime(time.time())
        self.prelog = "%d%d%d%d%d%d  " %(self.tempTime.tm_year,self.tempTime.tm_mon,self.tempTime.tm_mday,self.tempTime.tm_hour,self.tempTime.tm_min,self.tempTime.tm_sec)
        return self.prelog 
    
    
    def __del__(self):
        self.oFile.close()
        self.conHTTP.close()
        pass
    
    def GetSRVConnState(self, testtype=const.TEST_TYPE_CONDIS):
        self.WriteLog("GetSRVConnState ----- Start ")
###       
#        try:
#            self.conHTTP = httplib.HTTPConnection(const.SERVER_URL)
#            self.conHTTP.request("GET", testtype)
#            self.consource = self.conHTTP.getresponse()
#        except httplib.socket.timeout:
#            self.WriteLog("GetSRVConnState server timeout error : Server Check")
#            return False
#        except httplib.CannotSendRequest:
#            self.WriteLog("GetSRVconnStae Request Error : cannot connect server")
#            return Fasle
###
        consource = urllib.urlopen(const.SERVER_URL+testtype)
        readsource = consource.read()
        domtree = ElementTree(XML(readsource))
        domtree.getroot()
        srvstate = domtree.findtext("p-answer/condata/state/value")
        srvstatedes = domtree.findtext("p-answer/condata/state/description")
        netsrvingName = domtree.findtext("p-answer/condata/network/serving/name")
        netsrvingType = domtree.findtext("p-answer/condata/network/serving/type")
        netsrvingID = domtree.findtext("p-answer/condata/network/serving/id")
        netsrvingServer = domtree.findtext("p-answer/condata/network/serving/server")
        netsrvingServertype = domtree.findtext("p-answer/condata/network/serving/servertype")
        netsrvingEncruption = domtree.findtext("p-answer/condata/network/serving/encryption")
        netroamType = domtree.findtext("p-answer/condata/network/serving/roam/type")
        netroamIndicator  = domtree.findtext("p-answer/condata/network/serving/roam/indicator")
        netroamIndicatordescription = domtree.findtext("p-answer/condata/network/serving/roam/indicatordescription")
        netroamRoaminglistversion = domtree.findtext("p-answer/condata/network/serving/roam/roaminglistversion")
        netHomeType = domtree.findtext("p-answer/condata/network/home/type")
        netHomeID = domtree.findtext("p-answer/condata/network/home/id")
        Actionsss = domtree.findtext("p-answer/condata/actions")
        connectionAddrIPV4IP = domtree.findtext("p-answer/condata/connection/address/ipv4/ip")
        connectionAddrIPV4SUB = domtree.findtext("p-answer/condata/connection/address/ipv4/subnet")
        connectionAddrIPV4GWY = domtree.findtext("p-answer/condata/connection/address/ipv4/gateway")
        connectionAddrIPV4DNS = domtree.findtext("p-answer/condata/connection/address/ipv4/dns")
        connectionAddrIPV6IP = domtree.findtext("p-answer/condata/connection/address/ipv6/ip")
        connectionAddrIPV6SUB = domtree.findtext("p-answer/condata/connection/address/ipv6/subnet")
        connectionAddrIPV6GWY = domtree.findtext("p-answer/condata/connection/address/ipv6/gateway")
        connectionAddrIPV6DNS = domtree.findtext("p-answer/condata/connection/address/ipv6/dns")
        self.WriteLog(const.STR_SHAP)
        self.WriteLog("Server State : " + srvstate)        
        self.WriteLog("Description : "+ srvstatedes)
        self.WriteLog("+++++++++++++++++++++++++++++++++++++++++")
        self.WriteLog("Network Serving Nmae : " + netsrvingName)
        self.WriteLog("Network Serving Type : " + netsrvingType)
        self.WriteLog("Network Serving ID : " + netsrvingID)
        self.WriteLog("Network Serving Server : " + netsrvingServer)
        self.WriteLog("Netwrok Serving Server Type : " + netsrvingServertype)
        self.WriteLog("Network Serving Encryption : " + netsrvingEncruption)
        self.WriteLog("+++++++++++++++++++++++++++++++++++++++++")
        self.WriteLog("Network Serving Roam Type : " + str(netroamType))
        self.WriteLog("Network Serving Roam Indicator : " + str(netroamIndicator))
        self.WriteLog("Network Serving Roam Indicator Description : " + str(netroamIndicatordescription))
        self.WriteLog("Network Serving Roam Indicator Description : " + str(netroamRoaminglistversion))
        self.WriteLog("Network Serving Home Type : " + str(netHomeType))
        self.WriteLog("Network Serving Home ID : " + str(netHomeID))
        self.WriteLog("+++++++++++++++++++++++++++++++++++++++++")
        self.WriteLog("Network Actions : " + Actionsss)
        self.WriteLog("+++++++++++++++++++++++++++++++++++++++++")
        self.WriteLog("Network Connection IP4 IP : " + str(connectionAddrIPV4IP))
        self.WriteLog("Network Connection IP4 Subnet : " + str(connectionAddrIPV4SUB))
        self.WriteLog("Network connection IP4 Gateway : " + str(connectionAddrIPV4GWY))
        self.WriteLog("Network Connection IP4 DNS : " + str(connectionAddrIPV4DNS))
        self.WriteLog("+++++++++++++++++++++++++++++++++++++++++")
        self.WriteLog("Network Connection IP6 IP : " + str(connectionAddrIPV6IP))
        self.WriteLog("Network Connection IP6 Subnet : " + str(connectionAddrIPV6SUB))
        self.WriteLog("Network connection IP6 Gateway : " + str(connectionAddrIPV6GWY))
        self.WriteLog("Network Connection IP6 DNS : " + str(connectionAddrIPV6DNS))
        self.WriteLog(const.STR_SHAP)
        consource.close()
        self.WriteLog("GetSRVConnState ----- END ")
        return srvstate
    
    def GetSrvID(self,testtype=const.TEST_TYPE_CONDIS):
        self.WriteLog("GetSrvID ----- Start ")

        self.consource = urllib.urlopen(const.SERVER_URL+testtype)
        self.readsource = self.consource.read()
        self.WriteLog(self.readsource)
        self.domtree = ElementTree(XML(self.readsource))
        self.domtree.getroot()
        self.emel = self.domtree.findtext("p-answer/id")
        self.WriteLog(const.STR_SHAP)
        self.WriteLog("Server ID : " + self.emel)
        self.WriteLog(const.STR_SHAP)
        self.consource.close()
        self.WriteLog("GetSrvID ----- END ")
        return self.emel
    
    def ActSrvURL(self,actiontype,testtype=const.TEST_TYPE_CONDIS, phnumber="",smsbody=""):
        self.WriteLog("ActSrvURL ----- Start ")
        srvid = self.GetSrvID()
        wx.MessageBox(testtype) 
        if testtype == const.TEST_TYPE_CONDIS:
            srvAction =  const.SERVER_URL + const.TEST_TYPE_CONDIS + "?id=%s&action=%s" %(srvid,actiontype)
        elif testtype == const.TEST_TYPE_MSG:
            #end url : 192.168.7.2:4330/messaging?action=send& amp;serviceid=0&to=&body=message body
            srvAction = const.SERVER_URL + const.TEST_TYPE_MSG + "?action="+ actiontype +"&servvice=0&to"+ phnumber + "&body=" + smsbody
        
        self.WriteLog(const.STR_SHAP)
        self.WriteLog("Action URL : " + srvAction)
        self.WriteLog(const.STR_SHAP)
        self.WriteLog("ActSrvURL ----- END ")
        return srvAction

    def SrvStateChange(self,srvState):
        self.WriteLog("SrvStateChange ----- Start ")
                
        if const.SRV_STATE_IDLE == srvState:
            ActURL = self.ActSrvURL(const.CONDATA_ACT_CONNECT)
        elif const.SRV_STATE_CONNECTED == srvState:
            ActURL = self.ActSrvURL(const.CONDATA_ACT_DISCONNECT)
        
        self.WriteLog("SRv STATE change server url :: " + ActURL)     
        consource = urllib.urlopen(ActURL)
        srvstate = self.GetSRVConnState()
        time.sleep(1)        
        
        while True:
            if (const.SRV_STATE_IDLE == srvstate) or (const.SRV_STATE_CONNECTED == srvstate):
                self.WriteLog("SrvStateChange ----- END ")
                self.consource.close()
                return True
            else:
                self.WriteLog("Server State Checking ::: %s" %srvstate)
                time.sleep(1)        
                self.srvstate = self.GetSRVConnState()
        
            
    
    def SrvCHK(self, server=const.SERVER_URL,page=const.TEST_TYPE_CONDIS):
        self.WriteLog("SrvCHK ----- START ")
        
        while True:
            try:
                self.conHTTP.connect()
            except httplib.HTTPException, socket.error :
                self.WriteLog("%s Error Check the device PLZ" %server)
                self.WriteLog("SrvCHK ----- Fail ")
                self.conHTTP.close()
                return False
        
        self.WriteLog("SrvCHK ----- END:: True ")
        self.conHTTP.close()
        return True

   
    def ConnectionHTTP(self, testtype=const.TEST_TYPE_CONDIS):
        
        try:
            conHTTP = httplib.HTTPConnection(const.SERVER_URL)
            conHTTP.request("GET",testtype)
            consource = conHTTP.getresponse()
        except httplib.HTTPException :
                pass     

    def OnConCounterKeyDown(self, event):
        pass
    
    def FindAtag(self, url):
        pass

    def OnSmsTestButton(self, event):
        srvState = self.GetSRVConnState()
        counter = int(self.smsCounter.GetValue())
        fone =  self.PhoneNumber.GetValue()
        ii = 1
        for ii in counter :
            if self.SMSCase1.GetValue() or self.SMSCase2.GetValue() :
                if srvState == const.SRV_STATE_CONNECTED:
                    self.SrvStateChange(srvState)
                
                
                
                
                
                if self.SMSCase1.GetValue() :   #if Checkbox is  checking return the True
                    self.GetSMSBody(const.SMS_BODY_TYPTE_MAX)
                if self.SMSCase2.GetValue():
                    self.GetSMSBody(const.SMS_BODY_TYPE_1TO160)
        
            self.SendSMS()
        
    def GetSMSBody(self,smstype=const.SMS_BODY_TYPTE_MAX):
        
        items = '''`1234567890-=\~!@#$%^&*()_+|QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?qwertyuiop[]asdfghjkl;'zxcvbnm,./'''
        smsbody =""
        if smstype == const.SMS_BODY_TYPTE_MAX:
            counter = 1 
            for counter in const.SMS_MAX: 
                smsbody = smsbody + random.choice(items)
            return smsbody
        elif smstype == const.SMS_BODY_TYPE_1TO160 :
            bodylen = random.randint(1, 160)
            counter = 1
            for counter in bodylen:
                smsbody = smsbody + random.choice(items)
            return random.choice(items)
            
    def SendSMS(self,smsbody,fone):
        smsurl = self.ActSrvURL("send", const.TEST_TYPE_MSG, fone, smsbody)
        smssend = self.ActionSrv(smsurl)
        
    
    def ActionSrv(self,srvurl):
        consource = urllib.urlopen(srvurl)
        srvstate = self.GetSRVConnState()
        time.sleep(1)        

    def GetEngData(self):
        self.WriteLog("Get engdata ----- Start ")
        consource = urllib.urlopen(const.SERVER_URL + const.TEST_TYPE_ENGDATA)
        readsource = consource.read()
        domtree = ElementTree(XML(readsource))
        domtree.getroot()
        mobileip = domtree.findtext("p-answer/engdata/settings/mobile_ip")
        access_overload_class = domtree.findtext("p-answer/engdata/settings/access_overload_class")
        preferred_operating_mode=domtree.findtext("p-answer/engdata/settings/preferred_operating_mode")
        slot_cycle_index = domtree.findtext("p-answer/engdata/field_test/slot_cycle_index")
        current_nam = domtree.findtext("p-answer/engdata/field_test/current_nam")
        auto_nam = domtree.findtext("p-answer/engdata/field_test/auto_nam")
        spc_change_enabled = domtree.findtext("p-answer/engdata/field_test/spc_change_enabled")
        directory_number = domtree.findtext("p-answer/engdata/field_test/directory_number")
        access_overload_class1 = domtree.findtext("p-answer/engdata/field_test/access_overload_class")
        mcc = domtree.findtext("p-answer/engdata/field_test/mcc")
        mnc  = domtree.findtext("p-answer/engdata/field_test/mnc")
        channel_primary_a = domtree.findtext("p-answer/engdata/field_test/channel_primary_a")
        channel_primary_b = domtree.findtext("p-answer/engdata/field_test/channel_primary_b")
        channel_secondary_a = domtree.findtext("p-answer/engdata/field_test/channel_secondary_a")
        channel_secondary_b = domtree.findtext("p-answer/engdata/field_test/channel_secondary_b")
        home_sid_table = domtree.findtext("p-answer/engdata/field_test/home_sid_table")
        terminated_reg_home_sid = domtree.findtext("p-answer/engdata/field_test/terminated_reg_home_sid")
        terminated_reg_foreign_sid = domtree.findtext("p-answer/engdata/field_test/terminated_reg_foreign_sid")
        terminated_reg_foreign_nid = domtree.findtext("p-answer/engdata/field_test/terminated_reg_foreign_nid")
        system_preffered_mode = domtree.findtext("p-answer/engdata/field_test/system_preffered_mode")
        prl_version_number = domtree.findtext("p-answer/engdata/field_test/prl_version_number")
        dns_primary = domtree.findtext("p-answer/engdata/field_test/dns_primary")
        dns_secondary = domtree.findtext("p-answer/engdata/field_test/dns_secondary")
        packet_dial_string = domtree.findtext("p-answer/engdata/field_test/packet_dial_string")
        mdr_mode = domtree.findtext("p-answer/engdata/field_test/mdr_mode")
        data_scrm = domtree.findtext("p-answer/engdata/field_test/data_scrm")
        mip_ha_spi_value = domtree.findtext("p-answer/engdata/field_test/mip_ha_spi_value")
        mip_reverse_tunneling = domtree.findtext("p-answer/engdata/field_test/mip_reverse_tunneling")
        mip_home = domtree.findtext("p-answer/engdata/field_test/mip_home")
        mip_primary_ha_address = domtree.findtext("p-answer/engdata/field_test/mip_primary_ha_address")
        mip_secondary_ha_address = domtree.findtext("p-answer/engdata/field_test/mip_secondary_ha_address")
        mip_behavior = domtree.findtext("p-answer/engdata/field_test/mip_behavior")
        mip_pre_registration_timeout = domtree.findtext("p-answer/engdata/field_test/mip_pre_registration_timeout")
        mip_registration_retries = domtree.findtext("p-answer/engdata/field_test/mip_registration_retries")
       #dmu_key_exchange_indicator 
        nid = domtree.findtext("p-answer/engdata/field_test/nid")
        fer = domtree.findtext("p-answer/engdata/field_test/fer")
        rssi = domtree.findtext("p-answer/engdata/field_test/rssi")
        #ec_io 
        channel = domtree.findtext("p-answer/engdata/field_test/channel") 
        latitude = domtree.findtext("p-answer/engdata/field_test/latitude")
        longitude = domtree.findtext("p-answer/engdata/field_test/longitude")
        #<tx_power /> 
        #<rx_power /> 
        band_class = domtree.findtext("p-answer/engdata/field_test/band_class")
        p_rev = domtree.findtext("p-answer/engdata/field_test/p_rev")
        packet_zone_id = domtree.findtext("p-answer/engdata/field_test/packet_zone_id")
        #last_call_error /> 
        #<service_option_in_use /> 
        #<call_state /> 
        dormant_state = domtree.findtext("p-answer/engdata/field_test/dormant_state")
        #<mac_index /> 
        subnet_mask = domtree.findtext("p-answer/engdata/field_test/subnet_mask")
        color_code = domtree.findtext("p-answer/engdata/field_test/color_code")
        uati024 = domtree.findtext("p-answer/engdata/field_test/uati024")
        #finger_info_pn_offsets /> 
      #<finger_info_walsh_codes /> 
      #<finger_info_rssi /> 
      #<active_set_pn_offsets /> 
      #<active_set_ec_io_dbm /> 
      #<active_set_channel /> 
      #<neighbor_set_pn_offsets /> 
      #<neighbor_set_ec_io_dbm /> 
      #<neighbor_set_channel /> 
      #<candidate_set_pn_offsets /> 
      #<candidate_set_ec_io_dbm /> 
      #<candidate_set_channel /> 

        
        self.WriteLog(const.STR_SHAP)
        self.WriteLog("mobile IP : " + mobileip)        
        self.WriteLog("access_overload_class : "+ access_overload_class)
        self.WriteLog("preferred_operating_mode : "+ preferred_operating_mode)
        self.WriteLog("slot_cycle_index : " + slot_cycle_index)
        self.WriteLog("current_nam : " + current_nam)
        self.WriteLog("auto_nam : " + auto_nam)
        self.WriteLog("spc_change_enabled : " + spc_change_enabled)
        self.WriteLog("directory_number : " + directory_number)
        self.WriteLog("access_overload_class : " + access_overload_class1)
        self.WriteLog("mcc : " + str(mcc))
        self.WriteLog("mnc : " + str(mnc))
        self.WriteLog("channel_primary_a : " + str(channel_primary_a))
        self.WriteLog("channel_primary_b : " + str(channel_primary_b))
        self.WriteLog("channel_secondary_a : " + str(channel_secondary_a))
        self.WriteLog("channel_secondary_b : " + channel_secondary_b)
        self.WriteLog("home_sid_table : " + str(home_sid_table))
        self.WriteLog("terminated_reg_home_sid> : " + str(terminated_reg_home_sid))
        self.WriteLog("terminated_reg_foreign_sid : " + str(terminated_reg_foreign_sid))
        self.WriteLog("terminated_reg_foreign_nid : " + str(terminated_reg_foreign_nid))
        self.WriteLog("system_preffered_mode : " + str(system_preffered_mode))
        self.WriteLog("prl_version_number : " + str(prl_version_number))
        self.WriteLog("dns_primary : " + str(dns_primary))
        self.WriteLog("dns_secondary : " + str(dns_secondary))
        self.WriteLog("packet_dial_string : " + str(packet_dial_string))
        self.WriteLog("mdr_mode : " + str(mdr_mode))
        self.WriteLog("data_scrm : " + str(data_scrm))
        self.WriteLog("mip_ha_spi_value : " + str(mip_ha_spi_value))
        self.WriteLog("mip_reverse_tunneling : " + str(mip_reverse_tunneling))
        self.WriteLog("mip_home : " + str(mip_home))
        self.WriteLog("mip_primary_ha_address : " + str(mip_primary_ha_address))
        self.WriteLog("mip_secondary_ha_address : " + str(mip_secondary_ha_address))
        self.WriteLog("mip_behavior : " + str(mip_behavior))
        self.WriteLog("mip_pre_registration_timeout : " + str(mip_pre_registration_timeout))
        self.WriteLog("mip_registration_retries : " + str(mip_registration_retries))
        self.WriteLog("nid : " + str(nid))
        self.WriteLog("fer : " + str(fer))
        self.WriteLog("rssi : " + str(rssi))
        self.WriteLog("channel : " + str(channel))
        self.WriteLog("latitude : " + str(latitude))
        self.WriteLog("longitude : " + str(longitude))
        self.WriteLog("band_class : " + str(band_class))
        self.WriteLog("p_rev : " + str(p_rev))
        self.WriteLog("packet_zone_id : " + str(packet_zone_id))
        self.WriteLog("dormant_state : " + str(dormant_state))
        self.WriteLog("subnet_mask : " + str(subnet_mask))
        self.WriteLog("color_code : " + str(color_code))
        self.WriteLog("uati024 : " + str(uati024))
        self.WriteLog(const.STR_SHAP)
        consource.close()
        self.WriteLog("Get engdata  ----- End ")
        
    def GetGPSData(self):
        self.WriteLog("Get gps Data ----- Start ")
        consource = urllib.urlopen(const.SERVER_URL + const.TEST_TYPE_GPS)
        readsource = consource.read()
        domtree = ElementTree(XML(readsource))
        domtree.getroot()
        value = domtree.findtext("p-answer/gps/state/value")
        description = domtree.findtext("p-answer/gps/state/percentage")
        
        self.WriteLog(const.STR_SHAP)
        self.WriteLog("value : " + value)        
        self.WriteLog("description: "+ description)
       
        self.WriteLog(const.STR_SHAP)
        consource.close()
        self.WriteLog("Get gps Data  ----- End ")
        