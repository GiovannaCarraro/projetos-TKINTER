import ttkbootstrap as tk
import tkinter.messagebox


class Cadastro():
    def __init__(self):

        self.janela = tk.Window(themename="minty")
        self.janela.title = ("Painel de Cadastro")
        self.janela.configure(bg="")
        self.janela.geometry("800x500") 
        self.janela.resizable(False, False)

        self.label_titulo = tk.Label(self.janela,
                        text="Painel de Cadastro",
                        background="",
                        font="Arial",
                        foreground="")
        self.label_titulo.pack(pady=20)

        self.caixa_senha = tk.Label(self.janela,
                                    text="Digite seu nome de usuario",
                                    font=("Arial"))
        self.caixa_senha.pack()

        self.caixa_login1 = tk.Entry(font=("Arial", 18))
        self.caixa_login1.pack(pady=10)

        self.caixa_senha2 = tk.Label(self.janela,
                                    text= "Digite sua senha",
                                    font=("Arial"))
        self.caixa_senha2.pack(pady=10)
        
        self.caixa_senha2 = tk.Entry(show="*",
                                    font= ("Arial", 18))
        self.caixa_senha2.pack()         
        
        frame_botao = tk.Frame()
        frame_botao.pack()

        tk.Button(frame_botao, text = "Login", command=self.logar, padding=(10)).pack(side="left",padx=10)
        tk.Button(frame_botao, text = "Sair", command=self.sair, padding=(10), bootstyle = "danger").pack(side="right",pady=10)

    def logar (self):
        usuario_senha = (self.caixa_senha2.get())
        usuario_nome = (self.caixa_login1.get())
        if usuario_nome == "123" and usuario_senha == "123":
                
            self.janela.destroy()
            janela = Cadastro()
            janela.run()
            
        else:
                tkinter.messagebox.showerror(title="ERRO", message="Senha inválida")

    def sair (self):
        resposta = tkinter.messagebox.askyesno(title="LOGIN", message= "Você deseja sair?")
        if resposta == True:
            exit()

       



    def run (self):
        self.janela.mainloop()

if __name__ == "__main__":
    janela = Cadastro()
    janela.run()