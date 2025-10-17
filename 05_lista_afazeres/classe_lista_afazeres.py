import ttkbootstrap as tk
from tkinter import Listbox, END
from tkinter import messagebox
from classe_login import Login
import sqlite3

class Lista_Tarefa():

    def __init__(self):

        self.janela = tk.Window(themename="minty")
        self.janela.title ("Lista De Afazeres")
        # self.janela.configure(bg="")
        self.janela.geometry("800x500") 
        self.janela.resizable(False, False)

        self.label_titulo = tk.Label(self.janela,
                        text="Lista de afazeres",
                        background="",
                        font="Arial",
                        foreground="")
        self.label_titulo.pack(pady=20)
        
       
        add_frame = tk.Frame()
        add_frame.pack(fill="x")

        self.add_tarefa = tk.Entry(add_frame) 
        self.add_tarefa.pack(side= "left", fill="x", expand= True)
        
        tk.Button(add_frame,
                   text= "Adicionar", command= self.adicionar).pack(side= "right")

        self.lista = Listbox(self.janela, font=("Arial", 12), height=10)
        self.lista.pack(pady=20, padx=10, fill="both", expand=True)

        frame_botao = tk.Frame(self.janela)
        frame_botao.pack(side="bottom", fill="x", expand=True, padx=20)

        botao_excluir = tk.Button(frame_botao, text="Excluir", command= self.excluir, bootstyle = "danger" )
        botao_excluir.pack(side="left")

        botao_marcar = tk.Button(frame_botao, command= self.marcar_como_concluida,
                                 text="Marcar como concluido")
        botao_marcar.pack(side="right")

        #conectando ao banco de dados
        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")

        #cursor = resp. por comandar o bd
        cursor = conexao.cursor()

        sql_para_criar_tabela = """
                CREATE TABLE IF NOT EXISTS tarefa (
                codigo integer primary key autoincrement,
                tarefa varchar(200)
                );
                                     """
        cursor.execute(sql_para_criar_tabela)

        #comitei as alterações
        conexao.commit()

        #fechei a conexão
        cursor.close()
        conexao.close()

        janela_login = Login(self.janela)
        
        self.atualizar()

        #escondendo a janela da lista tarefas
        self.janela.withdraw()

    def atualizar(self):
        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
        cursor = conexao.cursor()
        
        sql_select = """
                SELECT codigo,tarefa FROM tarefa;
                        """
        
        cursor.execute(sql_select)

        #fecthall lista de listas (retorna tudo)
        lista_afazeres = cursor.fetchall()

        cursor.close()
        conexao.close()

        #inserindo os itens 
        for linha in lista_afazeres:
            self.lista.insert("end", linha[1])

        

    def adicionar (self):
        tarefa = self.add_tarefa.get()
        #inserindo a tarefa na lista
        self.lista.insert(END, tarefa) #END: CONSTNATE: variavel fixa
         
        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
        cursor = conexao.cursor()

        sql_insert = """
                INSERT INTO tarefa (tarefa)
                VALUES (?)
                     """
        
        cursor.execute(sql_insert,[tarefa])

        conexao.commit()

        cursor.close()
        conexao.close()




    def excluir(self):
            selecionar = self.lista.curselection()
            if selecionar:
                self.lista.delete(selecionar[0])

            else:
             messagebox.showerror(message="selecione um item antes de excluir")

    def marcar_como_concluida(self):
        marcar = self.lista.curselection()
        if marcar:
            item = self.lista.get(marcar)
            self.lista.delete(marcar)
            self.lista.insert(marcar, item  + "                     concluido")
            self.lista.itemconfig(marcar, {"fg": "green", "selectbackground": "green"})
        else:
            messagebox.showerror("Aviso! selecione uma tarefa para concluir")
        

        if "concluido" not in item:
            with sqlite3.connect("./bd_lista_tarefa.sqlite") as conexao:
                texto_concluido = item +  "            concluido"
                cursor = conexao.cursor()

                sqlupdate = """
                            UPDATE tarefa
                            SET tarefa = ?
                            WHERE tarefa = ?
                            """
                valores = (texto_concluido, item)

                cursor.execute(sqlupdate, valores)
                
    
    def run (self):
        self.janela.mainloop()

if __name__ == "__main__":
    janela = Lista_Tarefa()
    janela.run()