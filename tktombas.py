from tkinter import *
import os

#criar um objeto para usar o tk

def mensagem():
    mensagem['text'] = 'CADASTRO REALIZADO'

tela = Tk()

monitor_height = tela.winfo_screenheight()
monitor_width = tela.winfo_screenwidth()

tela.geometry(f'{monitor_width}x{monitor_height}')
tela.title('minha primeira linha')
nome = Label(tela,text='Nome:',font='Georgia').place(x=30,y=30)
email = Label(tela,text='Email:',font='Georgia').place(x=30,y=60)
telefone = Label(tela,text='telefone:',font='Georgia').place(x=30,y=90)
campo_nome = Entry(tela,width=20,font='Verdana').place(x=130,y=30)
campo_email = Entry(tela,width=20,font='Verdana').place(x=130,y=60)
campo_telefone = Entry(tela,width=20,font='Verdana').place(x=130,y=90)

botao = Button(tela,background='#000080',fg='#fff',command=mensagem,text='cadastrar').place(x=130,y=120)

mensagem = Label(tela,text='')
mensagem.grid(column=0,row=2,padx = 10,pady = 10)






tela.mainloop() 