from tkinter import *

papel= Tk()
papel.title("PAVL & Co.")
papel.geometry("500x500")


def guardar():
    notas=texto.get("1.0",END)
    with open("Blog de notas.txt","w") as write:
        write.write(notas)

def nuevo():
    with open("Blog de nuevo.txt","w") as write:
        with open("Blog de nuevo.txt","r") as read:
            leer=str(read.read())
            insertar=texto.insert("1.0",leer,END)

bara=Menu(papel)
papel.config(menu=bara)

archivos=Menu(bara,tearoff=False)
bara.add_cascade(label="Archivos",menu=archivos)
archivos.add_command(label="Nuevo",command=nuevo)
archivos.add_command(label="Guardar",command=guardar)
archivos.add_command(label="Cerrar",command=exit)


texto=Text(papel,height=500,borderwidth=2,relief="raised")
texto.pack(fill="both") 
mainloop()