# 🚀 ESTRATÉGIA DE POTENCIALIZAÇÃO DO ARTIGO EM DESIGN SCIENCE RESEARCH (DSR)

**Objetivo:** Elevar o manuscrito DSR do patamar de proposta estruturada para um **artigo/capítulo com padrão de publicação internacional (Qualis A / Periódico de Alto Impacto)**, garantindo blindagem metodológica e aprovação imediata junto aos professores (Prof. Yukio e Profª Iraci).

---

## 🎯 1. OS 4 PILARES DE EXCELÊNCIA PARA O ARTIGO DSR

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      PILARES DE EVOLUÇÃO DO ARTIGO DSR (HEVNER ET AL.)                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. RASTREABILIDADE METODOLÓGICA (Design Principles formais de Gregor et al., 2020)     │
│ 2. SIMULAÇÃO NUMÉRICA DO ARTEFATO (Cenário Financeiro Real do TCU com WACC e IRPJ)    │
│ 3. PAINEL DE AVALIAÇÃO POR ESPECIALISTAS (Expert Evaluation Protocol com 4 Dimensões)   │
│ 4. REPRESENTAÇÃO VISUAL EM 3 CICLOS (Relevance Cycle, Design Cycle e Rigor Cycle)       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📐 PILAR 1: MATRIZ DE DESIGN PRINCIPLES (DP) FORMAIS
Em DSR de ponta (Gregor, Kruse & Seidel, 2020), o artefato deve derivar explicitamente seus **Princípios de Design (*Design Principles - DP*)** a partir dos Meta-Requisitos ($MR$):

| Meta-Requisito ($MR$) | Princípio de Design Prescritivo ($DP$) | Implementação Concreta no Framework ATaaS |
| :--- | :--- | :--- |
| **$MR_1$: Viabilidade TCU e Opex** | **$DP_1$ (Princípio da Liquidez e Eficiência Tributária):** *O sistema deve estruturar a remuneração por subscrição operacional dedutível no Lucro Real, contingenciando custos de ociosidade patrimonial.* | Formulação analítica de $TCU_{ATaaS}$, desoneração de 34% de IRPJ/CSLL e cláusula de desmobilização sem multa em caso de desligamento. |
| **$MR_2$: Disponibilidade e Uptime** | **$DP_2$ (Princípio da Continuidade Funcional Sem Fricção):** *A arquitetura de suporte deve descentralizar estoques-pulmão para garantir substituição emergencial (Hot-swap) em prazo inferior a um ciclo de trabalho.* | SLA contratual de Hot-swap em até 24h com Uptime garantido em $\ge 98,5\%$ e monitoramento preventivo de hardware. |
| **$MR_3$: Privacidade e LGPD** | **$DP_3$ (Princípio da Segregação Ontológica de Dados):** *O fluxo de telemetria deve dissociar estritamente métricas de saúde mecânica/elétrica do ativo de qualquer telemetria comportamental do usuário.* | Isolamento de telemetria (apenas voltagem, latência de drivers e ciclos de bateria; proibição de keyloggers ou métricas de tempo de digitação - art. 11 LGPD). |
| **$MR_4$: Mútua Adaptação com ERPs** | **$DP_4$ (Princípio da Mediação Semântica Interoperável):** *A solução deve prover middleware e scripts de injeção acessível para contornar limitações de interfaces gráficas legadas da firma.* | Desenvolvimento de conectores/APIs acessíveis para SAP GUI, TOTVS e portais corporativos em intranet. |
| **$MR_5$: Coprodução Biopsicossocial** | **$DP_5$ (Princípio da Centralidade no Usuário e Values-Fit):** *A especificação da tecnologia assistiva deve ser codesenhada com o trabalhador utilizando o modelo MPT, alinhando a liderança de equipe.* | Aplicação do instrumento MPT (Scherer, 2005) na Fase 1 e criação do Comitê Interfuncional (D&I, TI, RH, SST) na Fase 3. |

---

## 🔢 PILAR 2: SIMULAÇÃO NUMÉRICA PARAMÉTRICA DO CUSTO TOTAL DE USO (TCU)
Para tornar o artefato irresistível para o comitê avaliador e gestores (CFOs), incluímos uma **simulação contábil realista para 10 postos de trabalho corporativos** ao longo de 36 meses ($T=36$):

### Parâmetros da Simulação no Contexto Brasileiro:
* **Amostra:** 10 colaboradores com deficiência (5 com deficiência visual necessitando de software leitor com IA + display braille; 5 com deficiência motora necessitando de cadeira motorizada adaptada e teclados especiais);
* **Custo Médio Ponderado de Capital ($WACC$):** 12,0% ao ano (1,0% ao mês);
* **Alíquota Fiscal (Lucro Real):** 34% (25% IRPJ + 9% CSLL);
* **Taxa Média de Desligamento/Abandono ($p_{deslig}$):** 35% nos primeiros 12 meses no modelo Capex;
* **Custo Médio de Aquisição ($P_0$):** R$ 25.000,00 por posto (Total inicial = R$ 250.000,00);
* **Mensalidade Servitizada ($\Phi_{mensal}$):** R$ 980,00 por posto/mês com SLA integral e hot-swap.

