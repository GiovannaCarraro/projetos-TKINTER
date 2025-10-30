import ttkbootstrap as ttk
import sqlite3
from tkinter import messagebox

#Interface 
janela = ttk.Window(themename="minty")
janela.title("Gerenciador de Alunos")
janela.geometry("800x500")
janela.resizable(False, False)

# Título
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
#Bd
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

    conexao = sqlite3.connect("alunos.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    for linha in cursor.fetchall():
        tabela.insert("", "end", values=linha)
    conexao.close()


janela.mainloop()

