

rayuela = ["1","2","3","4","5","6","7","8","cielo"] #Arreglo que contiene las posiciones de la rayuela
piedra = "4" #@param{type:"string"}

piedra = input('Digite No. A Donde Va La Piedra ....:')

from tkinter import *

master = Tk()

master.title('Rayuela')

canvas = Canvas(width=800, height=600, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_rectangle(170, 80, 80, 40, width=5, fill='green')
canvas.create_text(120, 60,text='1', fill='white',font="Arial")
canvas.create_rectangle(170, 80, 80, 120, width=5, fill='green')
canvas.create_text(120, 100, text='2', fill='white',font="Arial")
canvas.create_rectangle(170, 120, 80, 160, width=5, fill='green')
canvas.create_text(120, 140, text='3', fill='white',font="Arial")

canvas.create_rectangle(120, 160, 50, 200, width=5, fill='green')
canvas.create_text(90, 180, text='5', fill='white',font="Arial")
canvas.create_rectangle(120, 160, 200, 200, width=5, fill='green')
canvas.create_text(160, 180, text='4', fill='white',font="Arial")

canvas.create_rectangle(170, 200, 80, 240, width=5, fill='green')
canvas.create_text(120, 220, text='6', fill='white',font="Arial")

canvas.create_rectangle(120, 240, 50, 280, width=5, fill='green')
canvas.create_text(90, 260, text='8', fill='white',font="Arial")


canvas.create_rectangle(120, 240, 200, 280, width=5, fill='green')
canvas.create_text(160, 260, text='7', fill='white',font="Arial")

canvas.create_arc(50, 260, 200, 300, width=5, start=180, extent=180, fill='yellow')
canvas.create_text(120, 290, text='Cielo', fill='red',font="Arial")

#rayuela = ["1","2","3","4","5","6","7","8","cielo"] #Arreglo que contiene las posiciones de la rayuela
#piedra = "4" #@param{type:"string"}

recorrido_ida = rayuela[1:]

msj = "Piedra", "En:",piedra

label = Label(master, text=msj)
label.pack()
label.config(fg="blue",    # Foreground
             bg="gray90",   # Background
             font=("Verdana",10)) 

if piedra == "1":
        canvas.create_rectangle(170, 80, 80, 40, width=5, fill='red')
        canvas.create_text(120, 60,text='1', fill='white',font="Arial")
        recorrido_ida
        recorrido_vuelta = list(reversed(recorrido_ida))
        for elemento in recorrido_ida:
            Label(text=elemento).pack()
        for elemento in recorrido_vuelta:
            Label(text=elemento).pack()

elif piedra == "2":
        canvas.create_rectangle(170, 80, 80, 120, width=5, fill='red')
        canvas.create_text(120, 100, text='2', fill='white',font="Arial")
        recorrido_ida2 = recorrido_ida[1:]
        recorrido_vuelta2 = list(reversed(recorrido_ida2))        
        Label(text=rayuela[0]).pack()
        for elemento in recorrido_ida2:
            Label(text=elemento).pack()
        for elemento in recorrido_vuelta2:
            Label(text=elemento).pack()
        Label(text=rayuela[0]).pack()

elif piedra == "3":
        canvas.create_rectangle(170, 120, 80, 160, width=5, fill='red')
        canvas.create_text(120, 140, text='3', fill='white',font="Arial")
        recorrido_ida3 = recorrido_ida[2:]
        recorrido_vuelta3 = list(reversed(recorrido_ida3))     
        Label(text=rayuela[0]).pack()
        Label(text=rayuela[1]).pack()
        for elemento in recorrido_ida3:
            Label(text=elemento).pack()
        for elemento in recorrido_vuelta3:
            Label(text=elemento).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[0]).pack()

