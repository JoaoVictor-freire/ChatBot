from function import MathAssistant

# Inicializar o assistente de matemática
api_key = "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"  # Substitua pela sua chave real
assistant = MathAssistant(api_key)

print("Assistant: Bem-vindo ao Tutor de Matemática! Pergunte o que quiser.")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["sair", "exit", "quit"]:
        print("Assistant: Encerrando o chat. Até logo!")
        break

    # Identificar a intenção do usuário
    intent = assistant.identify_intent(user_input)

    if intent == "resolver":
        problem = input("Assistant: Qual problema deseja resolver? ")
        resposta = assistant.solve_problem(problem)
        print("\nAssistant:", resposta)

    elif intent == "criar":
        subject = input("Assistant: Sobre qual assunto deve ser o problema? ")
        difficulty = input("Assistant: Qual a dificuldade? (fácil, mediana, difícil) ") or "mediana"
        resposta = assistant.make_equation(subject, difficulty)
        print("\nAssistant:", resposta)

    elif intent == "corrigir":
        print("Assistant: Você deseja corrigir o problema anterior ou inserir um novo?")
        choice = input("Digite 'anterior' para corrigir o último problema resolvido ou 'novo' para inserir um novo problema: ").strip().lower()

        if choice == "anterior":
            student_ans = input("Assistant: Qual sua resposta para o problema anterior? ")
            resposta = assistant.fix_solution(student_ans)
        elif choice == "novo":
            problem = input("Assistant: Digite o problema que deseja corrigir: ")
            student_ans = input("Assistant: Qual sua resposta? ")
            resposta = assistant.fix_solution(student_ans, problem)
        else:
            resposta = "Escolha inválida. Digite 'anterior' ou 'novo'."

        print("\nAssistant:", resposta)

    elif intent == "explicar":
        concept = input("Assistant: Qual conceito deseja entender? ")
        level = input("Assistant: Qual seu nível? (básico, médio, avançado) ") or "medio"
        resposta = assistant.explain_concept(concept, level)
        print("\nAssistant:", resposta)

    else:
        print("\nAssistant: Não entendi sua solicitação. Poderia reformular a pergunta?")
