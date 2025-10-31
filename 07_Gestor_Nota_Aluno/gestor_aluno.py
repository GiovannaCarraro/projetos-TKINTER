import ttkbootstrap as ttk
import sqlite3
from tkinter import messagebox

# Interface 
janela = ttk.Window(themename="minty")
janela.title("Gerenciador de Alunos")
janela.geometry("900x800")
janela.resizable(False, False)

# Título
ttk.Label(janela, text="Dados Alunos",
          font=("Arial", 18, )).pack(pady=10)

entrada_nome = ttk.Label(janela,
                         text="Nome").pack()

entrada_nome = ttk.Entry(janela,
                         font=("Arial", 18)).pack()

entrada_turma = ttk.Label(janela,
                         text="Turma").pack()

entrada_turma = ttk.Entry(janela,
                         font=("Arial", 18)).pack()

entrada_email = ttk.Label(janela,
                         text="Email").pack()

entrada_email = ttk.Entry(janela,
                         font=("Arial", 18)).pack(pady=10)


frame_botao = ttk.Frame(janela)
frame_botao.pack()

ttk.Button(frame_botao,  text = "Adicionar").pack(pady=5) #Adicionar
ttk.Button(frame_botao,  text = "Excluir").pack(pady=5) #Excluir
ttk.Button(frame_botao,  text = "Alterar").pack(pady=5) #Alterar

ttk.Label(janela, text="Gerenciamento de Alunos",
          font=("Arial", 18, )).pack(pady=10)

treeview = ttk.Treeview(janela)
treeview.pack()

treeview["columns"] = ("nome", "idade", "email")
treeview["show"] = "headings"

treeview.heading("nome", text="Nome")
treeview.heading("idade", text="Idade")
treeview.heading("email", text="Email")

treeview.column("idade", width=100, anchor= "center")
treeview.column("nome", width=100, anchor= "center")
treeview.column("email", width=100, anchor= "center")

treeview.insert("", "end", values =["", "", ""])

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

def atualizar_lista():
    # Limpa o treeview antes de preencher
    for item in treeview.get_children():
        treeview.delete(item)
    
    conexao = sqlite3.connect("alunos.db")
    cursor = conexao.cursor()
    # Pega todos os dados da tabela
    cursor.execute("""SELECT id, nome, turma, email
                FROM alunos 
                ORDER BY id DESC""")
    
    alunos = cursor.fetchall()
    conexao.close()

    for aluno in alunos:
        treeview.insert("", "end", 
                        id=aluno[0], values=[aluno[1], aluno[2], aluno[3]])

def cadastrar_aluno():
    
    # Pega os valores dos campos de entrada
        nome = entrada_nome.get()
        turma = entrada_turma.get()
        email = entrada_email.get()
        
        # Verifica se os campos estão preenchidos
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
            
            # Limpa os campos após o cadastro
            entrada_nome.delete(0, 'end')
            entrada_turma.delete(0, 'end')
            entrada_email.delete(0, 'end')
            
            # Atualiza a lista para mostrar o novo aluno
            atualizar_lista()
            
        except:
            messagebox.showerror("Erro!", "Ocorreu um erro ao tentar cadastrar um aluno.")

def excluir_aluno():
   
    item_selecionado = treeview.selection()
    
    # Verifica se algum item foi selecionado
    if not item_selecionado:
        messagebox.showinfo("Atenção", "Selecione um aluno para excluir!")
        return
    
    aluno_id = item_selecionado[0] 
    
    nome_aluno = treeview.item(aluno_id, "values")[0] 
    
    # Confirmação de exclusão
    confirmar = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o aluno '{nome_aluno}'?")
    
    if confirmar:
    
            conexao = sqlite3.connect("alunos.db")
            cursor = conexao.cursor()
            cursor.execute("""DELETE FROM alunos
                            WHERE id = ?""", (aluno_id,))
            conexao.commit()
            conexao.close()
            
            messagebox.showinfo("Sucesso", f"Aluno '{nome_aluno}' excluído com sucesso!")
            atualizar_lista()

def alterar_aluno():
    
    item_selecionado = treeview.selection()
    if not item_selecionado:
        messagebox.showinfo("Atenção", "Selecione um aluno na lista para alterar!")
        return
        
    aluno_id = item_selecionado 
    nome = entrada_nome.get()
    turma = entrada_turma.get()
    email = entrada_email.get()
    
    if not nome or not turma or not email:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos para alterar!")
        return
        
    conexao = sqlite3.connect("alunos.db")
    cursor = conexao.cursor()
    cursor.execute("""UPDATE alunos 
                   SET nome = ?, turma = ?, email = ? 
                   WHERE id = ?""", 
                (nome, turma, email, aluno_id))
    conexao.commit()
    conexao.close()
        
    messagebox.showinfo("Sucesso", "Dados do aluno alterados com sucesso!")
        
    # Limpa os campos após a alteração
    entrada_nome.delete(0, 'end')
    entrada_turma.delete(0, 'end')
    entrada_email.delete(0, 'end')
        
    atualizar_lista()
           

janela.mainloop()
