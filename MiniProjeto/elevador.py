import tkinter as tk
import RegrasElevador as rules
from experta import Fact
import tkinter.font as tkFont

# Busca nas regras para qual andar irá
def verificaRegras():
    controleElevador = rules.RegrasElevador()
    controleElevador.reset()

    controleElevador.declare(Fact(AndarAtual=str(escolhaAndarAtual.get())))
    controleElevador.declare(Fact(AndarDesejado=str(escolhaAndarDesejado.get())))
    controleElevador.declare(Fact(CaminhoAtual=str(caminhoElevador.get())))
    controleElevador.run()

    return controleElevador.resposta

def janela_andar_atual():
    fontTipo = tkFont.Font(family="Helvetica", size=15)
    tk.Label(raiz, text="Em qual andar o elevador está?", width=60, bg=background, font=fontTipo).grid(row=0, column=0)

    c1 = tk.Checkbutton(raiz, text="1o andar", variable=escolhaAndarAtual, onvalue=1, width=50, height=5,
                        bg=background)
    c1.grid(row=1, column=0)

    c1 = tk.Checkbutton(raiz, text="2o andar", variable=escolhaAndarAtual, onvalue=2, width=50, height=5,
                        bg=background)
    c1.grid(row=2, column=0)

    c1 = tk.Checkbutton(raiz, text="3o andar", variable=escolhaAndarAtual, onvalue=3, width=50, height=5,
                        bg=background)
    c1.grid(row=3, column=0)

    c1 = tk.Checkbutton(raiz, text="4o andar", variable=escolhaAndarAtual, onvalue=4, width=50, height=5,
                        bg=background)
    c1.grid(row=4, column=0)

    c1 = tk.Checkbutton(raiz, text="5o andar", variable=escolhaAndarAtual, onvalue=5, width=50, height=5,
                        bg=background)
    c1.grid(row=5, column=0)

    c1 = tk.Checkbutton(raiz, text="6o andar", variable=escolhaAndarAtual, onvalue=6, width=50, height=5,
                        bg=background)
    c1.grid(row=6, column=0)

    b1 = tk.Button(raiz, text="Continuar", command=caminho_elevador, bg=background)
    b1.grid(row=18, column=0, padx=0, pady=0)

def caminho_elevador():
    fontTipo = tkFont.Font(family="Helvetica", size=15)
    tk.Label(raiz, text="Para qual andar o elevador está a caminho?", width=60, bg=background, font=fontTipo).grid(row=0, column=0)

    c1 = tk.Checkbutton(raiz, text="A caminho do 1o andar", variable=caminhoElevador, onvalue=1, width=50, height=5,
                        bg=background)
    c1.grid(row=1, column=0)

    c1 = tk.Checkbutton(raiz, text="A caminho do 2o andar", variable=caminhoElevador, onvalue=2, width=50, height=5,
                        bg=background)
    c1.grid(row=2, column=0)

    c1 = tk.Checkbutton(raiz, text="A caminho do 3o andar", variable=caminhoElevador, onvalue=3, width=50, height=5,
                        bg=background)
    c1.grid(row=3, column=0)

    c1 = tk.Checkbutton(raiz, text="A caminho do 4o andar", variable=caminhoElevador, onvalue=4, width=50, height=5,
                        bg=background)
    c1.grid(row=4, column=0)

    c1 = tk.Checkbutton(raiz, text="A caminho do 5o andar", variable=caminhoElevador, onvalue=5, width=50, height=5,
                        bg=background)
    c1.grid(row=5, column=0)

    c1 = tk.Checkbutton(raiz, text="A caminho do 6o andar", variable=caminhoElevador, onvalue=6, width=50, height=5,
                        bg=background)
    c1.grid(row=6, column=0)

    c1 = tk.Checkbutton(raiz, text="Elevador livre", variable=caminhoElevador, onvalue=999, width=50, height=5,
                        bg=background)
    c1.grid(row=7, column=0)

    b1 = tk.Button(raiz, text="Continuar", command=result, bg=background)
    b1.grid(row=18, column=0, padx=0, pady=0)

