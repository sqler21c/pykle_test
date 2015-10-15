#-*- coding: cp949-*-
'''
Created on 2012. 6. 18.

@author: user
'''
import wx
import thread
import time
import webbrowser
import const 
import mainUI

'''import logwin
'''

'''
import elementtree
        
'''

modules ={u'logwin': [0, '', u'logwin.py'], u'mainUI': [0, '', u'mainUI.py']}

class DataDeviceSTBTool(wx.App):
    def OnInit(self):
        omainUI = mainUI.create(None)
        omainUI.Show()
        self.SetTopWindow(omainUI) 
        return True


def main():
    app = DataDeviceSTBTool(0)
    app.MainLoop()
    pass

if __name__ == '__main__':
    main()
