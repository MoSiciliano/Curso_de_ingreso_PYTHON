import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Morena
apellido: Siciliano
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        importe_uno = int(self.txt_importe_1.get())
        importe_dos = int(self.txt_importe_2.get())
        importe_tres = int(self.txt_importe_3.get())

        resultado_suma = importe_uno + importe_dos + importe_tres
        mensaje = f"El resultado de la suma es {resultado_suma}"
        alert("Mensaje", mensaje)

    def btn_promedio_on_click(self):
        importe_uno = float(self.txt_importe_1.get())
        importe_dos = float(self.txt_importe_2.get())
        importe_tres = float(self.txt_importe_3.get())

        resultado_promedio = (importe_uno + importe_dos + importe_tres) / 3
        mensaje = f"El promedio es {resultado_promedio}"
        alert("Mensaje", mensaje)

    def btn_total_iva_on_click(self):
        importe_uno = float(self.txt_importe_1.get())
        importe_dos = float(self.txt_importe_2.get())
        importe_tres = float(self.txt_importe_3.get())

        suma_importes = importe_uno  + importe_dos + importe_tres
        operación_iva = (suma_importes * 21) / 100
        resultado_con_iva = suma_importes + operación_iva
        mensaje = f"El precio final mas iva es {resultado_con_iva}"
        alert("Mensaje", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()