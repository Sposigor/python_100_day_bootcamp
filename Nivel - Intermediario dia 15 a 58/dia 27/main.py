''' Exercicio do dia 27 '''

from tkinter import Tk, Label, Entry, Button

janela = Tk()
janela.title('Conversor de Kms para Milhas')
janela.minsize(width=250, height=100)
janela.config(padx=20, pady=20)


def kms_para_milhas():
    ''' Função para converter Kms para Milhas '''
    kms = float(entrada_kms.get())
    milhas = round(kms * 0.621371)
    resultado_milhas.config(text=f'{milhas}')

entrada_kms = Entry(width=7)
entrada_kms.grid(row=0, column=1)

kms_label = Label(text='Kms')
kms_label.grid(row=0, column=2)

igual_a = Label(text='Igual á')
igual_a.grid(row=1, column=0)

resultado_milhas = Label(text='0')
resultado_milhas.grid(row=1, column=1)

resultado_label = Label(text='Milhas')
resultado_label.grid(row=1, column=2)

botão_calcular = Button(text='Calcular', command=kms_para_milhas)
botão_calcular.grid(row=2, column=1)

janela.mainloop()
