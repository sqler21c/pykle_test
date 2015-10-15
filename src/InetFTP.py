#-*- coding: cp949-*-
'''
Created on 2012. 7. 4.

@author: user
'''
import ftplib
import wx

class InetFTP():
    
    '''
    classdocs
    ftp의 지정된 폴더의 파일 donwnload
    '''


    def __init__(self,srvurl):
        '''
        Constructor
        '''
        self.oFtp = ftplib.FTP()
        
        try:
            self.oFtp.connect(srvurl)
        except ftplib.all_errors  :
            wx.MessageBox("CM server or FTP Server Check")
            self.oFtp.close()  
        
    def __del__(self):
        self.oFtp.close()
        
    def SetDir(self, srvdir):
        self.srvans = self.oFtp.cwd(srvdir)
        if self.srvans[:3] != "220":
            wx.MessageBox(self.srvans)
            return False
        if self.srvans[:3] == "220" : return True
        
    def SetLogin(self,usrid,usrpass):
        self.srvans = self.oFtp.login(usrid, usrpass)
        if self.srvans[:3] != "230":
            wx.MessageBox("Not login, Check User ID/Password")
            return False
        if self.srvans[:3] == "230": return True
        
    def GetDirList(self):
        return self.oFtp.nlst()
    
    def ChangeDir(self,chgdir):
        self.srvans = self.oFtp.cwd(chgdir)
        if self.srvans[:3] != "250":
            wx.MessageBox("Check Test Direcotry")
            return False
        if self.srvans[:3] == "250": return True
        
    def GetSrvFileSzie(self,filename):
        self.fielsize = self.oFtp.size(filename)
        return self.filesize
    
    def GetTestFileName(self):
        self.filelist = self.GetDirList()
        i = 0
        for self.filetype in self.filelist:
            if self.filetype[:4] == "test":
                self.filename[i] = self.filetype
                i=i + 1
            else:
                wx.MessageBox("File don't download.... File check")
                return False
        return self.filename
    
    def GetSrvFile(self,filename):
        self.oFtp.retrbinary("RETR " + filename, open("tmp.tmp","wb").write)
        return True
                
                
            
            