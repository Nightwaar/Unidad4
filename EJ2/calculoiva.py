from tkinter import *
from tkinter import ttk

class calculariva():
    __ventana=None
    __preciobase=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry('500x500')
        self.__ventana.configure(bg='white')
        self.__ventana.title('Calculador de iva')
        iva1=int(21)
        iva2=float(10.5)
        
        opts = { 'ipadx': 500, 'ipady': 10}
        ttk.Label(self.__ventana,text='Calculo de IVA',background='gray').place(width=500,height=50)
        
        ttk.Label(self.__ventana,text='IVA 21%').place(x=150,y=150)
        ttk.Radiobutton(self.__ventana,textvariable=iva1).place(x=130,y=150)
        ttk.Label(self.__ventana,text='IVA 10.5%').place(x=150,y=180)
        ttk.Radiobutton(self.__ventana,textvariable=iva2).place(x=130,y=180)
        style = ttk.Style()
        style.configure("Red.TButton", background="red")
        ttk.Button(self.__ventana, text='Salir', style="Red.TButton", command=self.__ventana.destroy).place(x=400, y=425)
        style1 = ttk.Style()
        style1.configure("Green.TButton", background="green")
        ttk.Button(self.__ventana, text='Calcular', style="Green.TButton", command=self.calcular).place(x=200, y=425)
        
        ttk.Label(self.__ventana,text='Precio sin IVA').place(x=80,y=90)
        self.__preciobase=StringVar()
        self.preciobaseEntry=ttk.Entry(self.__ventana,textvariable=self.__preciobase).place(x=180,y=90)
        
        self.__ventana.mainloop()
    def calcular(self):
        ttk.Label(self.__ventana,text='Hola').place(x=300,y=290)
def testapp():
    miapp=calculariva()
if __name__=='__main__':
    testapp()