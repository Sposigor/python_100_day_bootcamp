''' Exercicio dia 34 '''

from tkinter import Tk, Label, Canvas, PhotoImage, Button
from mecanismo_pergunta import MecanismoPergunta

tema_cor = "#375362"


class InterfaceJogo:
    ''' Interface UI do jogo de perguntas '''
    def __init__(self, mecanismo_pergunta: MecanismoPergunta):
        ''' Inicializar a classe e os metodos '''
        self.pergunta = mecanismo_pergunta

        self.window = Tk()
        self.window.title("Perguntas")
        self.window.config(padx=20, pady=20, bg=tema_cor)

        self.placar_label = Label(text="Placar: 0", fg="white", bg=tema_cor)
        self.placar_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.texto_questão = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Questão",
            fill=tema_cor,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        imagem_verdadeiro = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 34\Verdadeiro.png")
        self.botão_verdadeiro = Button(image=imagem_verdadeiro, highlightthickness=0, command=self.correto_click)
        self.botão_verdadeiro.grid(row=2, column=0)

        imagem_falso = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 34\Falso.png")
        self.botão_falso = Button(image=imagem_falso, highlightthickness=0, command=self.falso_click)
        self.botão_falso.grid(row=2, column=1)

        self.ir_para_proxima_pergunta()

        self.window.mainloop()

    def ir_para_proxima_pergunta(self):
        ''' Proxima pergunta '''
        self.canvas.config(bg="white")
        if self.pergunta.ainda_tem_pergunta():
            self.placar_label.config(text=f"Placar: {self.pergunta.placar}")
            texto_pergunta = self.pergunta.nova_questão()
            self.canvas.itemconfig(self.texto_questão, text=texto_pergunta)
        else:
            self.canvas.itemconfig(self.texto_questão, text="Você terminou as perguntas")
            self.botão_verdadeiro.config(state="disabled")
            self.botão_falso.config(state="disabled")

    def correto_click(self):
        ''' Quando aperta o botão correto '''
        self.retorno_click(self.pergunta.check_pergunta("True"))

    def falso_click(self):
        ''' Quando aperta o botão incorreto '''
        esta_certo = self.pergunta.check_pergunta("False")
        self.retorno_click(esta_certo)

    def retorno_click(self, esta_certo):
        ''' Retorna o resultado do click '''
        if esta_certo:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.ir_para_proxima_pergunta)
