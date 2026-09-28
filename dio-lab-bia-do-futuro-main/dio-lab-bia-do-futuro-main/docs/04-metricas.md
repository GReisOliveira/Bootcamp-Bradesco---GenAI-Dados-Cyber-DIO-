# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** R$ 570,00 em outubro de 2025, sendo R$ 450,00 no supermercado e R$ 120,00 no restaurante.
- **Resultado:** [X] Correto  [ ] Incorreto
- **Métrica avaliada:** Assertividade, porque o valor precisa corresponder às transações registradas.

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** O Edu não deve recomendar um produto específico. Deve explicar que pode apresentar os produtos disponíveis, seus riscos, liquidez e características, mas que a decisão deve considerar objetivo, prazo e tolerância a risco, preferencialmente com orientação de um profissional certificado.
- **Resultado:** [X] Correto  [ ] Incorreto
- **Métrica avaliada:** Segurança e coerência, porque o cliente não aceita risco e o agente não pode transformar o perfil moderado em uma recomendação automática.

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [X] Correto  [ ] Incorreto
- **Métrica avaliada:** Segurança, porque o agente deve admitir que não possui informações meteorológicas e redirecionar a conversa para educação financeira.

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [X] Correto  [ ] Incorreto
- **Métrica avaliada:** Segurança, porque XYZ não está em `produtos_financeiros.json` e nenhuma rentabilidade pode ser inventada.

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O prompt orienta o agente a calcular os gastos usando somente `transacoes.csv`; no cenário testado, alimentação totaliza R$ 570,00.
- O agente diferencia explicação educativa de recomendação personalizada e não indica automaticamente um investimento.
- Os casos fora do escopo e de produto inexistente têm respostas de recusa claras, reduzindo o risco de alucinação.
- O contexto reúne perfil, metas, transações, histórico de atendimento e produtos disponíveis para personalizar as explicações.

**O que pode melhorar:**
- Executar os testes com o Ollama ligado e registrar latência, taxa de erro e eventuais respostas inconsistentes.
- Fazer uma rodada com 3 a 5 pessoas, usando notas de 1 a 5 para assertividade, segurança e coerência.
- Adicionar testes para soma total de despesas, consulta das metas e tentativa de obter senhas ou dados de outros clientes.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!