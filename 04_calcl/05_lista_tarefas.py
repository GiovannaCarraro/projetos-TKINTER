import ttkbootstrap as tk
import tkinter.messagebox

class Login():

    def __init__(self):
        self.janela = tk.Window(themename="minty")
        self.janela.title = ("Lista De Afazeres")
        self.janela.configure(bg="")
        self.janela.geometry("800x500") 
        self.janela.resizable(False, False)

        self.label_titulo = tk.Label(self.janela,
                        text="Pagina de Login!",
                        background="",
                        font="Arial",
                        foreground="")
        self.label_titulo.pack(pady=20)

        self.caixa_login1 = tk.Label(self.janela,
                                    text ="Digite seu Login",
                                    font=("Arial"))
        self.caixa_login1.pack()

        self.caixa_login2 = tk.Entry(font=("Arial", 18))
        self.caixa_login2.pack(pady=20)

        self.caixa_senha1 = tk.Label(self.janela,
                                    text="Digite sua Senha",
                                    font=("Arial"))
                                
        self.caixa_senha1.pack()

        self.caixa_senha2 = tk.Entry(show="*",
                                    font= ("Arial", 18))
        
        
        self.caixa_senha2.pack(pady= 20)
        
        frame_botao = tk.Frame()
        frame_botao.pack()

        tk.Button(frame_botao, text = "Login", command=self.logar, padding=(10)).pack(side="left",padx=10)
        tk.Button(frame_botao, text = "Sair", command=self.sair padding=(10), bootstyle = "danger").pack(side="right",pady=10)

    def logar (self):
            usuario_senha = (self.caixa_senha2.get())
            usuario_nome = (self.caixa_login2.get())

            if usuario_nome == "Nathalya" and usuario_senha == "Nathalya123":
                tkinter.messagebox.showinfo(title= "Login realizado com sucesso", message= "Login-aceito")
            else:
                 tkinter.messagebox.showerror(title="ERRO", message="Senha inválida")

    def run (self):
        self.janela.mainloop()

    def sair (self):
         

if __name__ == "__main__":
        janela = Login()
        janela.run()