import streamlit as st
import time
import random

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E CSS (VISUAL WHATSAPP)
# ==============================================================================
st.set_page_config(
    page_title="Guardião Gov 60+",
    page_icon="🛡",
    layout="centered"
)

# CSS para imitar a interface do WhatsApp
st.markdown("""
<style>
    /* Fundo geral */
    .stApp {
        background-color: #E5DDD5;
    }
    
    /* Remove padding excessivo do topo */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* Balão do Usuário (Verde WhatsApp) */
    .user-bubble {
        background-color: #dcf8c6;
        color: #000;
        padding: 10px 15px;
        border-radius: 10px 0px 10px 10px;
        margin: 5px 0 5px auto; /* auto na esquerda empurra pra direita */
        max-width: 80%;
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
        text-align: right;
        font-family: Helvetica, Arial, sans-serif;
    }

    /* Card do Bot (Branco) */
    .bot-card {
        background-color: #ffffff;
        color: #000;
        padding: 0;
        border-radius: 0px 10px 10px 10px;
        margin: 5px auto 5px 0; /* auto na direita empurra pra esquerda */
        max-width: 85%;
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
        font-family: Helvetica, Arial, sans-serif;
        overflow: hidden;
        border-left: 5px solid #ccc; /* Cor dinâmica será injetada aqui */
    }

    .bot-content { padding: 15px; }
    .bot-footer { 
        background-color: #f7f7f7; 
        padding: 10px 15px; 
        font-size: 12px; 
        color: #666;
        border-top: 1px solid #eee;
    }

    /* Esconde menu padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. LÓGICA DA API ("O CÉREBRO")
# ==============================================================================
def api_guardiao_gov(input_text):
    """
    Simula o processamento da API Governamental.
    """
    mensagem = input_text.lower()
    time.sleep(random.uniform(0.5, 1.2)) # Simula "pensando"

    # --- CENÁRIO 1: GOLPE FINANCEIRO ---
    if any(x in mensagem for x in ["pix", "senha", "bloqueio", "resgate", "valores", "clique", "conta suspensa"]):
        return {
            "status": "GOLPE FINANCEIRO",
            "risk": 5,
            "color": "#D32F2F", # Vermelho Alerta
            "icon": "🚨",
            "msg": "CUIDADO! Isso é uma tentativa de GOLPE.",
            "explain": "Órgãos oficiais e bancos *nunca* pedem senha ou transferências via link.",
            "tip": "Desconfie de mensagens urgentes ('faça agora ou perde').",
            "action": "🚫 Bloquear Contato",
            "source": "Banco Central / Lei 14.155"
        }

    # --- CENÁRIO 2: FAKE NEWS SAÚDE ---
    elif any(x in mensagem for x in ["cura", "chá", "milagre", "limão", "câncer", "diabetes", "vacina", "mata o vírus"]):
        return {
            "status": "FAKE NEWS SAÚDE",
            "risk": 4,
            "color": "#F57C00", # Laranja
            "icon": "💊",
            "msg": "Informação FALSA ou Sem Comprovação.",
            "explain": "Tratamentos caseiros não substituem a medicina. Cuidado com a automedicação.",
            "tip": "Na dúvida, não repasse. Consulte fontes oficiais.",
            "action": "👩‍⚕ Ver 'Saúde com Ciência'",
            "source": "Ministério da Saúde / ANVISA"
        }
    
    # --- CENÁRIO 3: SEGURO / OUTROS ---
    else:
        return {
            "status": "VERIFICADO",
            "risk": 1,
            "color": "#2E7D32", # Verde
            "icon": "✅",
            "msg": "Parece Seguro.",
            "explain": "Não encontramos termos de risco nesta mensagem.",
            "tip": "Continue atento. Se pedirem dinheiro, desconfie.",
            "action": "👍 Obrigado",
            "source": "Guardião Gov AI"
        }

# ==============================================================================
# 3. INTERFACE (FRONTEND)
# ==============================================================================

# Inicializa Histórico
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "type": "welcome",
            "content": "Olá! Sou o *Guardião Gov 60+* 🛡.\n\nEncaminhe para mim qualquer mensagem suspeita (texto ou áudio) que eu verifico para você."
        }
    ]

# --- BARRA LATERAL (DEMO CONTROLS) ---
with st.sidebar:
    st.header("⚙ Painel do Apresentador")
    st.info("Use estes botões para simular cenários reais durante o Pitch.")
    
    st.markdown("### 🧪 Testes Rápidos")
    
    # Botão 1: Golpe
    if st.button("🚨 Simular 'Falso Pix'"):
        st.session_state.temp_input = "URGENTE: Sua conta Gov foi suspensa. Pague o Pix no link para liberar: bit.ly/gov-pix"
        st.rerun() # Garante atualização imediata
        
    # Botão 2: Saúde
    if st.button("💊 Simular 'Cura Milagrosa'"):
        st.session_state.temp_input = "Recebi no grupo da igreja que chá de graviola cura diabetes em 3 dias."
        st.rerun()

    st.markdown("### 🎙 Acessibilidade")
    
    # Botão 3: Áudio
    if st.button("🎤 Simular Áudio (Idoso)"):
        st.session_state.temp_input = "[ÁUDIO TRANSCRITO]: Meu filho, recebi uma ligação do banco pedindo minha senha para atualizar o cadastro. É verdade isso?"
        st.rerun()

    st.markdown("---")
    st.caption("Visão Técnica: Backend API v1.0 connected to NewsData.io")

# --- ÁREA PRINCIPAL ---
st.title("Guardião Gov 60+")
st.markdown("Seu neto digital de confiança.")

# Container das mensagens
chat_placeholder = st.container()

# Verifica input (Do chat ou dos botões laterais)
user_input = st.chat_input("Digite sua mensagem...")

if "temp_input" in st.session_state:
    user_input = st.session_state.temp_input
    del st.session_state.temp_input

# PROCESSAMENTO
if user_input:
    # 1. Adiciona msg do usuário
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # 2. Adiciona placeholder de carregamento
    with chat_placeholder:
        # Re-renderiza histórico antes de mostrar o spinner
        pass 
        
    # 3. Chama API
    with st.spinner("🔍 Verificando bases oficiais..."):
        response_data = api_guardiao_gov(user_input)
    
    # 4. Adiciona resposta
    st.session_state.chat_history.append({
        "role": "assistant",
        "type": "analysis",
        "data": response_data
    })

# RENDERIZAÇÃO DO HISTÓRICO
with chat_placeholder:
    for msg in st.session_state.chat_history:
        
        # MENSAGEM DO USUÁRIO
        if msg["role"] == "user":
            st.markdown(f'<div class="user-bubble">{msg["content"]}</div><div style="clear:both"></div>', unsafe_allow_html=True)
        
        # MENSAGEM DO BOT (BO