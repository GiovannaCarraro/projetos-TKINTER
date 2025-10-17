import ttkbootstrap as tk
import tkinter.messagebox


class Login():

    def __init__(self, janela_pai):
        self.janela = tk.Toplevel(janela_pai)
        self.janela.title = ("Lista De Afazeres")
        self.janela.configure(bg="")
        self.janela.geometry("800x500") 
        self.janela.resizable(False, False)

        self.label_titulo = tk.Label(self.janela,
                        text="L O G I N",
                        background="",
                        font="Arial",
                        foreground="")
        self.label_titulo.pack(pady=20)

        self.caixa_login1 = tk.Label(self.janela,
                                    text ="Digite seu Login",
                                    font=("Arial"))
        self.caixa_login1.pack()

        self.caixa_login2 = tk.Entry(self.janela, font=("Arial", 18))
        self.caixa_login2.pack(pady=20)                                                                     

        self.caixa_senha1 = tk.Label(self.janela,
                                    text="Digite sua Senha",
                                    font=("Arial"))
                                
        self.caixa_senha1.pack()

        self.caixa_senha2 = tk.Entry(self.janela, show="*",
                                    font= ("Arial", 18))
        
        
        self.caixa_senha2.pack(pady= 20)
        
        frame_botao = tk.Frame(self.janela)
        frame_botao.pack()

        tk.Button(frame_botao, text = "Login", command=self.logar, padding=(10)).pack(side="left",padx=10)
        tk.Button(frame_botao, text = "Sair", command=self.sair, padding=(10), bootstyle = "danger").pack(side="right",pady=10)

    def logar (self):
            usuario_senha = (self.caixa_senha2.get())
            usuario_nome = (self.caixa_login2.get())

            if usuario_nome == "123" and usuario_senha == "123":
                #tkinter.messagebox.showinfo(title= "LOGIN", message= "Login realizado com sucesso")
                self.janela.destroy()
                # janela = Lista_Tarefa()
                # janela.run()
               

            else:
                 tkinter.messagebox.showerror(title="ERRO", message="Senha inválida")

    def run (self):
        self.janela.mainloop()

    def sair (self):
        resposta = tkinter.messagebox.askyesno(title="LOGIN", message= "Você deseja sair?")
        if resposta == True:
            exit()

if __name__ == "__main__":
        janela = Login()
        janela.run()