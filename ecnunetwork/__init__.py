from __future__ import print_function, division, absolute_import, unicode_literals
from six.moves import input

import json
import os
import requests
import logging


class ecnunetwork:
    MESSAGE_OK = "Successfully connected to the Internet."
    MESSAGE_FAIL = "Fail to login. Maybe your id or password is wrong."
    MESSAGE_INPUT = {"username": "Please input your ECNU id: ",
                     "password": "Please input your password: "}
    MESSAGE_RETRY = "Retry? [Y/n] "
    MESSAGE_SAVE = "Save password? [Y/n] "

    def __init__(self, username=None, password=None, configfile=None):
        self._initconfig(username, password)
        self._readpassword()
        self.configfile = configfile or os.path.join(
            os.path.expanduser('~'), ".ecnunetwork")
        self.url = "https://login.ecnu.edu.cn/include/auth_action.php"

    def _initconfig(self, username=None, password=None):
        self.config = {"username": username, "password": password}

    def connect(self):
        self._inputpassword()
        r = requests.post(self.url, data={"action": "login", "ajax": 1, "ac_id": 1,
                                          "username": self.config["username"], "password": self.config["password"]})
        logging.debug(r.text)
        if r.text.startswith("login_ok"):
            logging.info(self.MESSAGE_OK)
            self._savepassword()
        else:
            logging.error(self.MESSAGE_FAIL)
            if self._checkyes(self.MESSAGE_RETRY):
                self._initconfig()
                self.connect()

    def _inputpassword(self):
        for ii in ["username", "password"]:
            if self.config[ii] is None:
                self.config[ii] = input(self.MESSAGE_INPUT[ii])

    def _readpassword(self):
        try:
            with open(self.configfile, 'r') as f:
                self._config = json.load(f)
                self.config = self._config
        except:
            self._config = None

    def _savepassword(self):
        if self.config != self._config and self._checkyes(self.MESSAGE_SAVE):
            with open(self.configfile, 'w') as f:
                json.dump(self.config, f)
            self._config = self.config

    @classmethod
    def _checkyes(cls, message):
        yorn = input(message)
        return yorn in ["", "Y", "y", "yes"]


if __name__ == '__main__':
    ecnunetwork().connect()
