from tkinter import *
from tkinter import ttk

class calculador():
    __ventana = None
    __vestimentacantidad = None
    __vestimentabase = None
    __vestimentaactual = None
    __alimentoscantidad = None
    __alimentosbase = None
    __alimentosactual = None
    __educacionactual = None
    __educacionbase = None
    __educaciocantidad = None
    
    __total=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('800x400')
        self.__ventana.configure(background='white')
        self.__ventana.title('Calculadora de indec')

        self.__vestimentacantidad = DoubleVar()
        self.__vestimentabase = DoubleVar()
        self.__vestimentaactual = DoubleVar()
        self.__alimentoscantidad = DoubleVar()
        self.__alimentosbase = DoubleVar()
        self.__alimentosactual = DoubleVar()
        self.__educacionactual = DoubleVar()
        self.__educacionbase = DoubleVar()
        self.__educaciocantidad = DoubleVar()
        self.__total=DoubleVar()
        

        ttk.Button(self.__ventana, text='Salir', command=self.__ventana.destroy).place(x=345, y=266)
        ttk.Button(self.__ventana,text='Calcular',command=self.calcular).place(x=250,y=266)
        ttk.Label(self.__ventana, text='Item').place(x=67, y=80)
        ttk.Label(self.__ventana, text='Cantidad').place(x=150, y=80)
        ttk.Label(self.__ventana, text='Precio Año base').place(x=260, y=80)
        ttk.Label(self.__ventana, text='Precio Año actual').place(x=380, y=80)
        ttk.Label(self.__ventana, text='Vestimenta').place(x=58, y=130)
        ttk.Label(self.__ventana, text='Alimentos').place(x=58, y=170)
        ttk.Label(self.__ventana, text='Educacion').place(x=58, y=210)
    
        self.vestimentacantidadEntry=ttk.Entry(textvariable=self.__vestimentacantidad).place(x=150,y=130,width=80)
        self.vestimentabaseEntry=ttk.Entry(textvariable=self.__vestimentabase).place(x=260,y=130,width=80)
        self.vestimentaactualEntry=ttk.Entry(textvariable=self.__vestimentaactual).place(x=380,y=130,width=80)
        self.alimentosactualEntry=ttk.Entry(textvariable=self.__alimentosactual).place(x=150,y=170,width=80)
        self.alimentosbaseEntry=ttk.Entry(textvariable=self.__alimentosbase).place(x=260,y=170,width=80)
        self.alimentoscantidadEntry=ttk.Entry(textvariable=self.__alimentoscantidad).place(x=380,y=170,width=80)
        self.educaciocantidadEntry=ttk.Entry(textvariable=self.__educaciocantidad).place(x=150,y=210,width=80)
        self.educacionbaseEntry=ttk.Entry(textvariable=self.__alimentosbase).place(x=260,y=210,width=80)
        self.educacionactualEntry=ttk.Entry(textvariable=self.__educacionactual).place(x=380,y=210,width=80)
        
        ttk.Label(self.__ventana,text='El IPC es %').place(x=55,y=310)

        self.__ventana.mainloop()
    def calcular(self):
        try:
            vestimenta=float((self.vestimentacantidadEntry.get()*self.vestimentabaseEntry.get())/self.vestimentaactualEntry.get())
            alimentos=float((self.alimentoscantidadEntry.get()*self.alimentosbaseEntry.get())/self.alimentosactualEntry.get())
            educacion=float((self.educaciocantidadEntry.get()*self.educacionbaseEntry.get())/self.educacionactualEntry.get())
            total=float((vestimenta+alimentos+educacion)*100)
            totalmostrar=str(total.split(','))
        except ValueError:
            ttk.Label(self.__ventana,text='Error').place(x=120,y=310)

def testAPP():
    miapp = calculador()

if __name__ == '__main__':
    testAPP()