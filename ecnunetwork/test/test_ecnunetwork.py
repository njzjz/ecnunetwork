import unittest
import ecnunetwork


class Testecnunetwork(unittest.TestCase):
    def test_loginok(self):
        def answerinput(inp):
            print(inp)
            return 'y'
        ecnunetwork.input = answerinput
        n = ecnunetwork.ecnunetwork(configfile='.testfile')
        n.url = 'https://php.njzjz.win/login_ok.php'
        n.connect()
