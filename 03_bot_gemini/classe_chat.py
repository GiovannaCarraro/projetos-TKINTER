import tkinter as tk
from classe_bot_gemini import Gemini_Bot

class Janela_chat():
    def __init__(self):

        #Instanciando a classe
        self.robo = Gemini_Bot()

        #Criando a janela
        self.janela = tk.Tk()
        self.janela.title("Boa noite Cinderela")

        #Configurações da janela
        self.janela.configure(bg= "#073875")
        self.janela.geometry("800x500")
        self.janela.resizable(False,False)
        self.janela.iconbitmap("03_bot_gemini/sleeping (2).ico")

        self.label_titulo = tk.Label(self.janela,
                                text = "Boa noite!",
                                foreground= "black",
                                bg="#073875",
                                font="arial")
        self.label_titulo.pack(pady=10)

        #Texto digite sua pergunte
        self.label_pergunta = tk.Label(self.janela,
                                  text = "O que você deseja saber?")
        self.label_pergunta.pack(pady=10)

        #Caixa de texto para a pergunta
        self.caixa = tk.Entry(self.janela,
                font=("Arial", 18))
        self.caixa.pack(pady=10)

        #Botão para o progroma responder a pergunta
        self.button_resposta = tk.Button(self.janela,
                            text="Perguntar")
                             
        self.button_resposta.pack()

        #label resultado
        self.label_resultado = tk.Label(self.janela,
                                text= "",
                                font= ("Arial", 20),
                                foreground= "black")
        self.label_resultado.pack()

        

def responder(self):
    self.caixa = self.label.caixa.get()
    resposta = self.robo.enviar_mensagem(self.caixa)
    self.label_resultado.config(text=resposta)

    

def run(self):
    self.janela.mainloop()

if __name__ == "__main__":
    chat = Janela_chat()
    chat.run()
    
