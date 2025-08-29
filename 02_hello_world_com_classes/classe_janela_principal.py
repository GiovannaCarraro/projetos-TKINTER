import ttkbootstrap as tk

class Janela_principal:
    """Classe para a criação da janela principal"""

    def __init__(self):
        
        #criando uma janela
        self.janela = tk.Window(themename="darkly")

        self.janela.title("Hello World")
        self.janela.iconbitmap("01_hello_word/sun.ico")
        self.janela.geometry("800x500")
        self.janela.resizable(False,False)

        #Criando os widgets
        self.label_titulo = tk.Label(self.janela,
                                text="Hello world!")
                                
                        
        self.label_titulo.pack()

        #texto digite seu nome
        self.label_nome = tk.Label(self.janela,
                            text="Digite seu nome")
        self.label_nome.pack()

        #caixa de texto para digitar o nome
        self.caixa = tk.Entry(self.janela
                        )
                    
        self.caixa.pack(pady=10)


    

        #Botão para o progroma falar bom dia
        self.button_bomdia = tk.Button(self.janela,
                                text="Desejar Bom dia",
                                command = self.desejar_bomdia)
        self.button_bomdia.pack()

        #label bom dia
        self.label_resultado = tk.Label(self.janela,
                                text= "")
                            
        self.label_resultado.pack()

    def run(self):
        """Inicia a janela"""

        #loop para manter a janela aberta
        self.janela.mainloop()

    #função do botão
    def desejar_bomdia(self):
        """Esta função serve para pegar o nome digitado na caixa de texto e desejar um bom dia"""
        nome = self.caixa.get()
        self.label_resultado.configure(text=f"Bom dia, {nome}")