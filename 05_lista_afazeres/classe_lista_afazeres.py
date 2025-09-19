import ttkbootstrap as tk


class Lista_Tarefa():

    def __init__(self):
        self.janela = tk.Window(themename="minty")
        self.janela.title = ("Lista De Afazeres")
        self.janela.configure(bg="")
        self.janela.geometry("800x500") 
        self.janela.resizable(False, False)

        self.label_titulo = tk.Label(self.janela,
                        text="Minhs Lista de Tarefas",
                        background="",
                        font="Arial",
                        foreground="")
        self.label_titulo.pack(pady=20)

    def run (self):
        self.janela.mainloop()

if __name__ == "__main__":
    janela = Lista_Tarefa()
    janela.run()