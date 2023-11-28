
from tkinter import *

def mensagem():
    mensagem['text'] = "CADASTRO REALIZADO COM SUCESSO!"

tela = Tk()
tela.title("Tela de cadastro")
tela.geometry("700x300")
nome = Label(tela,text="NOME:",font="Georgia 14").place(x=30,y=50)
email = Label(tela,text="EMAIL:",font="Georgia 14").place(x=30,y=90)
telefone = Label(tela,text="TELEFONE:",font="Georgia 14").place(x=30,y=130)
campo_nome = Entry(tela,width=50,font="Verdana 14").place(x=150,y=50)
campo_email = Entry(tela,width=50,font="Verdana 14").place(x=150,y=90)
campo_telefone = Entry(tela,width=20,font="Verdana 14").place(x=150,y=130)

botao = Button(tela,text="CADASTRAR",background="#000080",font="Arial 17 bold",fg="#fff",command=mensagem).place(x=150,y=180)

mensagem = Label(tela,text="")
mensagem.grid(column=0, row=2, padx=10, pady=10)

tela.mainloop()