# def janela_andar_atual():
#     print(escolhaAndarDesejado.get())
#     raiz.withdraw()
#     andarAtual = tk.Tk()
#     andarAtual.title("Controle de um elevador")
#     background = "#C0C0C0"
#     andarAtual.columnconfigure(0, weight=1, minsize=75)
#     andarAtual.rowconfigure(0, weight=1, minsize=50)
#     andarAtual.geometry("400x400")
#     andarAtual.config(bg=background)
#     andarAtual.resizable(True, True)
#     fontTipo = tkFont.Font(family="Helvetica", size=15)
#     tk.Label(andarAtual, text="Em qual andar o elevador está?", width=60, bg=background, font=fontTipo).grid(row=0,
#                                                                                                              column=0)
#     c2 = tk.Checkbutton(andarAtual, text="1o andar", variable=escolhaAndarAtual, onvalue=1, width=50,height=5,
#                         bg=background)
#     c2.grid(row=1, column=0)
#
#     c2 = tk.Checkbutton(andarAtual, text="2o andar", variable=escolhaAndarAtual, onvalue=2, width=50,
#                         height=5,
#                         bg=background)
#     c2.grid(row=2, column=0)
#
#     c2 = tk.Checkbutton(andarAtual, text="3o andar", variable=escolhaAndarAtual, onvalue=3, width=50,
#                         height=5,
#                         bg=background)
#     c2.grid(row=3, column=0)
#     b2 = tk.Button(andarAtual, text="Continuar", command=result, bg=background)
#     b2.grid(row=18, column=0, padx=0, pady=0)


def result():
    print(caminhoElevador.get())
    newWindow = tk.Toplevel()
    newWindow.title("Resultado")
    newWindow.geometry("250x250")
    tk.Label(newWindow, text="Resultado").pack()

    response = verificaRegras()
    if response == '':
        response = 'Preencha todos os campos'
    tk.Label(newWindow, text=str(response)).pack()

background = "#C0C0C0"
raiz = tk.Tk()
raiz.title("Controle de um elevador")
raiz.columnconfigure(0, weight=1, minsize=75)
raiz.rowconfigure(0, weight=1, minsize=50)
raiz.geometry("400x720")
raiz.config(bg=background)
raiz.resizable(True, True)

# variaveis de escolha dos campos selecionados
escolhaAndarDesejado = tk.IntVar()
escolhaAndarAtual = tk.IntVar()
caminhoElevador = tk.IntVar()

fontStyle = tkFont.Font(family="Helvetica", size=20, weight="bold")

fontTipo = tkFont.Font(family="Helvetica", size=15)
tk.Label(raiz, text="Escolha o andar desejado", width=60, bg=background, font=fontTipo).grid(row=0, column=0)

c1 = tk.Checkbutton(raiz, text="1o andar", variable=escolhaAndarDesejado, onvalue=1, width=50, height=5, bg=background)
c1.grid(row=1, column=0)

c1 = tk.Checkbutton(raiz, text="2o andar", variable=escolhaAndarDesejado, onvalue=2, width=50, height=5, bg=background)
c1.grid(row=2, column=0)

c1 = tk.Checkbutton(raiz, text="3o andar", variable=escolhaAndarDesejado, onvalue=3, width=50, height=5, bg=background)
c1.grid(row=3, column=0)

c1 = tk.Checkbutton(raiz, text="4o andar", variable=escolhaAndarDesejado, onvalue=4, width=50, height=5, bg=background)
c1.grid(row=4, column=0)

c1 = tk.Checkbutton(raiz, text="5o andar", variable=escolhaAndarDesejado, onvalue=5, width=50, height=5, bg=background)
c1.grid(row=5, column=0)

c1 = tk.Checkbutton(raiz, text="6o andar", variable=escolhaAndarDesejado, onvalue=6, width=50, height=5, bg=background)
c1.grid(row=6, column=0)

b1 = tk.Button(raiz, text="Continuar", command=janela_andar_atual, bg=background)
b1.grid(row=18, column=0, padx=0, pady=0)

raiz.mainloop()