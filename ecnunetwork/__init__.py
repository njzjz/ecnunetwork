import json
import os
import requests
class ecnunetwork(object):
    def __init__(self,username=None,password=None,configfile=os.environ["HOME"]+"/.ecnunetwork"):
        self.username=username
        self.password=password
        self.configfile=configfile
        self.url="https://login.ecnu.edu.cn/include/auth_action.php"
        self.flag=0

    def connect(self):
        if self.username==None or self.password==None:
            self.readpassword()
        r=requests.post(self.url,data={"action":"login","ajax":1,"ac_id":1,"username":self.username,"password":self.password})
        if r.text.startswith("login_ok"):
            print("Successfully connected to the Internet.")
            if self.flag==1:
                yorn=input("Save password? [Y/n] ")
                if yorn=="" or yorn=="Y" or yorn=="y" or yorn=="yes":
                    self.savepassword()
        else:
            yorn=input("Fail to login. Maybe your id or password is wrong. Retry? [Y/n] ")
            self.flag=2
            if yorn=="" or yorn=="Y" or yorn=="y" or yorn=="yes":
                self.username=None
                self.password=None
                self.connect()

    def inputpassword(self):
        self.username=input("Please input your ECNU id: ")
        self.password=input("Please input your password: ")
        self.flag=1

    def readpassword(self):
        if not self.flag==2:
            try:
                with open(self.configfile, 'r') as f:
                    config = json.load(f)
                    self.username=config['username']
                    self.password=config['password']
            except:
                pass
        if self.username==None or self.password==None:
            self.inputpassword()

    def savepassword(self):
        config={"username":self.username,"password":self.password}
        with open(self.configfile, 'w') as f:
            json.dump(config, f)

if __name__=='__main__':
    ecnunetwork().connect()
