class Lancha:
    def __init__(self, motor):
        self.motor = motor



class veiculo :
    def suena_vocina ():
        print("Suena la vocina del veiculo")
    def arrancar ():
        print("el viculo da arranque")

class auto(veiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def abrir_capo(self):
        print("abro el capo del auto")
        pass




    
class movimientosEmbarcacion (Lancha):
    def virar_a_estribo (self):
        print("virto eb")

    def virar_a_babor(self):
        print("virto en bb")

class Lancha(veiculo,movimientosEmbarcacion):
    def __init__(self, motor):
        self.motor = motor
    def   