from tkinter import *

root = Tk()

root.title("Ascii Converter")

root.geometry("400x400")

root.configure(background = "snow")


enter_word = Entry(root)

enter_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root, text = "Name in ASCII : ", bg = "orange", fg = "black")
label1 = Label(root, text = "Name in Encryption : ", bg = "orange", fg = "black")

def Converter():
    label["text"]= " "
    input_word = enter_word.get()
    for letter in input_word:
        label["text"]+= str(ord(letter))+" "
        ascii = int(ord(letter))
        e = ascii - 1
        label1["text"]+= str(chr(e))
        
btn = Button(root, text = "Show Name in ASCII Code and Encryption", command = Converter, bg = "gold", fg = "black")

btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
root.mainloop()
