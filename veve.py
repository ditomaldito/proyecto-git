class vehiculos():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False


    def arrancar(self):

        self.en_marcha = True

    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):

        print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nen marcha: ", self.en_marcha,
              "\nacelerando: ",self.acelera,"\nfrenando: ", self.frena)




class furgoneta(vehiculos):

    def carga(self, cargar):

        self.cargado = cargar

        if(self.cargado):
            return "la furgoneta:........esta cargada..........."
        else:
            return "la furgoneta no esta cargada"






class moto(vehiculos):

    hcaballito = ""

    def caballito(self):

        self.hcaballito = "voy haciendo el caballito"

    def estado(self):

        print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nen marcha: ", self.en_marcha,
              "\nacelerando: ",self.acelera,"\nfrenando: ", self.frena, "\n", self.caballito)






class vehiculos_electricos():

    def __init__(self):

        self.autonomia = 100

    def cargar_energia(self):

        self.cargando = True




mi_moto = moto("honda" , "hfhf")

mi_moto.caballito()

mi_moto.estado()

mi_furgoneta = furgoneta("renault" , "kangooooo")

mi_furgoneta.arrancar()

mi_furgoneta.estado()

print(mi_furgoneta.carga(True))






class bicicleta_electrica(vehiculos_electricos,vehiculos):

    pass

mi_bici = bicicleta_electrica



