import ttkbootstrap as tk
import tkinter.messagebox
 
class Calculadora():

    def __init__ (self):
        self.janela = tk.Window(themename="minty")
        self.janela.title("Calculadora-IMC")
        self.janela.configure(bg="lightpink")
        self.janela.geometry("800x500")
        self.janela.resizable(False,False)


        self.label_titulo = tk.Label(self.janela,
                        text="Calculadora IMC!",
                        background="",
                        font="Arial",
                        foreground="pink")
        self.label_titulo.pack()

        self.label_peso = tk.Label(self.janela,
                    text="Digite seu peso")
        self.label_peso.pack(pady=20)

        self.caixa_peso = tk.Entry(self.janela,
                font=("Arial", 18))
        self.caixa_peso.pack(pady=5)

        self.label_altura = tk.Label(self.janela,
                    text="Digite sua altura")
        self.label_altura.pack(pady=20)

        self.caixa_altura = tk.Entry(self.janela,
                font=("Arial", 18))
        self.caixa_altura.pack(pady=5)

        self.button_resposta = tk.Button(self.janela,
                            text="Calcular",
                            command=self.calc
                            )
        self.button_resposta.pack(pady=15)

        self.vazio = tk.Label(text = "")
        self.vazio.pack()
        
    def calc (self):
        try:
            peso = float(self.caixa_peso.get())
            altura = float(self.caixa_altura.get())

            altura = altura / 100
            imc =  peso / (altura ** 2)
        except:
            tkinter.messagebox.showerror(title="ERRO", message="Você digitou um valor invalido")
            
        self.vazio.configure(text=f"Seu IMC é: {imc:.2f}")
            
            
        if imc < 18.5:
           self.vazio.configure(text= "abaixo do peso")     
        elif 18.5 <= imc < 24.9:
            self.vazio.configure(text = "peso normal")   
        elif 25 <= imc < 29.9:
            self.vazio.configure(text= "excesso de peso")
                      
        self.vazio.configure(text= imc)

    def run (self):
        self.janela.mainloop()

if __name__ == "__main__":
        janela = Calculadora()
        janela.run()

        