''' Exercicio do dia 33 '''

from tkinter import Tk, Button, Canvas, PhotoImage
import requests


def resposta_api():
    ''' respota da api do site '''
    url = 'https://api.kanye.rest'
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()
    frase = dados['quote']
    canvas.itemconfig(quote_text, text=frase, font=("Arial", 20))


window = Tk()
window.title("Kanye disse...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 33\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kayne vai falar aqui", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 33\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=resposta_api)
kanye_button.grid(row=1, column=0)


window.mainloop()
