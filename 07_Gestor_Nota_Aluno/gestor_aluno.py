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

        #Botões desafio extra
        ttk.Button(frame_botao, text="Ver Notas", command=self.adicionar_nota, bootstyle="primary").pack(side='left', padx=15)
        ttk.Button(frame_botao, text="Adicionar Nota", command=self.janela_notas, bootstyle="info").pack(side='left', padx=15)

        ttk.Label(self.janela, text="Gerenciamento de Alunos",
                font=("Arial", 18, )).pack(pady=10)

        # Treeview tabela
        self.treeview = ttk.Treeview(self.janela)
        self.treeview.pack()

        self.treeview["columns"] = ("nome", "turma", "email")
        self.treeview["show"] = "headings"

        self.treeview.heading("nome", text="Nome")
        self.treeview.heading("turma", text="Turma")
        self.treeview.heading("email", text="Email")

        self.treeview.column("nome", width=200, anchor= "center")
        self.treeview.column("turma", width=200, anchor= "center")
        self.treeview.column("email", width=200, anchor= "center")


        # Muda o tamanho (aprendi isso hj)
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

        # Tabela 2
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        disciplina TEXT NOT NULL,
        nota INT NOT NULL,
        FOREIGN KEY (aluno_id) REFERENCES alunos (id)
        )
        """)
        conexao.commit()
        conexao.close()

        # NOVO: Título e Treeview de Notas
        ttk.Label(self.janela, text="Notas do Aluno Selecionado",
                  font=("Arial", 18, )).pack(pady=10)

        self.treeview_notas = ttk.Treeview(self.janela)
        self.treeview_notas.pack()

        self.treeview_notas["columns"] = ("ID_Nota", "Disciplina", "Nota")
        self.treeview_notas["show"] = "headings"

        self.treeview_notas.heading("ID_Nota", text="ID")
        self.treeview_notas.heading("Disciplina", text="Disciplina")
        self.treeview_notas.heading("Nota", text="Nota")

        self.treeview_notas.column("ID_Nota", width=100, anchor="center")
        self.treeview_notas.column("Disciplina", width=300, anchor="w")
        self.treeview_notas.column("Nota", width=100, anchor="center")
        
        self.att_lista()

    def att_lista (self):
        # Limpa o treeview antes de preencher
        for item in self.treeview.get_children():
            self.treeview.delete(item)


        #Limpa a lista de notas ao recarregar
        for item in self.treeview_notas.get_children():
            self.treeview_notas.delete(item)
        
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
        
        if not item_selecionado:
            messagebox.showinfo("Atenção", "Selecione um aluno para excluir!")
            return
        
        # O id é o id interno do item selecionado, que é o id do aluno no banco de dados
        aluno_id = item_selecionado[0] 
        nome_aluno = self.treeview.item(aluno_id, "values")[0] 
        
        confirmar = messagebox.showinfo("Confirmação", f"Tem certeza que deseja excluir o aluno '{nome_aluno}' e todas as suas notas?")
        
        if confirmar:
            conexao = sqlite3.connect("alunos.db")
            cursor = conexao.cursor()
            
            # Exclui as notas primeiro 
            cursor.execute("""DELETE FROM notas
                            WHERE aluno_id = ?""",
                            (aluno_id,))
            
            # Exclui o aluno
            cursor.execute("""DELETE FROM alunos 
                            WHERE id = ?""",
                            (aluno_id,))
            
            conexao.commit()
            conexao.close()
            
            messagebox.showinfo("Sucesso", f"Aluno '{nome_aluno}' excluído com sucesso!")


            self.att_lista()

    def limpar_notas(self):
        # Limpa a Treeview de Notas
        for item in self.treeview_notas.get_children():
            self.treeview_notas.delete(item)

    def carregar_notas(self, aluno_id):
        self.limpar_notas()
            
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        
        sql_select = """SELECT id, disciplina, nota 
                        FROM notas
                        WHERE aluno_id = ?"""

        cursor.execute(sql_select, (aluno_id,))
        notas = cursor.fetchall()
        conexao.close()
        
        for nota in notas:
            self.treeview_notas.insert('', 'end', values=nota)

    def notas_selecionadas(self, valores):
        
        selecao = self.treeview.selection()
        
        if selecao:
            aluno_id = selecao[0] 
                    
            self.carregar_notas(aluno_id)
                      
            # Índices 0, 1, 2 corresponde a nome, turma, email do att lista
            self.entrada_nome.insert(0, valores[0])
            self.entrada_turma.insert(0, valores[1])
            self.entrada_email.insert(0, valores[2])
                    
        else:
            messagebox.showinfo("Atenção", "Selecione um aluno na lista para ver suas notas.")

            self.limpar_notas() 

    def janela_notas(self):
        
        selecao = self.treeview.selection()
        if not selecao:
            messagebox.showinfo("Atenção", "Selecione um aluno para adicionar notas.")
            return 

        selecao = self.treeview.selection()

        if not selecao:
            messagebox.showinfo("Atenção", "Selecione um aluno para adicionar notas.")
            return

        aluno_id = selecao[0] # ID do aluno
        aluno_nome = self.treeview.item(selecao[0], 'values')[0] # Nome
        
        janela_nota = (self.janela)
        janela_nota.title(f"Adicionar Nota: {aluno_nome}")
        janela_nota.geometry("400x250")
        janela_nota.transient(self.janela)

        ttk.Label(janela_nota, text=f"Adicionar Nota para {aluno_nome}", font=("Arial", 14)).pack(pady=10)
        
        # Entrada Disciplina
        ttk.Label(janela_nota, text="Disciplina:").pack(pady=2)
        entrada_disciplina = ttk.Entry(janela_nota)
        entrada_disciplina.pack(padx=20, fill='x')
        
        # Entrada Nota
        ttk.Label(janela_nota, text="Nota (Ex: 8.5):").pack(pady=2)
        entrada_nota = ttk.Entry(janela_nota)
        entrada_nota.pack(padx=20, fill='x')

    def adicionar_nota(self):
        disciplina = self.entrada_disciplina.get()
        nota= self.entrada_nota.get()
            
        if not disciplina:
            messagebox.showerror("Erro", "Preencha a disciplina.")
            return

        try:
            conexao = sqlite3.connect("alunos.db")
            cursor = conexao.cursor()
            cursor.execute("""INSERT INTO notas 
                            (aluno_id, disciplina, nota)
                            VALUES (?, ?, ?)""", 
                            (self.aluno_id, disciplina, nota))

            conexao.commit()
            conexao.close()
                
            messagebox.showinfo("Sucesso", "Nota adicionada!")
            self.janela_nota.destroy()
            self.carregar_notas(self.aluno_id) # Atualiza a lista de notas
                
        except sqlite3.Error as e:
                messagebox.showerror("Erro DB", f"Erro ao adicionar nota: {e}")

        ttk.Button(self.janela_nota, text="Salvar Nota", command=self.adicionar_nota, bootstyle="success").pack(pady=15)

    def alterar_aluno(self):
        
        item_selecionado = self.treeview.selection()
        if not item_selecionado:
            messagebox.showinfo("Atenção", "Selecione um aluno na lista para alterar!")
            return
            
        id = item_selecionado[0]
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
            

