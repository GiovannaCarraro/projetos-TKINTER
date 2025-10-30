import ttkbootstrap as ttk

janela = ttk.Window(themename="minty")
janela.geometry("800x500")

treeview = ttk.Treeview(janela)
treeview.pack()

treeview["columns"] = ("nome", "idade", "cidade")
treeview["show"] = "headings"

treeview.heading("nome", text="Nome")
treeview.heading("idade", text="Idade")
treeview.heading("cidade", text="Cidade")

treeview.column("idade", width=100, anchor= "center")
treeview.column("nome", width=100, anchor= "center")
treeview.column("cidade", width=100, anchor= "center")


treeview.insert("", "end", values =["Giovanna", "16", "Araraquara"])

janela.mainloop()