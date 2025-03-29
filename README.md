# 🧑‍🏫 Monitor de Física com IA

Este é um chatbot educacional criado com **Python**, **Streamlit** e **LLM (LLaMA 3 via Groq API)**. Ele atua como um **monitor virtual de Física**, respondendo dúvidas com linguagem acessível para estudantes do ensino médio.

![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red?logo=streamlit)
![Groq API](https://img.shields.io/badge/Powered%20by-Groq-blueviolet)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

## 🔗 Acesse o App

👉 [Clique aqui para testar o Monitor de Física online](https://monitor-f-sica-chatbot-manytwza373w48xkgrtn5h.streamlit.app)

---

## 💡 Funcionalidades

- Respostas simples e didáticas com base em LLM
- Interface web interativa via Streamlit
- Escolha de tema (Cinemática, Termodinâmica, etc.)
- Histórico de conversa com estilo de chat
- Suporte a fórmulas e explicações físicas
- Deploy gratuito com Streamlit Cloud
- Seguro (chave da API via `secrets.toml`)

---

## 🧠 Tecnologias utilizadas

- `Python`
- `Streamlit`
- `Groq API` com modelo `llama3-70b-8192`
- `requests`
- `python-dotenv`

---

## 🛠️ Como rodar localmente

```bash
# Clone o projeto
git clone https://github.com/Matheus-Emanue123/Monitor-F-sica-ChatBOT.git
cd monitor-fisica

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Crie o arquivo .env com sua chave da Groq
echo GROQ_API_KEY=sk-sua-chave-aqui > .env

# Rode o app
streamlit run app.py
```

---

## 📦 Deploy no Streamlit Cloud

1. Suba o código no GitHub
2. Vá para [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Crie um novo app com:
   - Main file: `app.py`
   - Branch: `main`
4. Vá na aba **Secrets** e adicione:

```toml
GROQ_API_KEY = "sk-sua-chave-aqui"
```

5. Clique em **Deploy**

---

## 📷 Screenshot

<img src="https://user-images.githubusercontent.com/exemplo/screenshot.png" alt="Monitor de Física interface" width="600"/>

---

## 🔄 Expansões futuras

- Suporte a fórmulas LaTeX
- Gráficos físicos com matplotlib
- Upload de questões para correção
- Geração automática de resumos

---

## 🙋‍♂️ Sobre o projeto

Este projeto foi desenvolvido como parte de um estudo em aplicações de IA e NLP voltadas para educação. Ele simula um monitor de física amigável, didático e gratuito, usando tecnologias modernas e acessíveis.

---

## 📬 Contato

Feito com ❤️ por Matheus Emamuel da Silva  
📧 matheus.silva@aluno.cefetmg.br
🐙 GitHub: [Matheus Silva](https://github.com/matheus-emanue123)

---

## 🧾 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
