import google.generativeai as genai

class Gemini_Bot:
    """Classe responsável por gerenciar o modelo do Gemini."""
    
    def __init__(self):
        genai.configure(api_key=" AIzaSyAqylEfukRImxev0EAolWeMNmW1URQK9lQ")
        
        instrucao_sistema = """Meu nome é Dr. Boa noite Cinderela. Sou um pesquisador do sono com mais de duas décadas de experiência.
          Minha função é fornecer informações detalhadas e especializadas, sempre com foco total no universo do sono e seus mistérios.
          Caso sua pergunta se desvie desse tema, farei o possível para guiá-lo de volta à nossa área de estudo,
          pois meu conhecimento é restrito a essa disciplina."""
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()

    def enviar_mensagem(self, mensagem: str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        response = self.chat.send_message(mensagem)
        return response.text
    
#Este if so será executado se eu rodar o arquivo diretamente
#Caso eu import essa parte não será executada
#Podendo utilizar isto para testes

if __name__ == "__main__":
    robo = Gemini_Bot()
    resposta = robo.enviar_mensagem("Quantas horas por dia devo dormir?")
    print(resposta)

