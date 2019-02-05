import ecnunetwork


class Testecnunetwork:
    def test_loginok(self, httpserver):
        httpserver.serve_content('login_ok,xxx')
        def answerinput(inp):
            print(inp)
            return 'y'
        ecnunetwork.input = answerinput
        n = ecnunetwork.ecnunetwork(configfile='.testfile')
        n.url = httpserver.url
        n.connect()
