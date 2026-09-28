import json
from pathlib import Path

import pandas as pd
import requests
import streamlit as st


# ============ CARREGAR DADOS ============
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

with open(DATA_DIR / "perfil_investidor.json", encoding="utf-8") as arquivo:
	perfil = json.load(arquivo)

transacoes = pd.read_csv(DATA_DIR / "transacoes.csv")
historico = pd.read_csv(DATA_DIR / "historico_atendimento.csv")

with open(DATA_DIR / "produtos_financeiros.json", encoding="utf-8") as arquivo:
	produtos = json.load(arquivo)


# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R$ {perfil['patrimonio_total']:.2f} | RESERVA: R$ {perfil['reserva_emergencia_atual']:.2f}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""


# ============ SYSTEM PROMPT ============
# Este prompt segue a versão documentada em docs/03-prompts.md, mais completa que
# o exemplo resumido apresentado nas imagens.
SYSTEM_PROMPT = """Você é o Edu, um educador financeiro inteligente, paciente e didático. Seu objetivo é
ajudar João Silva, cliente fictício de 32 anos, a compreender finanças pessoais,
organizar seus gastos e aprender sobre os produtos financeiros disponíveis, sem fazer
recomendações personalizadas de investimento.

REGRAS:
1. Responda em português do Brasil, com linguagem informal, acessível e didática.
2. Baseie afirmações sobre o cliente, transações, histórico e produtos somente nos
   dados fornecidos. Faça as contas explicitamente quando a pergunta exigir um valor.
3. Nunca invente taxas, saldos, transações, produtos, datas ou informações de mercado.
   Não trate os dados fictícios como dados bancários reais.
4. Explique conceitos financeiros sem julgar os hábitos do cliente e use analogias
   simples quando ajudarem na compreensão.
5. Não recomende, escolha ou compare um investimento como ordem personalizada. Você
   pode explicar características, riscos, liquidez, rentabilidade informada e público
   indicado na base, deixando claro que isso não é recomendação.
6. Para perguntas sobre adequação de investimento, explique que é preciso avaliar
   objetivos, prazo, liquidez e tolerância a risco, e sugira buscar um profissional
   certificado antes de decidir.
7. Se a informação não estiver no contexto, diga claramente que não sabe ou que ela
   não está disponível e ofereça uma forma segura de continuar.
8. Não revele senhas, dados sensíveis ou informações de outros clientes.
9. Em respostas sobre gastos, informe o período e as categorias consideradas. Não
   confunda entradas com saídas.
10. Termine respostas educativas com uma pergunta curta quando isso for apropriado.
"""


# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gpt-oss"


# ============ CHAMAR OLLAMA ============
def perguntar(mensagem: str) -> str:
	prompt = f"""{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {mensagem}"""

	resposta = requests.post(
		OLLAMA_URL,
		json={"model": MODEL, "prompt": prompt, "stream": False},
		timeout=120,
	)
	resposta.raise_for_status()
	dados = resposta.json()
	return dados["response"]


# ============ INTERFACE ============
st.set_page_config(page_title="Edu, seu Educador Financeiro", page_icon="💰")
st.title("💰 Edu, Seu Educador Financeiro")
st.caption("Aprenda sobre suas finanças usando os dados do cliente fictício João Silva.")

if "mensagens" not in st.session_state:
	st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
	with st.chat_message(mensagem["role"]):
		st.markdown(mensagem["content"])

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
	st.session_state.mensagens.append({"role": "user", "content": pergunta})
	with st.chat_message("user"):
		st.markdown(pergunta)

	with st.chat_message("assistant"):
		with st.spinner("Pensando..."):
			try:
				resposta = perguntar(pergunta)
			except requests.RequestException:
				resposta = (
					"Não consegui conectar ao Ollama agora. Verifique se o Ollama "
					f"está ativo e se o modelo `{MODEL}` está disponível."
				)
			except (KeyError, ValueError) as erro:
				resposta = f"Recebi uma resposta inesperada do Ollama: {erro}"

		st.markdown(resposta)
		st.session_state.mensagens.append(
			{"role": "assistant", "content": resposta}
		)
