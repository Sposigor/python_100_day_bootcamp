''' Exercicio do dia 28 '''

from tkinter import Tk, Label, Button, Canvas, PhotoImage, FLAT
import math

# Variaveis
rosa = "#e2979c"
vermelho = "#e7305b"
verde = "#9bdeac"
amarelo = "#f7f5dd"
nome_fonte = "Courier"
tempo_produtivo = 25
tempo_descanso = 5
tempo_recuperação = 25
repetição = 0
tempo = None

# ---------------------------- Mecanica do reset ------------------------------- #
def resetar_cronometro():
    ''' Reseta o cronometro '''
    janela.after_cancel(tempo)
    canvas.itemconfig(texto_tempo, text='00:00')
    tempo_label.config(text='Timer', fg=amarelo)
    check.config(text="")
    global repetição
    repetição = 0
    iniciar['state'] = 'normal'
# ---------------------------- Mecanica do iniciar ------------------------------- #
def iniciar_cronometro():
    ''' Iniciar o cronometro '''
    global repetição
    repetição += 1

    trabalho = tempo_produtivo * 60
    intervalo_leve = tempo_descanso * 60
    pausa_para_recuperar = tempo_recuperação * 60

    if repetição % 8 == 0:
        cronometro(pausa_para_recuperar)
        tempo_label.config(text='Pausa para recuperar', fg=rosa)
    elif repetição % 2 == 0:
        cronometro(intervalo_leve)
        tempo_label.config(text='Intervalo leve', fg=vermelho)
    else:
        cronometro(trabalho)
        tempo_label.config(text='Trabalho', fg=verde)
        iniciar['state'] = 'disabled'


# ---------------------------- Mecanica do cronometro ------------------------------- #
def cronometro(contagem):
    ''' Cronometro do pomodoro '''
    # Formatos de minutos e segundos para o cronometro
    formata_em_minutos = math.floor(contagem / 60)
    formata_em_segundos = contagem % 60
    # Correção do bug de contagem abaixo de 10
    if formata_em_segundos < 10:
        formata_em_segundos = f'0{formata_em_segundos}'
    # Mecanica de funcionamento do cronometro
    canvas.itemconfig(texto_tempo, text=f'{formata_em_minutos}:{formata_em_segundos}')
    if contagem > 0:
        global tempo
        tempo = janela.after(1000, cronometro, contagem - 1)
    else:
        iniciar_cronometro()
        check_icone = ""
        trabalho = math.floor(repetição / 2)
        for _ in range(trabalho):
            check_icone += "✔"
        check.config(text=check_icone)

# ---------------------------- UI SET""UP ------------------------------- #

# Configuração da janela principal
janela = Tk()
janela.title("Metodo de Pomodoro")
janela.config(padx=100, pady=50, bg=amarelo)

# Texto temnpo
tempo_label = Label(text="Tempo", font=(nome_fonte, 20, 'bold'), fg=verde, bg=amarelo)
tempo_label.grid(row=0, column=1)

# Imagem do tomate e cronometro do tempo
canvas = Canvas(width=200, height=224, bg=amarelo, highlightthickness=0)
tomate_img = PhotoImage(file=r"Nivel - Intermediario dia 15 a 58\exercicios\dia 28\tomato.png")
canvas.create_image(100, 112, image=tomate_img)
texto_tempo = canvas.create_text(100, 128, text="00:00", font=(nome_fonte, 25, 'bold'),
                                    fill='white')
canvas.grid(column=1, row=1)


# Botão iniciar
iniciar = Button(text="Iniciar", highlightthickness=0, relief=FLAT, bg=amarelo,
                    fg='black', font=(nome_fonte, 8), command=iniciar_cronometro)
iniciar.grid(row=3, column=0)

# Botão reiniciar
reiniciar = Button(text="Reiniciar", highlightthickness=0, relief=FLAT, bg=amarelo,
                    fg='black', font=(nome_fonte, 8 ), command=resetar_cronometro)
reiniciar.grid(row=3, column=2)

# Check
check_icone = '✔'
check = Label(text=check_icone, font=(nome_fonte, 20, 'bold'), fg=verde, bg=amarelo)
check.grid(row=4, column=1)


janela.mainloop()