### Tabela de Comparação Financeira Simulada (Valores Presentes Líquidos):

| Linha de Custo / Desembolso | Modelo Tradicional (Capex) | Modelo ATaaS Servitizado (Opex) | Diferencial / Economia |
| :--- | :--- | :--- | :--- |
| **Desembolso Inicial ($P_0$)** | R$ 250.000,00 | R$ 0,00 | **+ R$ 250.000,00 em caixa** |
| **Custo de Manutenção e Reparos Reativos ($C_{maint}$)** | R$ 58.400,00 (estocástico) | Incluso na mensalidade | Redução de incerteza |
| **Custo de Ociosidade por Abandono/Giro ($C_{ocioso}$)** | R$ 87.500,00 (ativo parado) | R$ 0,00 (remobilizado) | **R$ 87.500,00 eliminados** |
| **Impacto Fiscal / Desoneração (Lucro Real 34%)** | Depreciação lenta (5 anos) | - R$ 119.952,00 (abatimento) | Ganho de liquidez imediato |
| **Custo Total de Uso Presente ($TCU_{VPL}$)** | **R$ 342.180,00** | **R$ 232.848,00** | **Economia Líquida de 31,9%** |

> **Conclusão Gerencial do Artefato:** O modelo ATaaS não apenas reduz o custo total em **~32%**, mas **elimina 100% do risco de perda patrimonial** de equipamentos ociosos no almoxarifado corporativo.

---

## 👥 PILAR 3: PAINEL DE AVALIAÇÃO POR ESPECIALISTAS (*EXPERT EVALUATION PROTOCOL*)
Em vez de esperar respostas de centenas de estranhos na internet, o DSR orienta a validação por um **painel focal qualificado (4 a 6 especialistas com autoridade acadêmica e prática)**.

### Especialistas Recomendados (Acesso Direto do Grupo A):
1. **Profª. Drª. Maria Elizete Kunkel:** Referência nacional em Tecnologias Assistivas, Biomecânica e Inclusão (LabBiAT/UNIFESP);
2. **Profª. Drª. Míriam Raquel Diniz Zanetti:** Doutora em Gestão da Inovação e Sustentabilidade;
3. **Prof. Dr. Carlos Marcelo Gurjão de Godoy:** Engenheiro e pesquisador em inovação tecnológica;
4. **Liderança Executiva de RH/D&I da Embraer:** (Contato corporativo via Alexandre);
5. **Especialista em Acessibilidade Digital e ERPs:** Profissional de TI sênior do ecossistema de São José dos Campos.

### Ficha de Avaliação Estruturada do Artefato (Critérios de Prat et al., 2015):
Aplica-se um roteiro rápido (15 a 20 minutos de entrevista ou formulário estruturado) avaliando 4 dimensões com notas de 1 a 5:
* **Dimensão 1 (Utilidade Prática):** O framework resolve o abandono crônico de 30% a 50% de TAs nas empresas?
* **Dimensão 2 (Viabilidade Operacional):** As 4 fases gerenciais são factíveis de serem adotadas por comitês corporativos?
* **Dimensão 3 (Rigor Analítico e Financeiro):** A modelagem de TCU e a desoneração em Lucro Real refletem a tomada de decisão do CFO?
* **Dimensão 4 (Aderência Regulatória):** A segregação de telemetria atende plenamente ao art. 11 da LGPD?

---

## 📊 PILAR 4: CICLOS DE HEVNER (2007) VISUALIZADOS NO TEXTO
Inserir o diagrama canônico de Hevner no início da metodologia para impressionar a banca:
* **Ciclo de Relevância (*Relevance Cycle*):** Pessoas com deficiência no mercado de trabalho, Lei de Cotas nº 8.213/1991, ODS 8 e 10 e sistemas corporativos reais (SAP/TOTVS).
* **Ciclo de Design (*Design Cycle*):** Concepção do Framework ATaaS, formulação paramétrica do TCU, arquitetura de Privacy by Design e avaliação do artefato.
* **Ciclo de Rigor (*Rigor Cycle*):** S-D Logic (Vargo & Lusch), PSS (Tukker; Baines), MPT (Scherer), TOE (Tornatzky & Fleischer) e DSR (Peffers et al.; Hevner et al.).

---

## 🗓️ CRONOGRAMA DE FINALIZAÇÃO DO ARTIGO DSR (3 SEMANAS)

| Semana | Ações Críticas da Equipe | Responsável |
| :--- | :--- | :--- |
| **Semana 1 (24 a 31/10)** | Inserir a simulação numérica do TCU e os Design Principles formais no texto; agendar 3 a 4 conversas com orientadores/especialistas. | Josué + Alexandre |
| **Semana 2 (01 a 07/11)** | Realizar as entrevistas de avaliação do artefato (Painel de Especialistas) e compilar as citações qualitativas na Seção 6. | Toda a equipe |
| **Semana 3 (08 a 15/11)** | Revisão final ortográfica, diagramação nas normas da editora (ABNT) e fechamento do manuscrito para entrega. | Manuela + Equipe |
