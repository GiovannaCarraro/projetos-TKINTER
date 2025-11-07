import ttkbootstrap as ttk
import sqlite3
from tkinter import messagebox, Toplevel  #O TopLevel serve para criar janela "filha" da janela principal

class Alunos:

    def __init__ (self):

        # Interface 
        self.janela = ttk.Window(themename="minty")
        self.janela.title("Gerenciador de Alunos")
        self.janela.geometry("1200x1000")
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

        ttk.Button(frame_botao, text="Adicionar", command=self.cadastrar_aluno, bootstyle="success").pack(side='left', padx=5) #Create
        ttk.Button(frame_botao, text="Alterar", command=self.alterar_aluno, bootstyle="warning").pack(side='left', padx=5) # Update
        ttk.Button(frame_botao, text="Excluir", command=self.excluir_aluno, bootstyle= "danger").pack(side='left', padx=5) # Delete

        #Botão desafio extra
        ttk.Button(frame_botao, text="Adicionar Nota", command=self.mostrar_cadastro_notas, bootstyle="info").pack(side='left', padx=15)

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

        # Faz o app att a lista de notas automaticamente quando clica em um aluno, ai deixa a interface mais bonitinha
        self.treeview.bind("<<TreeviewSelect>>", self.aluno_selecionado)

        # Muda o tamanho de comprimento (aprendi isso hj)
        ttk.Style().configure("Treeview", rowheight=30)

        # Adiciona uma nova linha no final do Treeview com três colunas, todas vazias
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

        # Tabela 2 desafio extra
        cursor.execute("""
       CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        disciplina TEXT NOT NULL,
        nota REAL NOT NULL,
        FOREIGN KEY (aluno_id) REFERENCES alunos (id)
)
        """)
        conexao.commit()
        conexao.close()

        #Treeview das notas
        self.treeview_notas = ttk.Treeview(self.janela)
        self.treeview_notas.pack()

        self.treeview_notas["columns"] = ("ID_Nota", "Disciplina", "Nota")
        self.treeview_notas["show"] = "headings"

        self.treeview_notas.heading("ID_Nota", text="ID")
        self.treeview_notas.heading("Disciplina", text="Disciplina")
        self.treeview_notas.heading("Nota", text="Nota")

        self.treeview_notas.column("ID_Nota", width=100, anchor="center")
        self.treeview_notas.column("Disciplina", width=300, anchor="center")
        self.treeview_notas.column("Nota", width=100, anchor="center")
        
        #Configura o tamanho comprimento
        ttk.Style().configure("Treeview", rowheight=25)
        
        self.att_lista()

    def cadastrar_aluno(self):
        
        # Pega os valores dos campos de entrada
            nome = self.entrada_nome.get()
            turma = self.entrada_turma.get()
            email = self.entrada_email.get()
            
            # Verifica se os campos estão preenchidos
            if not nome or not turma or not email:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
                return
                
            try:
                conexao = sqlite3.connect("alunos.db")
                cursor = conexao.cursor()

                # Insere o novo aluno
                cursor.execute("""INSERT INTO alunos 
                               (nome, turma, email)
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
        
        #prga TODOS os resultados
        alunos = cursor.fetchall()
        conexao.close()

        # Uma nova linha é adicionada no Treeview
        # Cada coluna da linha recebe os valores: nome, turma e email
        # A linha recebe um identificador (iid) igual ao id do aluno no banco de dados
        for aluno in alunos:
         self.treeview.insert("", "end", iid=str(aluno[0]), values=[aluno[1], aluno[2], aluno[3]])

    def mostrar_cadastro_notas(self):
        selecao = self.treeview.selection()
        
        if not selecao:
            messagebox.showinfo("Atenção", "Selecione um aluno na lista para adicionar notas.")
            return

        aluno_id = selecao[0]
        aluno_nome = self.treeview.item(aluno_id, 'values')[0] 

        # Cria nova janela "filha"
        self.janela_notas = ttk.Toplevel(self.janela)
        self.janela_notas.title(f"Adicionar Nota {aluno_nome}")
        self.janela_notas.geometry("400x300")
        self.janela_notas.resizable(False, False)

        ttk.Label(self.janela_notas,
                text=f"Adicionar Nota para {aluno_nome}", 
                font=("Arial", 18)).pack(pady=10)

        # Disciplina
        ttk.Label(self.janela_notas, text="Disciplina:").pack(pady=5)
        self.entrada_disciplina = ttk.Entry(self.janela_notas,
                                            font=("Arial", 18))
        
        self.entrada_disciplina.pack(pady=5)

        # Nota
        ttk.Label(self.janela_notas, text="Nota:").pack(pady=5)
        self.entrada_nota_valor = ttk.Entry(self.janela_notas,
                                            font=("Arial", 18))
        
        self.entrada_nota_valor.pack(pady=5)

        # Botão Salvar
        # A função lambda cria uma função anônima que só é executada quando o botão é clicado, e não no momento da criação
        ttk.Button(self.janela_notas, text="Salvar Nota", 
                   command=lambda: self.salvar_nota(aluno_id),
                   bootstyle="success").pack(pady=20)

        
    def salvar_nota(self, aluno_id):
        # Pega as info de disciplna e nota
        disciplina = self.entrada_disciplina.get()
        nota = self.entrada_nota_valor.get()

        # Validação
        if not disciplina or not nota:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        
        # Replace: substitui todas as vírgulas , por ponto . dentro de nota.
        try:
            nota = float(nota.replace(',', '.'))
        except:
            messagebox.showerror("Erro", "A nota deve ser um número válido.")
            return
        
        #Insere
        try:
            conexao = sqlite3.connect("alunos.db")
            cursor = conexao.cursor()
            cursor.execute("""INSERT INTO notas 
                           (aluno_id, disciplina, nota)
                            VALUES (?, ?, ?)""",
                           (aluno_id, disciplina, nota))
            
            conexao.commit()
            conexao.close()

            messagebox.showinfo("Sucesso", "Nota adicionada com sucesso!")

            # Fecha a janela de notas e atualiza lista
            self.janela_notas.destroy()
            self.carregar_notas(aluno_id)

        except:
            messagebox.showerror("Erro", f"Erro ao adicionar nota")

    def excluir_aluno(self):
        # Pega os itens selecionados no Treeview
        item_selecionado = self.treeview.selection()
        
        # Verifica
        if not item_selecionado:
            messagebox.showinfo("Atenção", "Selecione um aluno para excluir!")
            return
        
        # Pega o ID do primeiro item selecionado
        aluno_id = item_selecionado[0] 
        nome_aluno = self.treeview.item(aluno_id, "values")[0] 
        

        confirmar = messagebox.showinfo("Confirmação", f"Tem certeza que deseja excluir o aluno '{nome_aluno}' e todas as suas notas?")
        
        if confirmar:
            conexao = sqlite3.connect("alunos.db")
            cursor = conexao.cursor()
            # Deleta todas as notas do aluno no banco, usando aluno_id como referência
            cursor.execute("""DELETE FROM notas 
                           WHERE aluno_id = ?""", 
                           (aluno_id,))
            
            # Deleta o registro do aluno na tabela alunos
            cursor.execute("""DELETE FROM alunos
                            WHERE id = ?""", 
                            (aluno_id,))
            
            conexao.commit()
            conexao.close()
            
            messagebox.showinfo("Sucesso", f"Aluno '{nome_aluno}' excluído com sucesso!")

            # Limpar campos após exclusão
            self.entrada_nome.delete(0, 'end')
            self.entrada_turma.delete(0, 'end')
            self.entrada_email.delete(0, 'end')
            
            self.att_lista()

    def limpar_notas(self):
        # Essa função apaga todas as linhas do treeview, limpa completamente a tabela de notas na interface
        for item in self.treeview_notas.get_children():
            self.treeview_notas.delete(item)

    def aluno_selecionado(self, event):
        # Retorna uma tupla de ids das linhas selecionadas
        selecao = self.treeview.selection()
        if not selecao:
            self.limpar_notas()
            return

        aluno_id = selecao[0]
        self.carregar_notas(aluno_id)

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

    def cadastro_notas(self):
       
        selecao = self.treeview.selection()
        
        if not selecao:
            messagebox.showinfo("Atenção", "Selecione um aluno na lista para adicionar notas.")
            return

        aluno_id = selecao[0]
        aluno_nome = self.treeview.item(aluno_id, 'values')[0] 

        # Cria nova janela
        self.janela_notas = ttk.Toplevel(self.janela)
        self.janela_notas.title(f"Adicionar Nota - {aluno_nome}")
        self.janela_notas.geometry("400x300")
        self.janela_notas.resizable(False, False)

        ttk.Label(self.janela_notas, text=f"Adicionar Nota para {aluno_nome}", 
                  font=("Arial", 16)).pack(pady=10)

        # Campo Disciplina
        ttk.Label(self.janela_notas, text="Disciplina:").pack(pady=5)
        self.entrada_disciplina = ttk.Entry(self.janela_notas, font=("Arial", 14))
        self.entrada_disciplina.pack(pady=5)

        # Campo Nota
        ttk.Label(self.janela_notas, text="Nota:").pack(pady=5)
        self.entrada_nota_valor = ttk.Entry(self.janela_notas, font=("Arial", 14))
        self.entrada_nota_valor.pack(pady=5)

        # Botão Salvar
        ttk.Button(self.janela_notas, text="Salvar Nota", 
                   command=lambda: self.salvar_nova_nota(aluno_id),
                   bootstyle="success").pack(pady=20)

        self.carregar_notas(aluno_id) # Atualiza a lista de notas
            

    def visualizar_notas(self): 
        selecao = self.treeview.selection()
        
        if not selecao:
            messagebox.showinfo("Atenção", "Selecione um aluno na lista para ver suas notas.")
            self.limpar_notas() 
            return
        
        aluno_id = selecao[0] 
        valores = self.treeview.item(aluno_id, 'values')
        
        # Carrega as notas
        self.carregar_notas(aluno_id)
        
        # Carrega os dados do aluno nos campos de entrada
        self.entrada_nome.delete(0, 'end')
        self.entrada_turma.delete(0, 'end')
        self.entrada_email.delete(0, 'end')

        self.entrada_nome.insert(0, valores[0])
        self.entrada_turma.insert(0, valores[1])
        self.entrada_email.insert(0, valores[2])

    def nota_selecionada(self, event):
        selecao = self.treeview_notas.selection()
        if not selecao:
            return

        nota_id = selecao[0]
        valores = self.treeview_notas.item(nota_id, 'values')

        self.entrada_disciplina.delete(0, 'end')
        self.entrada_disciplina.insert(0, valores[1])  # Disciplina

        self.entrada_nota_valor.delete(0, 'end')
        self.entrada_nota_valor.insert(0, valores[2])  # Nota

    def alterar_nota(self):
        # Pega a nota selecionada
        selecao_nota = self.treeview_notas.selection()
        if not selecao_nota:
            messagebox.showinfo("Atenção", "Selecione uma nota para alterar.")
            return

        nota_id = selecao_nota[0]
        disciplina = self.entrada_disciplina.get()
        nota = self.entrada_nota_valor.get()

        if not disciplina or not nota:
            messagebox.showerror("Erro", "Preencha todos os campos para alterar a nota.")
            return

        try:
            nota = float(nota.replace(',', '.'))
        except:
            messagebox.showerror("Erro", "A nota deve ser um número válido.")
            return

        try:
            conexao = sqlite3.connect("alunos.db")
            cursor = conexao.cursor()
            cursor.execute("""
                UPDATE notas
                SET disciplina = ?, nota = ?
                WHERE id = ?
            """, (disciplina, nota, nota_id))
            conexao.commit()
            conexao.close()

            messagebox.showinfo("Sucesso", "Nota alterada com sucesso!")
            self.carregar_notas(self.treeview.selection()[0])  # Atualiza lista de notas

        except:
            messagebox.showerror("Erro", f"Erro ao alterar nota")

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
            