elif piedra == "4":
        canvas.create_rectangle(120, 160, 200, 200, width=5, fill='red')
        canvas.create_text(160, 180, text='4', fill='white',font="Arial")   
        recorrido_ida4 = recorrido_ida[3:]
        recorrido_vuelta4 = list(reversed(recorrido_ida4))       
        Label(text=rayuela[0]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[2]).pack()
        for elemento in recorrido_ida4:
            Label(text=elemento).pack()
        for elemento in recorrido_vuelta4:
            Label(text=elemento).pack()
        Label(text=rayuela[2]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[0]).pack()

elif piedra == "5":
        canvas.create_rectangle(120, 160, 50, 200, width=5, fill='red')
        canvas.create_text(90, 180, text='5', fill='white',font="Arial")
        recorrido_ida5 = recorrido_ida[4:]
        recorrido_vuelta5 = list(reversed(recorrido_ida5))
        Label(text=rayuela[0]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[2]).pack()
        Label(text=rayuela[3]).pack()
        for elemento in recorrido_ida5:
            Label(text=elemento).pack()
        for elemento in recorrido_vuelta5:
            Label(text=elemento).pack()
        Label(text=rayuela[3]).pack()
        Label(text=rayuela[2]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[0]).pack()

elif piedra == "6":
        canvas.create_rectangle(170, 200, 80, 240, width=5, fill='red')
        canvas.create_text(120, 220, text='6', fill='white',font="Arial")
        recorrido_ida6 = recorrido_ida[5:]
        recorrido_vuelta6 = list(reversed(recorrido_ida6))
        Label(text=rayuela[0]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[2]).pack()
        Label(text=rayuela[3]).pack()
        Label(text=rayuela[4]).pack()
        for elemento in recorrido_ida6:
            Label(text=elemento).pack()
        for elemento in recorrido_vuelta6:
            Label(text=elemento).pack()
        Label(text=rayuela[4]).pack()
        Label(text=rayuela[3]).pack()
        Label(text=rayuela[2]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[0]).pack()

elif piedra == "7":
        canvas.create_rectangle(120, 240, 200, 280, width=5, fill='red')
        canvas.create_text(160, 260, text='7', fill='white',font="Arial")
        recorrido_ida7 = recorrido_ida[6:]
        recorrido_vuelta7 = list(reversed(recorrido_ida7))
        Label(text=rayuela[0]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[2]).pack()
        Label(text=rayuela[3]).pack()
        Label(text=rayuela[4]).pack()
        Label(text=rayuela[5]).pack()
        for elemento in recorrido_ida7:
            Label(text=elemento).pack()
        for elemento in recorrido_vuelta7:
            Label(text=elemento).pack()
        Label(text=rayuela[5]).pack()
        Label(text=rayuela[4]).pack()
        Label(text=rayuela[3]).pack()
        Label(text=rayuela[2]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[0]).pack()

elif piedra == "8":
        canvas.create_rectangle(120, 240, 50, 280, width=5, fill='red')
        canvas.create_text(90, 260, text='8', fill='white',font="Arial")
        recorrido_ida8 = recorrido_ida[7:]
        recorrido_vuelta8 = list(reversed(recorrido_ida8))
        Label(text=rayuela[0]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[2]).pack()
        Label(text=rayuela[3]).pack()
        Label(text=rayuela[4]).pack()
        Label(text=rayuela[5]).pack()
        Label(text=rayuela[6]).pack()
        for elemento in recorrido_ida8:
            Label(text=elemento).pack()
        for elemento in recorrido_vuelta8:
            Label(text=elemento).pack()
        Label(text=rayuela[6]).pack()
        Label(text=rayuela[5]).pack()
        Label(text=rayuela[4]).pack()
        Label(text=rayuela[3]).pack()
        Label(text=rayuela[2]).pack()
        Label(text=rayuela[1]).pack()
        Label(text=rayuela[0]).pack()

elif piedra == "cielo":
        canvas.create_arc(50, 260, 200, 300, width=5, start=180, extent=180, fill='gray90')
        canvas.create_text(120, 290, text='Cielo', fill='red',font="Arial")
        Label(text="Ganaste!!!").pack()
else:
        Label(text="Lo siento. Tu turno acabó").pack()
    
mainloop()


