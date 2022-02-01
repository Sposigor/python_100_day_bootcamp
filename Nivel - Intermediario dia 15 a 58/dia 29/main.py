''' Exercicio do dia 29 '''

from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage, END, messagebox
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- Abrir senha ------------------------------- #
#Password Generator Project
def gerador_senha():
    ''' Função para gerar senha '''
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    senha_letras = [choice(letras) for _ in range(randint(8, 10))]
    senhas_simbolos = [choice(simbolos) for _ in range(randint(2, 4))]
    senhas_numeros = [choice(numeros) for _ in range(randint(2, 4))]

    lista_senha = senha_letras + senhas_simbolos + senhas_numeros
    shuffle(lista_senha)

    senha = "".join(lista_senha)
    senha_texto.insert(0, senha)
    pyperclip.copy(senha)

# ---------------------------- Salvar nova senha ------------------------------- #
def salvar_senha():
    ''' Salva a senha em um TXT '''

    usuario = user_texto.get()
    site = site_texto.get()
    senha = senha_texto.get()

    if usuario == '' or site == '' or senha == '':
        messagebox.showerror('Erro', 'Preencha todos os campos!')
    else:
        confirma_salvamento = messagebox.askokcancel(title='Confirmação',
                            message=f'Esse são os dados: \Site: {site} \n'
                            f'Usuario: {usuario} \nSenha: {senha}\nAperte OK para confirmar')

        if confirma_salvamento:
            with open(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 29\senha.txt', 'a') as arquivo:
                arquivo.write(f'{site} - {usuario} - {senha}\n')
                site_texto.delete(0, END)
                senha_texto.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Criando a janela
janela = Tk()
janela.title('Gerador de Senhas')
janela.config(padx=50, pady=50)

# Imagem logo do gerador de senhas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 29\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Sites de armazenamento de senhas
site_label = Label(text='Sites:', font=('Courier', 8, 'bold'))
site_label.grid(row=1, column=0)
site_texto = Entry(width=46)
site_texto.grid(row=1, column=1, columnspan=2)
site_texto.focus()

# Email e Username
user_label = Label(text='Usuário/Email:', font=('Courier', 8, 'bold'))
user_label.grid(row=2, column=0)
user_texto = Entry(width=46)
user_texto.grid(row=2, column=1, columnspan=2)
user_texto.insert(0, 'sposigor@gmail.com')

# Senha
senha_label = Label(text='Senha:', font=('Courier', 8, 'bold'))
senha_label.grid(row=3, column=0)
senha_texto = Entry(width=33)
senha_texto.grid(row=3, column=1)
gerador_senha = Button(text=' Gerar Senha', command=gerador_senha)
gerador_senha.grid(row=3, column=2)

# Adicionando nova senha
add_senha = Button(text='Adicionar Senha', width=39, command=salvar_senha)
add_senha.grid(row=4, column=1, columnspan=2)

janela.mainloop()
