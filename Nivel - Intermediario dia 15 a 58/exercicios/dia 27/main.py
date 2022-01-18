''' Exercicio do dia 27 '''

import tkinter

janela = tkinter.Tk()
janela.title('Minha primeira GUI')
janela.minsize(width=500, height=300)


etiqueta = tkinter.Label(janela, text='Funcionalidades:', font=('Arial', '12'))
etiqueta.pack(expand=True, fill='both')

janela.mainloop()
