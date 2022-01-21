''' Exercicio dia 31 '''

from tkinter import Tk, Canvas, PhotoImage, Button, FLAT
from random import choice
from pandas import read_csv, DataFrame


# Variáveis
cor_de_fundo = "#B1DDC6"
cards = []



# ---------------------------- Lendo o CSV ------------------------------- #
try:
    dados = read_csv(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 31\palavras_que_falta_aprender.csv')
except FileNotFoundError:
    dados_originais = read_csv(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 31\palavras_traduzidas_usando_googletranslate - Página1.csv')
    dicDados = dados_originais.to_dict(orient="records")
else:
    dicDados = dados.to_dict(orient="records")

# ---------------------------- Mecanismo de troca os cards ------------------------------- #
def trocar_cards():
    ''' Troca o card '''
    canvas.itemconfig(titulo_card, text='Portugues', fill='white')
    canvas.itemconfig(palavra_card, text=cards['Portugues'], fill='white')
    canvas.itemconfig(card, image=fundo_imagem)

# ---------------------------- Janela Principal ------------------------------- #
# Janela principal
janela = Tk()
janela.title("PalaCards")
janela.config(padx=50, pady=50, bg=cor_de_fundo)
tempo_de_troca = janela.after(3000, trocar_cards)

# ---------------------------- Mecanismo de palavras e temporazidor ------------------------------- #
def proxima_palavra():
    ''' Proxima palavra '''
    global cards, tempo_de_troca
    janela.after_cancel(tempo_de_troca)
    cards = choice(dicDados)
    canvas.itemconfig(titulo_card, text='Ingles', fill='black')
    canvas.itemconfig(palavra_card, text=cards['Ingles'], fill='black')
    canvas.itemconfig(card, image=frente_imagem)
    tempo_de_troca = janela.after(3000, trocar_cards)

# ---------------------------- Mecanismo de palavras e temporazidor ------------------------------- #
def voce_sabe():
    ''' novos csv com as palavras que falta aprender '''
    dicDados.remove(cards)
    palavras_que_falta_aprender = DataFrame(dicDados)
    palavras_que_falta_aprender.to_csv(r"Nivel - Intermediario dia 15 a 58\exercicios\dia 31\palavras_que_falta_aprender.csv", index=False)
    proxima_palavra()

# ---------------------------- UI SETUP ------------------------------- #
# Canvas para a imagem de fundo e texto que fica no centro
canvas = Canvas(width=800, height=526, highlightthickness=0)
fundo_imagem = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 31\fundo_card.png")
frente_imagem = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 31\frente_card.png")
card = canvas.create_image(400, 263, image=frente_imagem)
titulo_card = canvas.create_text(400, 150, text="PalaCards", font=("Arial", 40), fill="black")
palavra_card = canvas.create_text(400, 263, text="PALA CARDS", font=("Arial", 60), fill="black")
canvas.config(bg=cor_de_fundo, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Botões de ação
imagem_errado = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 31\errado.png")
botão_errado = Button(image=imagem_errado, highlightthickness=0, bg=cor_de_fundo, relief=FLAT, command=proxima_palavra)
botão_errado.grid(column=0, row=1)

imagem_correto = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 31\correto.png")
botão_correto = Button(image=imagem_correto, highlightthickness=0, bg=cor_de_fundo, relief=FLAT, command=voce_sabe)
botão_correto.grid(column=1, row=1)

proxima_palavra()
janela.mainloop()
