import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "ace-ai"

st.set_page_config(
    page_title="ACE AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.stApp { background: #0b1020; color: #edf2ff; }
[data-testid="stSidebar"] { background: #111a2e; }
.block-container { max-width: 1000px; padding-top: 2rem; }
.ace-title { font-size: 2.25rem; font-weight: 800; letter-spacing: .04em; }
.ace-subtitle { color: #9fb0d0; margin-top: -.4rem; }
[data-testid="stChatMessage"] {
    background: #141f35; border: 1px solid #263653;
    border-radius: 16px; padding: 12px;
}
.stChatInput textarea { background: #141f35 !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🧠 ACE AI")
    st.caption("Your local personal assistant")
    st.markdown("---")
    st.markdown("**Model**")
    st.code(MODEL)
    st.caption("Runs through Ollama on this laptop.")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.caption("Phase 1 • Local chat interface")

st.markdown('<div class="ace-title">ACE AI <span style="color:#7c9cff">✦</span></div>', unsafe_allow_html=True)
st.markdown('<div class="ace-subtitle">Your personal AI. Your laptop. Your rules.</div>', unsafe_allow_html=True)
st.write("")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🧠" if message["role"] == "assistant" else "🙂"):
        st.markdown(message["content"])

prompt = st.chat_input("Message ACE AI...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🙂"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🧠"):
        placeholder = st.empty()
        answer = ""
        try:
            payload = {
                "model": MODEL,
                "messages": st.session_state.messages,
                "stream": True,
            }
            with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=(10, 600)) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    if not line:
                        continue
                    import json
                    chunk = json.loads(line.decode("utf-8"))
                    answer += chunk.get("message", {}).get("content", "")
                    placeholder.markdown(answer + "▌")
            placeholder.markdown(answer or "I didn't receive a response. Please try again.")
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except requests.exceptions.ConnectionError:
            st.error("Ollama isn't running. Open Ollama, then try again.")
        except requests.exceptions.HTTPError as exc:
            st.error("ACE AI model wasn't found. In Command Prompt, run: ollama create ace-ai -f Modelfile")
            st.caption(str(exc))
        except Exception as exc:
            st.error(f"Something went wrong: {exc}")
