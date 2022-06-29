# metodo constructor
class cuenta:
    def __init__(self,numero,fecha,saldo):
        self.numero = numero
        self.fechaApertura = fecha
        self.saldo = saldo

# metodos set 

    def setNumero(self, numero):
        self.numero = numero
    def setSaldo(self, saldo):
        self.saldo = saldo

# metodos get 

    def getNumero(self):
        return self.numero
    def getFechaApertura(self):
        return self.fecha
    def getSaldo(self):
        return self.saldo
    
# metodos para retiro

    def retirar (self, retiro):
        if self.saldo >= retiro:
            self.saldo -= retiro
            print(' ::: Su Retiro Por Valor: $ {}. ::: Su Saldo Es: $ {}'.format(retiro, self.saldo))
        else:
            print(':::: Su Saldo Es Insuficiente ::::')
    def consignar (self, valor):
        self.saldo += valor
        print('Su nuevo saldo es {}'.format(self.saldo))
    def mostrarCuenta (self):
        print('Numero De Cuenta: {}'.format(self.numero))
        print('Fecha De Apertura: {}'.format(self.fechaApertura))
        print('Saldo $' + str(self.saldo))
        print('::::::::::::::::::::::::::::::::::')

# Programa Alterno

class CuentaCorriente(cuenta):
    def __init__(self, numero, fecha, saldo, numeroChequera):
        self.numero = numero
        self.fecha = fecha
        self.saldo = saldo
        self.numeroChequera = numeroChequera
    def NumeroChequera(self):
        return print(f' :::: Numero De Chequera Es : {self.numeroChequera}')
