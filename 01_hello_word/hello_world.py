import tkinter as tk

#criando uma janela
janela = tk.Tk()
janela.title("Hello world")

janela.configure(bg="lightblue")
janela.iconbitmap("01_hello_word/sun.ico")
janela.geometry("800x500")
janela.resizable(False,False)

#Criando os widgets
label_titulo = tk.Label(janela,
                        text="Hello world!",
                        bg="lightblue",
                        font="Arial",
                        foreground="green")
label_titulo.pack()

#texto digite seu nome
label_nome = tk.Label(janela,
                      text="Digite seu nome")
label_nome.pack()

#caixa de texto para digitar o nome
caixa = tk.Entry(janela,
                font=("Arial", 18))
caixa.pack(pady=10)

#função do botão
def desejar_bomdia():
    """Esta função serve para pegar o nome digitado na caixa de texto e desejar um bom dia"""
    nome = caixa.get()
    label_resultado.configure(text=f"Bom dia, {nome}")

#Botão para o progroma falar bom dia
button_bomdia = tk.Button(janela,
                          text="Desejar Bom dia",
                          command=desejar_bomdia)
button_bomdia.pack()

#label bom dia
label_resultado = tk.Label(janela,
                         text= "",
                         font= ("Arial", 20),
                         foreground= "black")
label_resultado.pack()

#loop para manter a janela aberta
janela.mainloop()