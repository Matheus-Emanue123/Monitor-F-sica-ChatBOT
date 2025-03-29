import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# --- Layout ---
st.set_page_config(page_title="Monitor de Física", page_icon="🧑‍🏫")
st.markdown("<h1 style='text-align: center;'>🧑‍🏫 Monitor de Física</h1>", unsafe_allow_html=True)

# --- Escolha de tema ---
temas = ["Geral", "Cinemática", "Dinâmica", "Termodinâmica", "Eletricidade", "Óptica", "Ondulatória"]
tema_escolhido = st.selectbox("Escolha o tema da dúvida:", temas)

# --- Botão limpar conversa ---
if st.button("🧹 Limpar conversa"):
    st.session_state.chat_history = []

# --- Inicializa histórico ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Campo de entrada ---
user_input = st.text_input("Digite sua dúvida:")

# --- Prompt de sistema ---
system_prompt = {
    "role": "system",
    "content": (
        f"Você é um monitor de física paciente e amigável. "
        f"Explique conceitos de física de forma clara, como se fosse para alunos do ensino médio. "
        f"Use exemplos simples, linguagem acessível e foque no tema: {tema_escolhido}."
    )
}

# --- Envio da dúvida ---
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    messages = [system_prompt] + st.session_state.chat_history

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": messages,
        "temperature": 0.7
    }

    with st.spinner("Pensando..."):
        response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
    else:
        st.error(f"Erro na API: {response.status_code}")
        st.write(response.text)

# --- Exibe histórico em formato de chat ---
st.markdown("---")
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"<div style='background-color:#e0f7fa;padding:10px;border-radius:10px;margin-bottom:10px'><strong>🧍 Você:</strong><br>{msg['content']}</div>", unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f"<div style='background-color:#f1f8e9;padding:10px;border-radius:10px;margin-bottom:10px'><strong>🤖 Monitor:</strong><br>{msg['content']}</div>", unsafe_allow_html=True)

# --- Rodapé ---
st.markdown("---")
st.markdown("<small>Feito com ❤️ por Matheus Emanuel da Sivca • Usando LLaMA 3 via Groq API</small>", unsafe_allow_html=True)
