import ttkbootstrap as ttk
import sqlite3
from tkinter import messagebox 

class Alunos:

    def __init__ (self):

        # Interface 
        self.janela = ttk.Window(themename="minty")
        self.janela.title("Gerenciador de Alunos")
        self.janela.geometry("900x800")
        self.janela.resizable(False, False)

        # Título
        ttk.Label(self.janela, text="Dados Alunos",
                font=("Arial", 18, )).pack(pady=10)
        
        # Entrys para o nome, turma e email
        ttk.Label(self.janela,
                   text="Nome").pack() 
        
        self.entrada_nome = ttk.Entry(self.janela,
                                    font=("Arial", 18))
        self.entrada_nome.pack()

        ttk.Label(self.janela,
                   text="Turma").pack()
         
        self.entrada_turma = ttk.Entry(self.janela,
                                    font=("Arial", 18))
        self.entrada_turma.pack()

        ttk.Label(self.janela,
                   text="Email").pack() 
        
        self.entrada_email = ttk.Entry(self.janela,
                                    font=("Arial", 18))
        self.entrada_email.pack(pady=10)

        # Botões
        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack()

        ttk.Button(frame_botao, text="Adicionar", command=self.cadastrar_aluno, bootstyle="sucess").pack(side='left', padx=5) #Create
        ttk.Button(frame_botao, text="Alterar", command=self.alterar_aluno, bootstyle="warning").pack(side='left', padx=5) # Update
        ttk.Button(frame_botao, text="Excluir", command=self.excluir_aluno, bootstyle= "danger").pack(side='left', padx=5) # Delete

        ttk.Label(self.janela, text="Gerenciamento de Alunos",
                font=("Arial", 18, )).pack(pady=10)

        # Treeview tabela
        self.treeview = ttk.Treeview(self.janela)
        self.treeview.pack()

        self.treeview["columns"] = ("nome", "idade", "email")
        self.treeview["show"] = "headings"

        self.treeview.heading("nome", text="Nome")
        self.treeview.heading("idade", text="Idade")
        self.treeview.heading("email", text="Email")

        self.treeview.column("idade", width=200, anchor= "center")
        self.treeview.column("nome", width=200, anchor= "center")
        self.treeview.column("email", width=200, anchor= "center")

        ttk.Style().configure("Treeview", rowheight=40)

        self.treeview.insert("", "end", values =["", "", ""])

        # Bd
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            turma TEXT NOT NULL,
            email TEXT NOT NULL  
        )
        """)
        conexao.commit()
        conexao.close()
        
        self.att_lista()

    def att_lista (self):
        # Limpa o treeview antes de preencher
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        # Pega todos os dados da tabela
        cursor.execute("""SELECT id, nome, turma, email
                    FROM alunos 
                    ORDER BY id DESC""")
        
        alunos = cursor.fetchall()
        conexao.close()

        for aluno in alunos:
            self.treeview.insert("", "end", 
                            id=aluno[0], values=[aluno[1], aluno[2], aluno[3]])

    def cadastrar_aluno(self):
        
        #Pega os valores dos campos de entrada
            nome = self.entrada_nome.get()
            turma = self.entrada_turma.get()
            email = self.entrada_email.get()
            
            #Verifica se os campos estão preenchidos
            if not nome or not turma or not email:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
                return
                
            try:
                conexao = sqlite3.connect("alunos.db")
                cursor = conexao.cursor()
                # Insere o novo aluno
                cursor.execute("""INSERT INTO alunos (nome, turma, email)
                                VALUES (?, ?, ?)""", 
                                (nome, turma, email))
                conexao.commit()
                conexao.close()
                
                messagebox.showinfo("Sucesso!", "Aluno cadastrado com sucesso!")
                
                # Limpa os campos dps do cadastro
                self.entrada_nome.delete(0, 'end')
                self.entrada_turma.delete(0, 'end')
                self.entrada_email.delete(0, 'end')
                
                # Att a lista para mostrar o novo aluno
                self.att_lista()
                
            except:
                messagebox.showerror("Erro!", "Ocorreu um erro ao tentar cadastrar um aluno.")

    def excluir_aluno(self):
    
        item_selecionado = self.treeview.selection()
        
        # Verifica se algum item foi selecionado
        if not item_selecionado:
            messagebox.showinfo("Atenção", "Selecione um aluno para excluir!")
            return
        
        id = item_selecionado[0] 
        
        nome_aluno = self.treeview.item(id, "values")[0] 
        
        # Confirmação de exclusão
        confirmar = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o aluno '{nome_aluno}'?")
        
        if confirmar:
        
                conexao = sqlite3.connect("alunos.db")
                cursor = conexao.cursor()
                cursor.execute("""DELETE FROM alunos
                                WHERE id = ?""", (id,))
                conexao.commit()
                conexao.close()
                
                messagebox.showinfo("Sucesso", f"Aluno '{nome_aluno}' excluído com sucesso!")
                self.att_lista()

    def alterar_aluno(self):
        
        item_selecionado = self.treeview.selection()
        if not item_selecionado:
            messagebox.showinfo("Atenção", "Selecione um aluno na lista para alterar!")
            return
            
        id = item_selecionado 
        nome = self.entrada_nome.get()
        turma = self.entrada_turma.get()
        email = self.entrada_email.get()
        
        if not nome or not turma or not email:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos para alterar!")
            return
            
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        cursor.execute("""UPDATE alunos 
                    SET nome = ?, turma = ?, email = ? 
                    WHERE id = ?""", 
                    (nome, turma, email, id))
        conexao.commit()
        conexao.close()
            
        messagebox.showinfo("Sucesso", "Dados do aluno alterados com sucesso!")
            
        # Limpa os campos após a alteração
        self.entrada_nome.delete(0, 'end')
        self.entrada_turma.delete(0, 'end')
        self.entrada_email.delete(0, 'end')
            
        self.att_lista()

    def run (self):
        self.janela.mainloop()

if __name__ == "__main__":
    janela = Alunos()
    janela.run()
            

