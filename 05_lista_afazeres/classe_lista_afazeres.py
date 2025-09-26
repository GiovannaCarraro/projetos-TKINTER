import ttkbootstrap as tk
from tkinter import Listbox, END

class Lista_Tarefa():

    def __init__(self):
        self.janela = tk.Window(themename="minty")
        self.janela.title = ("Lista De Afazeres")
        self.janela.configure(bg="")
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

        botao_marcar = tk.Button(frame_botao, text="Marcar como concluido")
        botao_marcar.pack(side="right")

    def adicionar (self):
        tarefa = self.add_tarefa.get()
        #inserindo a tarefa na lista
        self.lista.insert(END, tarefa) #END: CONSTNATE: variavel fixa

    def excluir(self):
        selecionar = self.lista.curselection()
        self.lista.delete(selecionar[0])  

    def run (self):
        self.janela.mainloop()

if __name__ == "__main__":
    janela = Lista_Tarefa()
    janela.run()