from tkinter import *
from tkinter import ttk

class conversor:
    __ventana=None
    __peso=None
    __dolares=None
    
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry('300x200')
        
        self.__dolares=DoubleVar()
        self.__peso=DoubleVar()
        
        self.__dolares.trace('w',self.calcular)
        ttk.Entry(self.__ventana,textvariable=self.__dolares).place(x=120,y=30,width=50)
        ttk.Label(self.__ventana,text='Dolares').place(x=190,y=30)
        
        ttk.Label(self.__ventana,text="Es equivalente a: ").place(x=10,y=70)
        ttk.Label(self.__ventana,textvariable=self.__peso).place(x=120,y=70)
        ttk.Label(self.__ventana,text='Pesos').place(x=190,y=70)
        
        
        ttk.Button(self.__ventana,text="Salir",command=self.__ventana.destroy).place(x=210,y=170)
        
        self.__ventana.mainloop()
    def calcular(self,*args):

        valor=float(self.__dolares.get())
        self.__peso.set(valor*257.330)

def testapp():
    app=conversor()
    
if __name__=='__main__':
    testapp()