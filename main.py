from tkinter import *
from tkinter import messagebox #No es una clase ni un metodo, por eso no se importa con el *
import pyperclip
import json

FUENTE = ("Times New Roman", 12, "italic")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from random import choice, randint, shuffle
def generador_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols #Asi se crea una lista a partir de otras
    shuffle(password_list)
    

    password = "".join(password_list)

   
    introducir_password.insert(0, password)
    pyperclip.copy(password)
    
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save ():
    website = introducir_website.get()
    email = introducir_email.get()
    password = introducir_password.get()
    new_data = {website: {
                    "email": email,
                    "password": password,
        }
        }
    
    if ((len(password) == 0) or (len(website) == 0) or (len(email) == 0) ):
        messagebox.showinfo(title="Cuidado", message="Has dejado un cuadro sin responder")
    else:    
        try:    
            with open (r"passwords\AlmacenPasswords.json", mode="r") as file:
                #json.dump(new_data, file, indent=4)
                #Se lee la informacion
                data = json.load(file)
                
        except FileNotFoundError:

            with open (r"passwords\AlmacenPasswords.json", mode="w") as file:
                #Se guarda la info actualizada
                json.dump(new_data, file, indent=4)
        else:
            #Se actualiza la info
            data.update(new_data)
            with open (r"passwords\AlmacenPasswords.json", mode="w") as file:
                #json.dump(new_data, file, indent=4)
                json.dump(data, file, indent=4)
                #Se actualiza la info
                #data.update(new_data)
                
        finally:        
            #introducir_email.delete(0,END)#Borra desde el elemento 0 hasta el final
            introducir_password.delete(0,END)
            introducir_website.delete(0,END)
            
    # ---------------------------- PASSWORD SEARCHER ------------------------------- #
            
def searcher ():
    
    website = introducir_website.get()
    email = introducir_email.get()
    password = introducir_password.get()
    
    
    
    
    try:  
        with open (r"passwords\AlmacenPasswords.json", mode="r") as file:
            data = json.load(file)
            website_registrado = data.keys()
            valores_registrados = data.values()
            
    except FileNotFoundError:
        messagebox.showinfo(title="Datos", message="Actualmente no hay ninguna cuenta asociada")
        
    else:
        if (website in website_registrado) == True:
            for datos in valores_registrados:
                email_registrado =  datos["email"]
                passwordd_registrada = datos ["password"]
                if email == email_registrado:
                    messagebox.showinfo(title=website, message=f"El email es: {email_registrado}\ny la password es: {passwordd_registrada}")
                else:
                    messagebox.showinfo(title="Error", message="Los datos ingresados son incorrectos o no hay una cuenta asociada")
                    
        else:
            messagebox.showinfo(title=f"{website}", message="Los datos ingresados son incorrectos o no hay una cuenta asociada")
    finally:
        pass       
            
    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="white")



imagen = Canvas(height=200, width=200, background="white", highlightthickness=0)
imagen_candado = PhotoImage(file=r"passwords\logo.png")
imagen.create_image(100, 100, image=imagen_candado)#La posicion de la  imagen dentro del canvas
imagen.grid(column=1, row=0)

#---------------------LABELS---------------------
website = Label (text="Website:", font=FUENTE, background="white", highlightthickness=0)
website.grid(column=0,row=1, sticky="E")

email_username = Label(text="Email/Username:", font=FUENTE, background="white", highlightthickness=0)
email_username.grid(column=0, row=2, sticky="E")

passwordl = Label(text="Password:", font=FUENTE, background="white", highlightthickness=0)
passwordl.grid(column=0, row=3, sticky="E")

#---------------------ENTRADAS---------------------

introducir_website = Entry(width=35, highlightthickness=0)
introducir_website.grid(column=1, row=1, columnspan=2, sticky="W")#EL WE IGNORA EL WIDHT PERO HACE CUMPLIR LA FUNCION DE QUE ESTE SOBRE EL BOTON
introducir_website.focus()#Para que al abrir la app puedas ingresar el sitio directamente

introducir_email = Entry(width=35, highlightthickness=0)
introducir_email.grid(column=1, row=2, columnspan=2, sticky="W")
introducir_email.insert(0, "slowness@gmail.com")


introducir_password = Entry(width=35, highlightthickness=0)
introducir_password.grid(column=1, row=3, columnspan=2, sticky="W")
#---------------------BOTONES---------------------
agregar = Button(text="Agregar", width=36, background="white", highlightthickness=0,command=save)
agregar.grid(column=1, row=4)

generar_password = Button(text="Generar Password", background="white", highlightthickness=0, command=generador_passwords)
generar_password.grid(column=2, row=3)

buscar_password = Button(text="Buscar", background="white", highlightthickness=0, command=searcher)
buscar_password.grid(column=2, row=1)

window.mainloop()