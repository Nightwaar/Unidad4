
from tkinter import *
from tkinter import ttk
from functools import partial
class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None
    __primerim=None
    __segundoim=None
    __resultado=None
    __resultadoim=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        self.__ventana.geometry('350x250')
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        self.__primerim=StringVar()
        self.__segundoim=StringVar()
        self.__resultado=StringVar()
        self.__resultadoim=StringVar()
        operatorEntry=ttk.Entry(self.__ventana, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.place(x=100,y=120)
        # ttk.Button(self.__ventana, text='1', command=partial(self.ponerNUMERO, '1')).place(x=50,y=20)
        # ttk.Button(self.__ventana, text='2', command=partial(self.ponerNUMERO,'2')).place(x=125,y=20)
        # ttk.Button(self.__ventana, text='3', command=partial(self.ponerNUMERO,'3')).place(x=200,y=20)
        # ttk.Button(self.__ventana, text='4', command=partial(self.ponerNUMERO,'4')).place(x=50,y=40)
        # ttk.Button(self.__ventana, text='5', command=partial(self.ponerNUMERO,'5')).place(x=125,y=40)
        # ttk.Button(self.__ventana, text='6', command=partial(self.ponerNUMERO,'6')).place(x=200,y=40)
        # ttk.Button(self.__ventana, text='7', command=partial(self.ponerNUMERO,'7')).place(x=50,y=60)
        # ttk.Button(self.__ventana, text='8', command=partial(self.ponerNUMERO,'8')).place(x=125,y=60)
        # ttk.Button(self.__ventana, text='9', command=partial(self.ponerNUMERO,'9')).place(x=200,y=60)
        # ttk.Button(self.__ventana, text='0', command=partial(self.ponerNUMERO, '0')).place(x=50,y=80)
        ttk.Button(self.__ventana, text='+', command=partial(self.ponerOPERADOR, '+')).place(x=125,y=20)
        ttk.Button(self.__ventana, text='-', command=partial(self.ponerOPERADOR, '-')).place(x=200,y=20)
        ttk.Button(self.__ventana, text='*', command=partial(self.ponerOPERADOR, '*')).place(x=50,y=20)
        ttk.Button(self.__ventana, text='/', command=partial(self.ponerOPERADOR, '/')).place(x=125,y=40)
        ttk.Button(self.__ventana, text='=', command=partial(self.ponerOPERADOR, '=')).place(x=200,y=40)
        ttk.Label(self.__ventana,text='A:').place(x=50,y=140)
        ttk.Label(self.__ventana,text='B:').place(x=50,y=180)
        ttk.Entry(self.__ventana,textvariable=self.__primerOperando).place(x=80,y=140,width=50)
        ttk.Label(self.__ventana,text='+').place(x=130,y=140)
        ttk.Entry(self.__ventana,textvariable=self.__primerim).place(x=150,y=140,width=50)
        ttk.Label(self.__ventana,text='i').place(x=200,y=140)
        ttk.Entry(self.__ventana,textvariable=self.__segundoOperando).place(x=80,y=180,width=50)
        ttk.Label(self.__ventana,text='+').place(x=130,y=180)
        ttk.Entry(self.__ventana,textvariable=self.__segundoim).place(x=150,y=180,width=50)
        ttk.Label(self.__ventana,text='i').place(x=200,y=180)
        
        ttk.Label(self.__ventana,textvariable='Hola',justify='right',state='disabled').place(x=100,y=220)
        self.__ventana.mainloop()
    # def ponerNUMERO(self, numero):
    #     if self.__operadorAux==None:
    #         valor = self.__panel.get()
    #         self.__panel.set(valor+numero)
    #     else:
    #         self.__operadorAux=None
    #         valor=self.__panel.get()
    #         self.__primerOperando=int(valor)
    #         self.__panel.set(numero)
    # def borrarPanel(self):
    #     self.__panel.set('0')
    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion=='-':
                resultado=operando1-operando2
            else:
                if operacion=='*':
                    resultado=operando1*operando2
                else:
                    if operacion=='/':
                        resultado=operando1/operando2
    def ponerOPERADOR(self, op):
        if op=='=':
            operacion=self.__operador.get()
            self.__segundoOperando=int(self.__panel.get())
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion=self.__operador.get()
                self.__segundoOperando=int(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux=op
    def enviarnumuno(self):
        return self.__primerOperando
    def enviarnumdos(self):
        return self.__segundoOperando
def main():
    calculadora=Calculadora()
    
if __name__=='__main__':
    main()



