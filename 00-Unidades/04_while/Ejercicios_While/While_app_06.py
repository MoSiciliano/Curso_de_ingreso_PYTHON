import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_06
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero_suma = 0
        contador = 0
        while contador < 5: 
            if contador == 0:
                numero_a = prompt("Numero", "ingrese un numero")
            else:
                numero_a = prompt("Numero", "Ingrese otro numero")
            if numero_a != "":
                numero_int = int(numero_a)
            else:
                break
            
            numero_suma += numero_int
            contador += 1
            print(numero_int)
        

        self.txt_suma_acumulada.delete(0, "end")
        self.txt_suma_acumulada.insert(0, numero_suma)

        self.txt_promedio.delete(0, "end")
        self.txt_promedio.insert(0, numero_suma / 5)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
