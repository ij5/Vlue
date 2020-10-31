import atexit
import bottle as bot


@bot.route("/index/<name>")
def index(name):
    return bot.template("<h1>Hello {{name}}!</h1>", name=name)

class Loc():
    def __init__(self):
        self.location = "/"
        self.temp = ""
        self.___variable = {}

    def template(self, t, *args):
        self.temp = t
        for arg in args:
            self.___variable[arg] = arg

    def apply(self):
        @bot.route(self.location)
        def ___index():
            return bot.template(self.temp, )

class Web():
    def __init__(self):
        self.port = 8000
        self.host = 'localhost'

    def start(self):
        bot.run(host=self.port, port=self.port)



def onexit():
    pass

atexit.register(onexit)