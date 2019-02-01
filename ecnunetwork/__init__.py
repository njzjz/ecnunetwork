from __future__ import print_function, division, absolute_import, unicode_literals
try:
    input = raw_input
except NameError:
    pass

import json
import os
import requests


class ecnunetwork(object):
    def __init__(
            self, username=None, password=None, configfile=os.path.join(
                os.path.expanduser('~'),
                ".ecnunetwork")):
        self.username = username
        self.password = password
        self.configfile = configfile
        self.url = "https://login.ecnu.edu.cn/include/auth_action.php"
        self.flag = 0

    def connect(self):
        if self.username is None or self.password is None:
            self._readpassword()
        r = requests.post(
            self.url,
            data={"action": "login", "ajax": 1, "ac_id": 1,
                  "username": self.username, "password": self.password})
        print(r.text)
        if r.text.startswith("login_ok"):
            print("Successfully connected to the Internet.")
            if self.flag == 1:
                yorn = input("Save password? [Y/n] ")
                if yorn == "" or yorn == "Y" or yorn == "y" or yorn == "yes":
                    self._savepassword()
        else:
            yorn = input(
                "Fail to login. Maybe your id or password is wrong. Retry? [Y/n] ")
            self.flag = 2
            if yorn == "" or yorn == "Y" or yorn == "y" or yorn == "yes":
                self._username = None
                self._password = None
                self.connect()

    def _inputpassword(self):
        self.username = input("Please input your ECNU id: ")
        self.password = input("Please input your password: ")
        self.flag = 1

    def _readpassword(self):
        if not self.flag == 2:
            try:
                with open(self.configfile, 'r') as f:
                    config = json.load(f)
                    self.username = config['username']
                    self.password = config['password']
            except:
                pass
        if self.username is None or self.password is None:
            self._inputpassword()

    def _savepassword(self):
        config = {"username": self.username, "password": self.password}
        with open(self.configfile, 'w') as f:
            json.dump(config, f)


if __name__ == '__main__':
    ecnunetwork().connect()
