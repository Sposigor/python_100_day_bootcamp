''' Exercicio dia 30 '''

from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage, END, messagebox, FLAT
from random import choice, shuffle, randint
import json
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
    armazenamento = {
        site: {
            'usuario/email': usuario,
            'senha': senha
        }
    }

    if usuario == '' or site == '' or senha == '':
        messagebox.showerror('Erro', 'Preencha todos os campos!')
    else:
        confirma_salvamento = messagebox.askokcancel(title='Confirmação',
                            message=f'Esse são os dados: \Site: {site} \n'
                            f'Usuario: {usuario} \nSenha: {senha}\nAperte OK para confirmar')

        if confirma_salvamento:
            try:
                with open(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 30\senha.json', 'r') as arquivo:
                    # Carrega os dados já salvos no .json
                    dados = json.load(arquivo)

            except FileNotFoundError:
                with open(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 30\senha.json', 'w') as arquivo:
                    # Criar um arquivo novo se não houver
                    json.dump(armazenamento, arquivo, indent=4)

            else:
                # Atualizar os dados já salvos no .json
                dados.update(armazenamento)
                with open(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 30\senha.json', 'w') as arquivo:
                    # Salva os novos dados no .json
                    json.dump(dados, arquivo, indent=4)

            finally:
                site_texto.delete(0, END)
                senha_texto.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
def encontrar_senha_salva():
    ''' Encontrar senha salva '''
    site = site_texto.get()
    try:
        with open("Nivel - Intermediario dia 15 a 58\exercicios\dia 30\senha.json", 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Não existe nenhuma senha salva")
    else:
        if site in dados:
            usuario = dados[site]['usuario/email']
            senha = dados[site]['senha']
            messagebox.showinfo(title=site, message=f"Usuario/Email: {usuario}\nSenha: {senha}")
        else:
            messagebox.showinfo(title="Error", message=f"Não possuir senhas salvas do {site}.")

# ---------------------------- UI SETUP ------------------------------- #
# Criando a janela
janela = Tk()
janela.title('Gerador de Senhas')
janela.config(padx=50, pady=50)

# Imagem logo do gerador de senhas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 30\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
site_label = Label(text='Sites:')
site_label.grid(row=1, column=0)
user_label = Label(text='Usuário/Email:')
user_label.grid(row=2, column=0)
senha_label = Label(text='Senha:')
senha_label.grid(row=3, column=0)

# Entrada de dados
site_texto = Entry(width=33)
site_texto.grid(row=1, column=1)
site_texto.focus()
user_texto = Entry(width=47)
user_texto.grid(row=2, column=1, columnspan=2)
user_texto.insert(0, 'sposigor@gmail.com')
senha_texto = Entry(width=33)
senha_texto.grid(row=3, column=1)

# Botões
pesquisa_site = Button(text='Pesquisar', width=10, command=encontrar_senha_salva)
pesquisa_site.grid(row=1, column=2)
gerador_senha = Button(text=' Gerar Senha', command=gerador_senha, width=10)
gerador_senha.grid(row=3, column=2)
add_senha = Button(text='Adicionar Senha', width=35, command=salvar_senha)
add_senha.grid(row=4, column=1, columnspan=2)

janela.mainloop()
