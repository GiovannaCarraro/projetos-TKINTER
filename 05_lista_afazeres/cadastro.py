import ttkbootstrap as tk
import tkinter.messagebox
import sqlite3
import tkinter.messagebox



class Cadastro():
    def __init__(self, janela_pai):

        self.janela = tk.Toplevel(janela_pai)
        self.janela.title  ("Painel de Cadastro")
        self.janela.configure(bg="")
        self.janela.geometry("800x500") 
        self.janela.resizable(False, False)

        self.label_titulo = tk.Label(self.janela,
                        text="Painel de Cadastro",
                        background="",
                        font="Arial",
                        foreground="")
        self.label_titulo.pack(pady=20)

        self.caixa_senha3 = tk.Label(self.janela,
                                    text="Digite seu nome completo",
                                    font=("Arial"))
        self.caixa_senha3.pack()

        self.caixa_login3 = tk.Entry(self.janela, font=("Arial", 18))
        self.caixa_login3.pack(pady=10)

        self.caixa_senha = tk.Label(self.janela,
                                    text="Digite seu nome de usuario",
                                    font=("Arial"))
        self.caixa_senha.pack()

        self.caixa_login1 = tk.Entry(self.janela, font=("Arial", 18))
        self.caixa_login1.pack(pady=10)

        self.caixa_senha2 = tk.Label(self.janela,
                                    text= "Digite sua senha",
                                    font=("Arial"))
        self.caixa_senha2.pack(pady=10)
        
        self.caixa_senha2 = tk.Entry(self.janela, show="*",
                                    font= ("Arial", 18))
        self.caixa_senha2.pack()         
        
        frame_botao = tk.Frame(self.janela)
        frame_botao.pack()

        
        tk.Button(frame_botao, text = "Cadastrar", command=self.inserir, padding=(10), bootstyle = "danger").pack(side="right",pady=10)
        

        self.criar_tabela()


        
    def cadastro (self):
        
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

       

    def criar_tabela(self):
        #conectando um banco de dados
        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
        #criar cursor
        cursor = conexao.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuario (
                nome varchar(80),
                senha varchar(20),
                usuario varchar(20) PRIMARY KEY)
                    """)
        conexao.commit()

        #Fechar a conexão
        cursor.close()
        conexao.close()

    def inserir(self):
        try:
            conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
            cursor = conexao.cursor()

            nome = self.caixa_login3.get()
            usuario = self.caixa_login1.get()
            senha = self.caixa_senha2.get()

            cursor.execute("""INSERT INTO usuario
                                (nome,
                                usuario,
                                senha)
                                VALUES (?,
                                        ?,
                                        ?);
                        """,
                        (nome, 
                            usuario,
                            senha))
            conexao.commit()

            cursor.close()
            conexao.close()
            cursor.execute(
                """SELECT nome, usuario FROM usuario
                    WHERE usuario = ? AND senha = ?;
                    """,
                    [usuario, senha]
            )

            tkinter.messagebox.showinfo("Cadastrado", "cadastrado com sucesso!")

        except:
            tkinter.messagebox.showerror("Erro", "Erro ao se cadastrar!")
            conexao.close()


    def run (self):
        self.janela.mainloop()

