import ttkbootstrap as tk
import tkinter.messagebox
from cadastro import Cadastro
import sqlite3



class Login():

    def __init__(self, janela_pai):

        #Tranformando em atributo pra usar em qlqr função
        self.janela_pai = janela_pai
        

        self.janela = tk.Toplevel(janela_pai)
        self.janela.title = ("Lista De Afazeres")
        self.janela.configure(bg="")
        self.janela.geometry("800x500") 
        self.janela.resizable(False, False)

        #Config para q qnd feche a janela de login, ele encerre o programa
        self.janela.protocol("WM_DELETE_WINDOW", self.sair)

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

        tk.Button(self.janela,
                text="Cadastro",
                style = "Primary",
                command=self.abrir_tela_cadastro).pack()

       
    def logar (self):
            usuario_senha = (self.caixa_senha2.get())
            usuario_nome = (self.caixa_login2.get())

            conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
            cursor = conexao.cursor()
            cursor.execute(
                """SELECT nome, usuario FROM usuario
                    WHERE usuario = ? AND senha = ?;
                    """,
                    [usuario_nome, usuario_senha]
            )

            rstld = cursor.fetchone()
            conexao.close()


            #se o resultado for diferente de vazio, ou (if rsltd != None), ele encontrou algm c essa informação, eu abro a tela de lista de tarefas
            if rstld:
                tkinter.messagebox.showinfo(title="Login realizado com sucesso", message=f"Bem vinde, {rstld[0]}!")
                self.janela.destroy()
                self.janela.deiconify()

            else:
                 tkinter.messagebox.showerror(title="ERRO", message="Senha inválida")

                

    def run (self):
        self.janela.mainloop()

    def abrir_tela_cadastro(self):
        Cadastro(self.janela)
         

    def sair (self):
        resposta = tkinter.messagebox.askyesno(title="LOGIN", message= "Você deseja sair?")
        if resposta == True:
            exit()

if __name__ == "__main__":
        janela = Login()
        janela.run()