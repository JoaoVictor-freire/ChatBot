# 📚 Chatbot Educacional para Ensino Fundamental

## 📖 Sobre o Projeto
Este projeto consiste em um **chatbot baseado em LLM (Large Language Model)** desenvolvido para auxiliar alunos do ensino fundamental na resolução de problemas matemáticos. O chatbot pode identificar a intenção do usuário e fornecer suporte em quatro funcionalidades principais:

1. **Correção de Problemas**: Analisa e corrige um problema resolvido pelo aluno.
2. **Criação de Problemas**: Gera problemas matemáticos com diferentes níveis de dificuldade.
3. **Explicação de Conceitos**: Explica conceitos matemáticos de forma didática.
4. **Resolução de Problemas**: Resolve problemas matemáticos passados pelo aluno.

Para isso, o projeto utiliza uma **API do Grop** para processar e gerar respostas inteligentes.

---

## 🚀 Tecnologias Utilizadas

- **Python** - Linguagem principal para o desenvolvimento
- **API do Grop** - Para interações inteligentes e resposta personalizada
- **Jupyter Notebook/Vs Code** - Para testes e experimentação do modelo

---

## 🛠 Como Executar o Projeto

### 🔹 Pré-requisitos
Antes de começar, certifique-se de ter instalado:

- **Python 3.8+**
- **Pip**
- **Bibliotecas necessárias** (Groq, os)

### 🔹 Passos para execução

1. **Clone o repositório**
```sh
 git clone https://github.com/JoaoVictor-freire/ChatBot.git
```

2. **Instale as dependências**
```sh
 pip install groq
```

3. **Configure a API do Grop**
   - Obtenha sua chave de API no site do Grop
   - Crie um arquivo `.env` e adicione sua chave:
     ```sh
     GROG_API_KEY=seu_token_aqui
     ```

4. **Execute o chatbot**
```sh
 python main.py
```


---

## 📌 Exemplo de Uso

💬 **Entrada do usuário:**
> "Explique o conceito de frações para mim."

🤖 **Resposta do chatbot:**
> "Uma fração representa uma parte de um todo. Ela é composta por um numerador e um denominador..."

💬 **Entrada do usuário:**
> "Crie um problema de multiplicação."

🤖 **Resposta do chatbot:**
> "João tem 3 caixas, cada uma com 5 lápis. Quantos lápis ele tem no total?"

---
