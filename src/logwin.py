'''
Created on 2012. 6. 18.

@author: user
'''
import wx
import wx.richtext
import os
import sys
import time

def create(parent):
    return LogUI(parent)

[wxID_LOGUI, wxID_LOGUIRICHTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class LogUI(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_LOGUI, name=u'LogUI', parent=prnt,
              pos=wx.Point(792, 66), size=wx.Size(548, 628),
              style=wx.DIALOG_MODELESS | wx.TAB_TRAVERSAL | wx.DEFAULT_DIALOG_STYLE,
              title=u'LogView')
        self.SetClientSize(wx.Size(540, 601))

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_LOGUIRICHTEXTCTRL1,
              parent=self, pos=wx.Point(0, 0), size=wx.Size(536, 664),
              style=wx.richtext.RE_READONLY | wx.richtext.RE_MULTILINE,
              value='Log Test : \n')
                  
        

    def __init__(self, parent):
        self._init_ctrls(parent)
        tempTime = time.localtime(time.time())
        strFileName = "%d%d%d%d%d%d" %(tempTime.tm_year,tempTime.tm_mon,tempTime.tm_mday,tempTime.tm_hour,tempTime.tm_min,tempTime.tm_sec)
        try:
            self.oFile = open(strFileName+".log", "a")
        except IOError:
            wx.MessageBox("Cannot Open the file",wx.OK)
       
           
        
    def _writeLog(self,logString):
        tempTime = time.localtime(time.time())
        logstr = "(%d-%d-%d  %d:%d:%d)  " %(tempTime.tm_year,tempTime.tm_mon,tempTime.tm_mday,tempTime.tm_hour,tempTime.tm_min,tempTime.tm_sec)
        setlogstring = logstr + logString + "\n\r"
        self.richTextCtrl1.SetValue(setlogstring)
        
        try:
            self.oFile.write(setlogstring)
        except IOError:
            wx.MessageBox("Don't write in file")
            
    
    def __del__(self):
        self.oFile.close()