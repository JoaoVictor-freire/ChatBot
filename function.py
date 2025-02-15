import os
from groq import Groq

class MathAssistant:
    def __init__(self, api_key):
        os.environ["GROQ_API_KEY"] = api_key
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.system_prompt = {
            "role": "system",
            "content": "Você é um agente assistente que auxilia crianças com questões de matemática. Você responde com respostas curtas."
        }
        self.chat_history = [self.system_prompt]
        self.last_problem = None  # Para armazenar o último problema resolvido

    def solve_problem(self, problem):
        """ Resolve um problema matemático e armazena para possível correção. """
        self.last_problem = problem  # Salvar o último problema resolvido

        prompt = f"Resolva o seguinte problema matemático, explicando todo o passo a passo de maneira bem resumida: {problem}."
        self.chat_history.append({"role": "user", "content": prompt})

        completion = self.client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=self.chat_history,
            max_tokens=300, temperature=0.4, top_p=0.7
        )

        response = completion.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": response})
        return response

    def make_equation(self, subject, difficulty="mediana"):
        """ Gera um problema matemático com base em um tema e dificuldade. """
        prompt = f"Formule um problema matemático sobre {subject} de dificuldade {difficulty}, adequado para alunos até o 8º ano."
        self.chat_history.append({"role": "user", "content": prompt})

        completion = self.client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=self.chat_history,
            max_tokens=400, temperature=1.4, top_p=0.7
        )

        response = completion.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": response})
        self.last_problem = response
        return response

    def fix_solution(self, student_ans, problem=None):
        """ Corrige uma resposta do aluno para um problema fornecido ou para o último problema resolvido. """
        if problem is None:
            if self.last_problem is None:
                return "Nenhum problema foi resolvido anteriormente. Forneça um problema para correção."
            problem = self.last_problem

        prompt = f"O problema é: {problem}.\nO aluno respondeu: '{student_ans}'.\nVerifique se está correta. Se não, forneça a solução correta passo a passo."

        self.chat_history.append({"role": "user", "content": prompt})

        completion = self.client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=self.chat_history,
            max_tokens=500, temperature=1, top_p=0.7
        )

        response = completion.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": response})
        return response

    def explain_concept(self, concept, difficulty="medio"):
        """ Explica um conceito matemático com base no nível do aluno. """
        prompt = f"Explique o conceito de {concept} para um estudante com conhecimento {difficulty}."

        self.chat_history.append({"role": "user", "content": prompt})

        completion = self.client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=self.chat_history,
            max_tokens=300, temperature=1.4, top_p=0.7
        )

        response = completion.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": response})
        return response

    def identify_intent(self, user_input):
        """ Identifica a intenção do usuário. """
        prompt = f"""O usuário digitou: "{user_input}". Determine a intenção e retorne apenas uma das palavras:
        - "resolver" → Se quer resolver um problema matemático.
        - "criar" → Se quer gerar um problema matemático.
        - "corrigir" → Se quer verificar uma resposta.
        - "explicar" → Se quer aprender um conceito.
        - "desconhecido" → Se a intenção não for clara.
        Retorne apenas uma dessas palavras, sem explicação adicional."""

        completion = self.client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10, temperature=0.4, top_p=0.7
        )

        return completion.choices[0].message.content.strip().lower()
