# -*- coding: utf-8 -*-
"""
Gera o arquivo PowerPoint (.pptx) para a apresentação do Capítulo de Livro / Artigo
para a Tutoria Docente com os Professores Antônio Yukio Ueta e Iraci de Souza João.
- 16:9 Widescreen (13.333 x 7.5 polegadas)
- Design premium profissional (fundo escuro moderno, cards estruturados, cores institucionais)
- Totalmente editável no PowerPoint
- Notas de orador (Speaker Notes) completas para que os colegas apresentem com segurança
"""

import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

sys.stdout.reconfigure(encoding='utf-8')

prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Paleta de Cores
C_BG = RGBColor(9, 13, 22)           # #090D16 (Fundo Escuro Sofisticado)
C_CARD = RGBColor(15, 23, 42)        # #0F172A (Card Base)
C_CARD_ALT = RGBColor(30, 41, 59)    # #1E293B
C_PRIMARY = RGBColor(56, 189, 248)   # #38BDF8 (Ciano / Azul Inovação)
C_ACCENT = RGBColor(129, 140, 248)   # #818CF8 (Índigo / Roxo)
C_SUCCESS = RGBColor(52, 211, 153)   # #34D399 (Esmeralda)
C_WARNING = RGBColor(251, 191, 36)   # #FBBF24 (Âmbar / Alerta)
C_DANGER = RGBColor(248, 113, 113)   # #F87171 (Rosa / Coral)
C_TEXT = RGBColor(248, 250, 252)     # #F8FAFC (Branco Puro)
C_TEXT_MUTED = RGBColor(148, 163, 184)# #94A3B8 (Cinza Médio)
C_TEXT_BODY = RGBColor(226, 232, 240)# #E2E8F0 (Texto Principal)
C_BORDER = RGBColor(51, 65, 85)      # #334155 (Borda Suave)

FONT_TITLE = "Arial"
FONT_BODY = "Arial"
FONT_MONO = "Consolas"

def apply_background(slide):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = C_BG

def add_header(slide, tag_text, title_text, subtitle_text=""):
    # Tag
    tb_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.73), Inches(0.35))
    tf_tag = tb_tag.text_frame
    tf_tag.word_wrap = True
    tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = tag_text.upper()
    p_tag.font.name = FONT_TITLE
    p_tag.font.size = Pt(10)
    p_tag.font.bold = True
    p_tag.font.color.rgb = C_PRIMARY

    # Title
    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.73), Inches(0.7))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.name = FONT_TITLE
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = C_TEXT

    # Subtitle
    if subtitle_text:
        tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.45), Inches(11.73), Inches(0.4))
        tf_sub = tb_sub.text_frame
        tf_sub.word_wrap = True
        tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = subtitle_text
        p_sub.font.name = FONT_BODY
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = C_TEXT_MUTED

def add_footer(slide, current_num, total_num=10):
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.73), Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = f"PPGPIT UNIFESP • Gestão Estratégica da Inovação Assistiva Corporativa (GETI 2026) | Slide {current_num} de {total_num}"
    p.font.name = FONT_BODY
    p.font.size = Pt(9)
    p.font.color.rgb = C_TEXT_MUTED

def set_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = notes_text

def create_card_shape(slide, left, top, width, height, border_color=C_BORDER, fill_color=C_CARD):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)
    return shape

# ==============================================================================
# SLIDE 1: ABERTURA OFICIAL
# ==============================================================================
slide1 = prs.slides.add_slide(blank_layout)
apply_background(slide1)
add_header(slide1, 
           "EIXO OFICIAL #65 PPGPIT / UNIFESP • VERSÃO 5.0 AJUSTADA",
           "Da Aquisição Transacional à Servitização Contínua em Tecnologias Assistivas no Brasil",
           "Gestão Estratégica da Inovação, Novos Modelos de Negócio (ATaaS), Estado da Arte da Literatura e os ODS 8 e 10.")

# 3 Cards
card_w = Inches(3.64)
card_h = Inches(4.7)
gap = Inches(0.4)
top_y = Inches(2.05)

# Card 1: Equipe
c1 = create_card_shape(slide1, Inches(0.8), top_y, card_w, card_h, C_PRIMARY)
tf1 = c1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = Inches(0.25)
p1 = tf1.paragraphs[0]
p1.text = "👥 Equipe do Grupo A\n"
p1.font.bold = True
p1.font.size = Pt(14)
p1.font.color.rgb = C_PRIMARY

team_members = [
    "• Josué Jofre Tomaz de Almeida",
    "• Alexandre Pedroso Fernandes",
    "• Diana Cortez",
    "• Emilie Modolo",
    "• Manuela Lima",
    "• Renata Andrea de Oliveira"
]
for m in team_members:
    p = tf1.add_paragraph()
    p.text = m
    p.font.size = Pt(11)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(6)

# Card 2: Orientadores
c2 = create_card_shape(slide1, Inches(0.8) + card_w + gap, top_y, card_w, card_h, C_ACCENT)
tf2 = c2.text_frame
tf2.word_wrap = True
tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = Inches(0.25)
p2 = tf2.paragraphs[0]
p2.text = "🎓 Orientadores Vinculados\n"
p2.font.bold = True
p2.font.size = Pt(14)
p2.font.color.rgb = C_ACCENT

advisors = [
    "• Profª. Drª. Maria Elizete Kunkel\n  (LabBiAT / UNIFESP)",
    "• Profª. Drª. Míriam Raquel D. Zanetti\n  (UNIFESP)",
    "• Prof. Dr. Carlos Marcelo G. de Godoy\n  (UNIFESP)"
]
for a in advisors:
    p = tf2.add_paragraph()
    p.text = a
    p.font.size = Pt(11)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(10)

# Card 3: Docentes da Disciplina
c3 = create_card_shape(slide1, Inches(0.8) + (card_w + gap)*2, top_y, card_w, card_h, C_SUCCESS)
tf3 = c3.text_frame
tf3.word_wrap = True
tf3.margin_left = tf3.margin_right = tf3.margin_top = tf3.margin_bottom = Inches(0.25)
p3 = tf3.paragraphs[0]
p3.text = "🏛️ Docentes da Disciplina\n"
p3.font.bold = True
p3.font.size = Pt(14)
p3.font.color.rgb = C_SUCCESS

teachers = [
    "• Prof. Dr. Antônio Yukio Ueta\n  (Docente GETI / PPGPIT)",
    "• Profª. Drª. Iraci de Souza João\n  (Docente GETI / PPGPIT)\n",
    "📚 Enquadramento:\nCapítulo de Livro (Editora Pimenta Cultural) e Artigo Científico Estruturado."
]
for t in teachers:
    p = tf3.add_paragraph()
    p.text = t
    p.font.size = Pt(11)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(8)

add_footer(slide1, 1)
set_speaker_notes(slide1, 
"""FALA DO APRESENTADOR (SLIDE 1 - ABERTURA):
'Bom dia / boa tarde, Professores Yukio e Iraci. Apresentamos aqui a proposta ajustada do Grupo A para o nosso Capítulo de Livro e Artigo da disciplina de Gestão Estratégica da Inovação.
O nosso tema é: 'Da Aquisição Transacional à Servitização Contínua em Tecnologias Assistivas no Brasil'.
O Josué não pôde estar presente conosco nesta reunião por motivo de agenda profissional inadiável, mas a equipe está totalmente alinhada e estruturada para apresentar nossa evolução metodológica e teórica.
Incorporamos integralmente as devolutivas da banca: retiramos termos metodologicamente inadequados (como RSL restrita), focamos na revisão robusta do estado da arte com 19 artigos já levantados em texto integral, estruturamos os objetivos no contexto Brasil e alinhamos a proposta aos ODS 8 e 10.'""")

# ==============================================================================
# SLIDE 2: GARGALO HISTÓRICO & A SOLUÇÃO DA GESTÃO DA INOVAÇÃO
# ==============================================================================
slide2 = prs.slides.add_slide(blank_layout)
apply_background(slide2)
add_header(slide2, 
           "RESUMO EXECUTIVO COM FONTES NO TEXTO",
           "A Falência da Compra Rígida e a Oportunidade em Gestão da Inovação",
           "Por que o modelo tradicional falha e como a gestão da firma pode transformar a inclusão em capacidade sustentável.")

# 2 Large Cards
c2_w = Inches(5.66)
c2_h = Inches(4.7)

c_gargalo = create_card_shape(slide2, Inches(0.8), top_y, c2_w, c2_h, C_WARNING)
tfg = c_gargalo.text_frame
tfg.word_wrap = True
tfg.margin_left = tfg.margin_right = tfg.margin_top = tfg.margin_bottom = Inches(0.3)
pg = tfg.paragraphs[0]
pg.text = "⚠️ O Gargalo Histórico no Brasil\n"
pg.font.bold = True
pg.font.size = Pt(15)
pg.font.color.rgb = C_WARNING

gargalo_bullets = [
    "• Visão Cartorial e Compulsória: A introdução de Tecnologias Assistivas ocorre quase exclusivamente para cumprir a cota da Lei nº 8.213/91, mediante aquisições pontuais de equipamentos via CAPEX (Brasil, 1991).",
    "• Abandono Tecnológico Crônico: Estudos seminais mostram taxas de abandono entre 30% e 50% quando o colaborador muda de função, a TA quebra ou falta adaptação contínua (Scherer, 2005; Sugawara et al., 2018).",
    "• Incompatibilidade de TI e Processos: A empresa fornece a TA individual, mas mantém os sistemas centrais (SAP, TOTVS, intranets) inacessíveis, gerando ilhas de isolamento funcional (Leonard-Barton, 1988)."
]
for b in gargalo_bullets:
    p = tfg.add_paragraph()
    p.text = b
    p.font.size = Pt(11)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(10)

c_solucao = create_card_shape(slide2, Inches(0.8) + c2_w + gap, top_y, c2_w, c2_h, C_SUCCESS)
tfs = c_solucao.text_frame
tfs.word_wrap = True
tfs.margin_left = tfs.margin_right = tfs.margin_top = tfs.margin_bottom = Inches(0.3)
ps = tfs.paragraphs[0]
ps.text = "💡 A Solução Proposta pela Gestão da Inovação\n"
ps.font.bold = True
ps.font.size = Pt(15)
ps.font.color.rgb = C_SUCCESS

solucao_bullets = [
    "• Transição Paradigmática para Servitização: Migrar da compra rígida de produtos físicos para a contratação contínua de capacidade e autonomia como serviço - ATaaS (Baines et al., 2009; Tukker, 2004).",
    "• Mitigação do Risco Operacional: O modelo de assinatura (OPEX) transfere a manutenção, calibragem, substituição emergencial (hot-swap) e obsolescência para parceiros especializados com SLA garantido (Kowalkowski et al., 2017).",
    "• Valor Compartilhado e Sustentabilidade (ESG): Alinhamento direto com o ODS 8 (Trabalho Decente e Produtividade) e o ODS 10 (Redução das Desigualdades) através de rotinas organizacionais maduras (ONU, 2015)."
]
for b in solucao_bullets:
    p = tfs.add_paragraph()
    p.text = b
    p.font.size = Pt(11)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(10)

add_footer(slide2, 2)
set_speaker_notes(slide2,
"""FALA DO APRESENTADOR (SLIDE 2):
'Professores, o ponto de partida do nosso capítulo é resolver uma dor crônica da gestão corporativa brasileira.
Hoje, as empresas compram tecnologias assistivas apenas para cumprir a Lei de Cotas (Lei 8.213/91). Compram no balcão via CAPEX, entregam o equipamento e consideram a tarefa cumprida.
O resultado disso na literatura é devastador: Scherer (2005) e Sugawara (2018) mostram que entre 30% a 50% dos equipamentos são abandonados em menos de um ano por quebra, falta de manutenção ou incompatibilidade com sistemas como SAP e TOTVS.
A nossa tese, embasada na literatura de Servitização (Baines et al., 2009; Tukker, 2004), é que a inclusão só se torna sustentável quando tratada como serviço contínuo (Assistive Technology as a Service - ATaaS), pago via OPEX com SLA de manutenção, hot-swap e treinamento continuado.'""")

# ==============================================================================
# SLIDE 3: MODELOS DE SERVITIZAÇÃO EM TA
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
apply_background(slide3)
add_header(slide3, 
           "ESTRATÉGIAS DE SERVITIZAÇÃO & REFERÊNCIAS PRÁTICAS",
           "Servitização e Novos Modelos de Negócio em Tecnologia Assistiva",
           "Como as empresas pioneiras no Brasil e no mundo estão inovando na forma de viabilizar TAs no posto de trabalho.")

# 4 Cards horizontais
c4_w = Inches(2.72)
c4_h = Inches(3.6)
top_y3 = Inches(2.05)

c_m1 = create_card_shape(slide3, Inches(0.8), top_y3, c4_w, c4_h, C_PRIMARY)
tf = c_m1.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.2)
p = tf.paragraphs[0]
p.text = "1. ATaaS (As a Service)\n"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_PRIMARY
bullets_m1 = [
    "• Assinatura & Locação: A empresa contrata a capacidade funcional do colaborador com SLA contratual (Tukker, 2004).",
    "• Hot-Swap em 24h: Troca imediata do dispositivo em caso de falha técnica, sem parar a operação do trabalhador."
]
for b in bullets_m1:
    p = tf.add_paragraph()
    p.text = b
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(6)

c_m2 = create_card_shape(slide3, Inches(0.8) + (c4_w + Inches(0.28))*1, top_y3, c4_w, c4_h, C_ACCENT)
tf = c_m2.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.2)
p = tf.paragraphs[0]
p.text = "2. BPO Inclusivo\n"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_ACCENT
bullets_m2 = [
    "• Managed Services: Terceirização da avaliação biopsicossocial (CIF), homologação com a TI e treino das lideranças (Chesbrough, 2003).",
    "• Desonera o RH e a TI interna de complexidades de acessibilidade especializada."
]
for b in bullets_m2:
    p = tf.add_paragraph()
    p.text = b
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(6)

c_m3 = create_card_shape(slide3, Inches(0.8) + (c4_w + Inches(0.28))*2, top_y3, c4_w, c4_h, C_WARNING)
tf = c_m3.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.2)
p = tf.paragraphs[0]
p.text = "3. Customização Ágil\n"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_WARNING
bullets_m3 = [
    "• Manufatura Aditiva: Dispositivos customizados sob medida via modelagem paramétrica e impressão 3D.",
    "• Conexão LabBiAT: Articulação direta com pesquisas da Profª Maria Elizete Kunkel na UNIFESP."
]
for b in bullets_m3:
    p = tf.add_paragraph()
    p.text = b
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(6)

c_m4 = create_card_shape(slide3, Inches(0.8) + (c4_w + Inches(0.28))*3, top_y3, c4_w, c4_h, C_SUCCESS)
tf = c_m4.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.2)
p = tf.paragraphs[0]
p.text = "4. Casos de Mercado\n"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_SUCCESS
bullets_m4 = [
    "• Hand Talk: SaaS corporativo de tradução para Libras;",
    "• EqualWeb: IA para acessibilidade em portais e ERPs;",
    "• German Bionic: Exoesqueletos industriais via RaaS (Robotics as a Service)."
]
for b in bullets_m4:
    p = tf.add_paragraph()
    p.text = b
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(6)

# Callout inferior
callout = create_card_shape(slide3, Inches(0.8), Inches(5.85), Inches(11.73), Inches(1.0), C_PRIMARY, C_CARD_ALT)
tfc = callout.text_frame
tfc.word_wrap = True
tfc.margin_left = tfc.margin_right = tfc.margin_top = tfc.margin_bottom = Inches(0.18)
pc = tfc.paragraphs[0]
pc.text = "⚖️ Diferenciação Conceitual Chave (LBI nº 13.146/15):\n"
pc.font.bold = True
pc.font.size = Pt(11)
pc.font.color.rgb = C_PRIMARY
pc2 = tfc.add_paragraph()
pc2.text = "A Tecnologia Assistiva é o recurso centrado no colaborador (órtese, leitor de tela, exoesqueleto); a Acessibilidade Sistêmica é o atributo do ambiente e dos sistemas legados da firma (ERPs e processos). A servitização é o elo estratégico que integra ambos sem atritos."
pc2.font.size = Pt(10)
pc2.font.color.rgb = C_TEXT_BODY

add_footer(slide3, 3)
set_speaker_notes(slide3,
"""FALA DO APRESENTADOR (SLIDE 3):
'Neste slide trazemos a taxonomia dos modelos de negócio que estamos mapeando no capítulo:
1. ATaaS puro: assinatura com substituição rápida em 24h;
2. BPO Inclusivo: outsourcing da avaliação funcional e compatibilização;
3. Customização rápida por manufatura aditiva (ligada às pesquisas do LabBiAT da Profª Kunkel);
4. E casos reais de mercado como Hand Talk e German Bionic.
Ressaltamos a diferenciação que a colega Renata Oliveira trouxe com base na Lei Brasileira de Inclusão: TA é o recurso individual do colaborador; acessibilidade é a propriedade do sistema da firma. O papel da servitização é conectar essas duas pontas.'""")

# ==============================================================================
# SLIDE 4: PERGUNTA DE PESQUISA E OBJETIVOS ESPECÍFICOS
# ==============================================================================
slide4 = prs.slides.add_slide(blank_layout)
apply_background(slide4)
add_header(slide4, 
           "OBJETO DE PESQUISA • DELIMITAÇÃO AO CONTEXTO BRASIL",
           "Pergunta de Pesquisa e Objetivos Específicos do Capítulo",
           "Estruturação delimitada ao cenário corporativo brasileiro, articulando literatura seminal e levantamento empírico.")

# Callout Pergunta
c_qp = create_card_shape(slide4, Inches(0.8), Inches(2.05), Inches(11.73), Inches(1.3), C_PRIMARY, C_CARD_ALT)
tf_qp = c_qp.text_frame
tf_qp.word_wrap = True
tf_qp.margin_left = tf_qp.margin_right = tf_qp.margin_top = tf_qp.margin_bottom = Inches(0.2)
p_qp = tf_qp.paragraphs[0]
p_qp.text = "❓ Pergunta de Pesquisa Principal (Contexto Brasil):\n"
p_qp.font.bold = True
p_qp.font.size = Pt(12)
p_qp.font.color.rgb = C_PRIMARY
p_qp2 = tf_qp.add_paragraph()
p_qp2.text = '"Como as empresas corporativas no Brasil podem estruturar rotinas de gestão da inovação para migrar de compras transacionais (CAPEX) para modelos de servitização contínua em tecnologia assistiva (ATaaS/OPEX), e quais determinantes organizacionais e tecnológicos condicionam a redução do abandono tecnológico e a inclusão sociolaboral sustentável (ODS 8 e 10)?"'
p_qp2.font.italic = True
p_qp2.font.size = Pt(11)
p_qp2.font.color.rgb = C_TEXT

# 3 Objetivos Específicos
oe_w = Inches(3.64)
oe_h = Inches(3.3)
top_oe = Inches(3.55)

# OE1
c_oe1 = create_card_shape(slide4, Inches(0.8), top_oe, oe_w, oe_h, C_PRIMARY)
tf = c_oe1.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.2)
p = tf.paragraphs[0]
p.text = "OE1: Mapeamento da Literatura\n"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_PRIMARY
p2 = tf.add_paragraph()
p2.text = "Mapear no estado da arte nacional e internacional os modelos de negócio emergentes, as práticas de servitização (PSS/ATaaS) e os determinantes de abandono de TAs corporativas (Tukker, 2004; Scherer, 2005)."
p2.font.size = Pt(10.5)
p2.font.color.rgb = C_TEXT_BODY

# OE2
c_oe2 = create_card_shape(slide4, Inches(0.8) + oe_w + gap, top_oe, oe_w, oe_h, C_ACCENT)
tf = c_oe2.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.2)
p = tf.paragraphs[0]
p.text = "OE2: Diagnóstico no Brasil (Campo)\n"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_ACCENT
p2 = tf.add_paragraph()
p2.text = "Diagnosticar práticas em empresas no Brasil quanto à viabilidade de transição de Capex para Opex (assinatura com SLA), compatibilidade de ERPs legados e clima de implementação via survey e entrevistas com gestores."
p2.font.size = Pt(10.5)
p2.font.color.rgb = C_TEXT_BODY

# OE3
c_oe3 = create_card_shape(slide4, Inches(0.8) + (oe_w + gap)*2, top_oe, oe_w, oe_h, C_SUCCESS)
tf = c_oe3.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.2)
p = tf.paragraphs[0]
p.text = "OE3: Recomendações Gerenciais\n"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_SUCCESS
p2 = tf.add_paragraph()
p2.text = "Propor diretrizes e recomendações gerenciais para a implementação da servitização assistiva no Brasil, a partir da adaptação de frameworks seminais de PSS (Tukker, 2004; Baines et al., 2009) e MPT (Scherer, 2005)."
p2.font.size = Pt(10.5)
p2.font.color.rgb = C_TEXT_BODY

add_footer(slide4, 4)
set_speaker_notes(slide4,
"""FALA DO APRESENTADOR (SLIDE 4):
'Professores, atendendo à orientação de delimitar o escopo ao contexto corporativo brasileiro, refinamos a Pergunta de Pesquisa e os 3 Objetivos Específicos:
- OE1: Estado da arte da literatura sobre modelos PSS e abandono de TAs;
- OE2: Levantamento diagnóstico com gestores no Brasil sobre viabilidade de migração para OPEX e atrito com sistemas legados;
- OE3: Recomendações gerenciais práticas adaptando frameworks de referência para a realidade das empresas nacionais.
Importante destacar: não estamos nos propondo a criar um framework inédito do zero no vácuo; estamos adaptando modelos consagrados internacionalmente (Tukker, Baines, Scherer) para o contexto corporativo do Brasil.'""")

# ==============================================================================
# SLIDE 5: ESTRATÉGIA DE BUSCA E MAPEAMENTO DA LITERATURA (SEM RSL)
# ==============================================================================
slide5 = prs.slides.add_slide(blank_layout)
apply_background(slide5)
add_header(slide5, 
           "MÉTODO & ESTRATÉGIA DE BUSCA DA LITERATURA",
           "Estratégia de Busca e Mapeamento da Literatura",
           "Estruturação booleana em 3 eixos conceituais para mapear a servitização e modelos de negócio em TA (19 PDFs no repositório).")

# 2 Cards com as Strings
c_st_w = Inches(5.66)
c_st_h = Inches(3.7)

c_en = create_card_shape(slide5, Inches(0.8), top_y, c_st_w, c_st_h, C_PRIMARY)
tf = c_en.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]
p.text = "🌐 String em Inglês (Scopus, WoS, OpenAlex, Europe PMC)\n"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_PRIMARY

p_sub = tf.add_paragraph()
p_sub.text = "Eixo 1 (Servitização) AND Eixo 2 (TA/Acessibilidade) AND Eixo 3 (Firma/Trabalho)\n"
p_sub.font.size = Pt(10)
p_sub.font.bold = True
p_sub.font.color.rgb = C_ACCENT

p_code = tf.add_paragraph()
p_code.text = """( "servitization" OR "servitisation" OR "product-service system*" OR "PSS" OR "business model*" OR "as-a-service" OR "subscription" OR "leasing" OR "rental" )
AND
( "assistive technology" OR "assistive technologies" OR "assistive device*" OR "workplace accessibility" OR "digital accessibility" OR "inclusive technology" )
AND
( "workplace" OR "corporate" OR "organization*" OR "enterprise" OR "firm" OR "employment" OR "industry" )"""
p_code.font.name = FONT_MONO
p_code.font.size = Pt(8.5)
p_code.font.color.rgb = C_TEXT_BODY

p_meta = tf.add_paragraph()
p_meta.text = "\nFiltros: Artigos revisados por pares • Período: 2018–2026 • Acesso Aberto (Open Access)."
p_meta.font.size = Pt(9)
p_meta.font.color.rgb = C_TEXT_MUTED

c_pt = create_card_shape(slide5, Inches(0.8) + c_st_w + gap, top_y, c_st_w, c_st_h, C_ACCENT)
tf = c_pt.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]
p.text = "🇧🇷 String em Português (SciELO, Spell, CAPES, Google Scholar)\n"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_ACCENT

p_sub = tf.add_paragraph()
p_sub.text = "Eixo 1 (Servitização) E Eixo 2 (TA/Acessibilidade) E Eixo 3 (Firma/Trabalho)\n"
p_sub.font.size = Pt(10)
p_sub.font.bold = True
p_sub.font.color.rgb = C_PRIMARY

p_code = tf.add_paragraph()
p_code.text = """( "servitização" OR "sistema produto-serviço" OR "modelo de negócio" OR "como serviço" OR "locação" OR "aluguel" OR "assinatura" )
E
( "tecnologia assistiva" OR "tecnologias assistivas" OR "acessibilidade no trabalho" OR "acessibilidade digital" )
E
( "empresa" OR "corporativo" OR "ambiente de trabalho" OR "organização" OR "posto de trabalho" )"""
p_code.font.name = FONT_MONO
p_code.font.size = Pt(8.5)
p_code.font.color.rgb = C_TEXT_BODY

p_meta = tf.add_paragraph()
p_meta.text = "\nRecorte temporal: Legislação pós-LBI (Lei nº 13.146/2015) até o presente (2026)."
p_meta.font.size = Pt(9)
p_meta.font.color.rgb = C_TEXT_MUTED

# Callout Resultado
c_res = create_card_shape(slide5, Inches(0.8), Inches(5.9), Inches(11.73), Inches(0.95), C_SUCCESS, C_CARD_ALT)
tfr = c_res.text_frame
tfr.word_wrap = True
tfr.margin_left = tfr.margin_right = tfr.margin_top = tfr.margin_bottom = Inches(0.18)
pr = tfr.paragraphs[0]
pr.text = "📊 Resultados Já Levantados no Repositório:\n"
pr.font.bold = True
pr.font.size = Pt(11)
pr.font.color.rgb = C_SUCCESS
pr2 = tfr.add_paragraph()
pr2.text = "Através da automação da busca via APIs científicas (OpenAlex, Europe PMC e Crossref), mapeamos 54 obras e já baixamos 19 artigos em PDF texto integral salvos no repositório GitHub para fundamentar o capítulo."
pr2.font.size = Pt(10)
pr2.font.color.rgb = C_TEXT_BODY

add_footer(slide5, 5)
set_speaker_notes(slide5,
"""FALA DO APRESENTADOR (SLIDE 5):
'Professores, um ponto central que alinhamos internamente com a nossa colega Manuela Lima: como não vamos entregar um protocolo estrito de Revisão Sistemática (com protocolo PRISMA completo e tripla checagem cega), eliminamos o termo 'RSL' da nossa proposta.
Adotamos a nomenclatura 'Estratégia de Busca e Mapeamento da Literatura / Estado da Arte', que é metodologicamente precisa e honesta.
Apresentamos as duas strings booleanas estruturadas em 3 eixos conceituais (Servitização x Tecnologia Assistiva x Ambiente Corporativo).
Como resultado direto, já temos 19 artigos acadêmicos com texto integral em PDF baixados e organizados no nosso repositório.'""")

# ==============================================================================
# SLIDE 6: FUNDAMENTAÇÃO TEÓRICA & EVIDÊNCIAS
# ==============================================================================
slide6 = prs.slides.add_slide(blank_layout)
apply_background(slide6)
add_header(slide6, 
           "ESTADO DA ARTE & REFERÊNCIAS TEÓRICAS",
           "Fundamentação Teórica e Evidências da Literatura",
           "Articulação entre Service-Dominant Logic (S-D Logic), Modelo MPT, PSS, TCU e os 19 PDFs baixados.")

c_lit = create_card_shape(slide6, Inches(0.8), top_y, c_st_w, Inches(4.7), C_PRIMARY)
tfl = c_lit.text_frame
tfl.word_wrap = True
tfl.margin_left = tfl.margin_right = tfl.margin_top = tfl.margin_bottom = Inches(0.25)
p = tfl.paragraphs[0]
p.text = "📚 Literatura Seminal em Gestão da Inovação\n"
p.font.bold = True
p.font.size = Pt(14)
p.font.color.rgb = C_PRIMARY

lit_items = [
    "• Vargo & Lusch (2016): Service-Dominant Logic (Valor em uso e coprodução biopsicossocial do benefício).",
    "• Scherer (2005): Matching Person & Technology - MPT (Prevenção preditiva ao abandono de TAs no trabalho).",
    "• Gebauer et al. (2005): Superação do Paradoxo da Servitização via modularidade e precificação por disponibilidade.",
    "• Baines et al. (2009) & Tukker (2004): Sistemas Produto-Serviço (PSS) orientados ao resultado funcional.",
    "• Leonard-Barton (1988) & Klein & Sorra (1996): Mútua Adaptação com sistemas ERPs e Clima de Implementação na firma.",
    "• Modelagem TCU & LGPD: Equação de Custo Total de Uso e governança Privacy by Design (Art. 11 da Lei 13.709/18)."
]
for item in lit_items:
    p = tfl.add_paragraph()
    p.text = item
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(7)

c_pdf = create_card_shape(slide6, Inches(0.8) + c_st_w + gap, top_y, c_st_w, Inches(4.7), C_SUCCESS)
tfp = c_pdf.text_frame
tfp.word_wrap = True
tfp.margin_left = tfp.margin_right = tfp.margin_top = tfp.margin_bottom = Inches(0.25)
p = tfp.paragraphs[0]
p.text = "📑 Evidências Mapeadas nos 19 PDFs Baixados\n"
p.font.bold = True
p.font.size = Pt(14)
p.font.color.rgb = C_SUCCESS

pdf_items = [
    "• From Abandonment to Adoption (2026): Fatores determinantes na transição para a adoção sustentável de TAs e redução de atritos.",
    "• From Aid Dependency to Market Transformation (2026): Superação da lógica de caridade via modelos de mercado, negócios escaláveis e PSS.",
    "• Business Models for Sustainable eHealth (2021): Viabilidade econômica e sustentabilidade financeira de TAs digitais como serviço.",
    "• Digital Accessibility in Workplace (2025): Tendências e melhores práticas para interfaces acessíveis em intranets corporativas.",
    "• Economics of Innovation in Prosthetic/Orthotics (2021): Dinâmica econômica e viabilidade de TAs customizadas sob demanda."
]
for item in pdf_items:
    p = tfp.add_paragraph()
    p.text = item
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(7)

add_footer(slide6, 6)
set_speaker_notes(slide6,
"""FALA DO APRESENTADOR (SLIDE 6):
'Aqui articulamos a fundamentação teórica de Gestão da Inovação com as evidências empíricas dos artigos recentes.
No lado da teoria da firma:
- A S-D Logic de Vargo & Lusch explica que o valor não está na prótese física, mas no 'valor em uso' da pessoa trabalhando;
- O modelo MPT de Scherer é a ferramenta para evitar o abandono;
- O PSS de Baines e Tukker fundamenta a precificação por disponibilidade.
No lado empírico, destacamos dois artigos quentíssimos de 2026 recém-baixados: um que aborda a transição do abandono para a adoção, e outro que discute a superação da dependência de doações/caridade através de modelos de mercado e negócios sustentáveis.'""")

# ==============================================================================
# SLIDE 7: ABORDAGEM METODOLÓGICA E SURVEY CORPORATIVO
# ==============================================================================
slide7 = prs.slides.add_slide(blank_layout)
apply_background(slide7)
add_header(slide7, 
           "MÉTODO DE PESQUISA • TRIANGULAÇÃO METODOLÓGICA",
           "Abordagem Metodológica Mista Triangulada (MMR)",
           "Integração do mapeamento da literatura com levantamento diagnóstico (Survey) e entrevistas com gestores corporativos.")

c7_w = Inches(5.66)
c7_h = Inches(4.7)

c_surv = create_card_shape(slide7, Inches(0.8), top_y, c7_w, c7_h, C_PRIMARY)
tf = c_surv.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]
p.text = "📋 5 Blocos do Instrumento Survey (5 a 7 min)\n"
p.font.bold = True
p.font.size = Pt(14)
p.font.color.rgb = C_PRIMARY

survey_blocks = [
    "1. Perfil da Empresa e Respondente: Setor, porte e área do gestor (P&D, D&I, TI, RH);",
    "2. Governança e Processo Decisório: Como a empresa compra TAs hoje (CAPEX vs OPEX) e envolvimento do colaborador com deficiência;",
    "3. Atritos e Abandono Tecnológico: Incidência de obsolescência, falta de manutenção, rejeição e quebra de equipamentos;",
    "4. Prontidão para Servitização (ATaaS): Interesse em terceirização com SLA garantido, hot-swap e consultoria de compatibilização;",
    "5. Interoperabilidade e Sistemas Legados: Desafios de TI na integração de softwares assistivos com SAP, TOTVS e intranets."
]
for b in survey_blocks:
    p = tf.add_paragraph()
    p.text = b
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(7)

c_est = create_card_shape(slide7, Inches(0.8) + c7_w + gap, top_y, c7_w, c7_h, C_SUCCESS)
tf = c_est.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]
p.text = "🚀 Estratégia de Engajamento e Amostragem\n"
p.font.bold = True
p.font.size = Pt(14)
p.font.color.rgb = C_SUCCESS

strat_items = [
    "• Meta Amostral Realista: 25 a 40 respondentes corporativos qualificados no questionário quantitativo;",
    "• Entrevistas Semiestruturadas: 6 a 8 entrevistas em profundidade com gestores de grandes contas e lideranças de D&I;",
    "• Gatilho de Reciprocidade (Benchmarking): Oferta do 'Relatório Executivo de Benchmarking em Gestão Assistiva' como contrapartida aos respondentes;",
    "• Canais de Disseminação: ABRH, grupos de C-Level no LinkedIn, redes corporativas do PIT SJC e ecossistema UNIFESP;",
    "• Triangulação de Dados: Cruzamento dos dados primários de campo com a literatura internacional de servitização."
]
for item in strat_items:
    p = tf.add_paragraph()
    p.text = item
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(7)

add_footer(slide7, 7)
set_speaker_notes(slide7,
"""FALA DO APRESENTADOR (SLIDE 7):
'Para responder ao OE2, desenhamos um método misto triangulado (Mixed Methods Research).
O questionário foi planejado para ser enxuto (5 a 7 minutos), estruturado em 5 blocos objetivos: perfil, governança de compras, taxas de abandono, prontidão para o modelo de assinatura (ATaaS) e interoperabilidade com TI.
Como estratégia de engajamento corporativo, criamos um gatilho de reciprocidade: a empresa que responder receberá o Relatório Executivo de Benchmarking da UNIFESP.
Prevemos uma meta segura de 25 a 40 respondentes no survey e 6 a 8 entrevistas qualitativas para aprofundar as nuances gerenciais.'""")

# ==============================================================================
# SLIDE 8: FRAMEWORK CONCEITUAL INTEGRADO
# ==============================================================================
slide8 = prs.slides.add_slide(blank_layout)
apply_background(slide8)
add_header(slide8, 
           "PRODUTO DO CAPÍTULO • ADAPTAÇÃO DE REFERENCIAIS",
           "Framework de Gestão da Inovação Assistiva Corporativa",
           "Estruturação das 4 macro-rotinas de inovação para superação do abandono e implementação de servitização contínua.")

# 4 Quadrantes
qw = Inches(5.66)
qh = Inches(2.2)
top_q1 = Inches(2.05)
top_q2 = Inches(4.55)

# Q1
c_q1 = create_card_shape(slide8, Inches(0.8), top_q1, qw, qh, C_PRIMARY)
tf = c_q1.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
p = tf.paragraphs[0]
p.text = "1. Prospecção & Co-Design (Busca & Seleção)\n"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_PRIMARY
p2 = tf.add_paragraph()
p2.text = "• Mapeamento biopsicossocial centrado na pessoa (CIF);\n• Homologação preliminar de TI (compatibilidade com ERPs);\n• Conexão com Open Innovation e startups especializadas."
p2.font.size = Pt(9.5)
p2.font.color.rgb = C_TEXT_BODY

# Q2
c_q2 = create_card_shape(slide8, Inches(0.8) + qw + gap, top_q1, qw, qh, C_ACCENT)
tf = c_q2.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
p = tf.paragraphs[0]
p.text = "2. Mútua Adaptação (Implementação Técnica)\n"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_ACCENT
p2 = tf.add_paragraph()
p2.text = "• Customização ergonômica no posto real de trabalho (Leonard-Barton, 1988);\n• Adequação das APIs e intranets aos leitores de tela;\n• Ciclos ágeis de prototipagem e testes com o colaborador."
p2.font.size = Pt(9.5)
p2.font.color.rgb = C_TEXT_BODY

# Q3
c_q3 = create_card_shape(slide8, Inches(0.8), top_q2, qw, qh, C_WARNING)
tf = c_q3.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
p = tf.paragraphs[0]
p.text = "3. Clima de Implementação (Cultura & Treinamento)\n"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_WARNING
p2 = tf.add_paragraph()
p2.text = "• Capacitação contínua do usuário, pares e liderança imediata (Klein & Sorra, 1996);\n• Patrocínio executivo da alta direção (C-Level);\n• Eliminação de vieses capacitistas e valorização da autonomia."
p2.font.size = Pt(9.5)
p2.font.color.rgb = C_TEXT_BODY

# Q4
c_q4 = create_card_shape(slide8, Inches(0.8) + qw + gap, top_q2, qw, qh, C_SUCCESS)
tf = c_q4.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.18)
p = tf.paragraphs[0]
p.text = "4. Sustentação & KPIs (Ciclo de Vida & ESG)\n"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_SUCCESS
p2 = tf.add_paragraph()
p2.text = "• SLA ágil de manutenção preventiva e reposição hot-swap (Baines et al., 2009);\n• Gestão do Custo Total de Uso (TCU);\n• Monitoramento de KPIs de retenção, satisfação e avanço nos ODS 8 e 10."
p2.font.size = Pt(9.5)
p2.font.color.rgb = C_TEXT_BODY

add_footer(slide8, 8)
set_speaker_notes(slide8,
"""FALA DO APRESENTADOR (SLIDE 8):
'O produto central que pretendemos entregar no capítulo é a adaptação dos modelos clássicos de inovação (Tidd & Bessant; Tukker) estruturado em 4 fases:
1. Prospecção & Co-Design: mapeamento prévio sem compra precipitada de prateleira;
2. Mútua Adaptação: conceito clássico de Leonard-Barton, onde tecnologia e empresa se adaptam mutuamente;
3. Clima de Implementação: Klein & Sorra mostrando que sem apoio da liderança e treinamento da equipe, a tecnologia é boicotada;
4. Sustentação com KPIs: gestão por disponibilidade e valor compartilhado ESG.'""")

# ==============================================================================
# SLIDE 9: CRONOGRAMA E DIVISÃO DE TAREFAS
# ==============================================================================
slide9 = prs.slides.add_slide(blank_layout)
apply_background(slide9)
add_header(slide9, 
           "GESTÃO DO PROJETO • DIVISÃO DO GRUPO A",
           "Divisão de Tarefas da Equipe e Cronograma Rumo à Publicação",
           "Atribuições equilibradas entre os 6 membros da equipe e prazos alinhados ao edital da disciplina.")

c_crono = create_card_shape(slide9, Inches(0.8), top_y, Inches(11.73), Inches(4.7), C_ACCENT)
tf = c_crono.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.3)
p = tf.paragraphs[0]
p.text = "📅 Cronograma Integrado & Frentes de Trabalho\n"
p.font.bold = True
p.font.size = Pt(14)
p.font.color.rgb = C_ACCENT

tasks = [
    "• Frente 1: Mapeamento e Síntese Teórica da Literatura (19 artigos) — Alexandre Fernandes & Emilie Modolo",
    "  Análise de conteúdo dos PDFs baixados, extração de métricas de abandono e fundamentação dos modelos de servitização PSS.\n",
    "• Frente 2: Instrumento de Campo (Survey & Entrevistas) — Josué Jofre & Manuela Lima",
    "  Validação das questões do Google Forms/Survey, disseminação corporativa (ABRH/LinkedIn) e coleta com gestores.\n",
    "• Frente 3: Redação do Capítulo & Articulação Editorial — Diana Cortez & Renata Oliveira",
    "  Redação das seções conceituais (LBI, ODS 8 e 10, modelo TCU), adequação às normas da Editora Pimenta Cultural e revisão final.\n",
    "⏱️ Marcos Temporais (Milestones):\n"
    "  • Out/2026: Alinhamento com professores + Aplicação do Survey de campo;\n"
    "  • Nov/2026: Triangulação dos dados + Redação da versão preliminar do capítulo (V1 completa);\n"
    "  • Dez/2026: Entrega final formatada para publicação no livro e submissão do artigo."
]
for t in tasks:
    p = tf.add_paragraph()
    p.text = t
    p.font.size = Pt(10.5)
    p.font.color.rgb = C_TEXT_BODY
    p.space_after = Pt(4)

add_footer(slide9, 9)
set_speaker_notes(slide9,
"""FALA DO APRESENTADOR (SLIDE 9):
'Para garantir a entrega com excelência sem sobrecarga, dividimos a equipe em 3 frentes coordenadas:
- Alexandre e Emilie na síntese dos 19 artigos da literatura;
- Josué e Manuela na operação do survey e contato com as empresas;
- Diana e Renata na redação, fundamentação legal (LBI) e adequação editorial.
O cronograma prevê coleta de dados em outubro/novembro e entrega do texto final revisado em dezembro.'""")

# ==============================================================================
# SLIDE 10: PAUTA ABERTA PARA DIRECIONAMENTO DOS PROFESSORES
# ==============================================================================
slide10 = prs.slides.add_slide(blank_layout)
apply_background(slide10)
add_header(slide10, 
           "TUTORIA DOCENTE • DIRECIONAMENTO E FEEDBACK",
           "Pauta Aberta para Direcionamento dos Professores",
           "Tópicos específicos para validação e orientações dos Professores Antônio Yukio e Iraci de Souza João.")

c10_w = Inches(3.64)
c10_h = Inches(4.7)

# Pauta 1
c_p1 = create_card_shape(slide10, Inches(0.8), top_y, c10_w, c10_h, C_PRIMARY)
tf = c_p1.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]
p.text = "1. Validação Amostral\n"
p.font.bold = True
p.font.size = Pt(14)
p.font.color.rgb = C_PRIMARY
p2 = tf.add_paragraph()
p2.text = "O desenho prevê meta de 25 a 40 respondentes no Survey + 6 a 8 entrevistas com gestores.\n\n" \
          "❓ Pergunta aos Professores:\n" \
          "Consideram essa amostragem suficiente e adequada para um capítulo de livro com natureza exploratório-descritiva de diagnóstico nacional?"
p2.font.size = Pt(11)
p2.font.color.rgb = C_TEXT_BODY

# Pauta 2
c_p2 = create_card_shape(slide10, Inches(0.8) + c10_w + gap, top_y, c10_w, c10_h, C_ACCENT)
tf = c_p2.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]
p.text = "2. Equilíbrio Teórico\n"
p.font.bold = True
p.font.size = Pt(14)
p.font.color.rgb = C_ACCENT
p2 = tf.add_paragraph()
p2.text = "Articulação de Servitização (Baines / Tukker) + Abandono (Scherer MPT) + Implementação (Klein & Sorra / Leonard-Barton).\n\n" \
          "❓ Pergunta aos Professores:\n" \
          "A banca sugere enfatizar mais a teoria da firma (capacidades dinâmicas) ou o foco em modelos de negócio PSS atende plenamente ao escopo da disciplina?"
p2.font.size = Pt(11)
p2.font.color.rgb = C_TEXT_BODY

# Pauta 3
c_p3 = create_card_shape(slide10, Inches(0.8) + (c10_w + gap)*2, top_y, c10_w, c10_h, C_SUCCESS)
tf = c_p3.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.25)
p = tf.paragraphs[0]
p.text = "3. Desdobramento Editorial\n"
p.font.bold = True
p.font.size = Pt(14)
p.font.color.rgb = C_SUCCESS
p2 = tf.add_paragraph()
p2.text = "Capítulo de até 8.000 palavras no padrão da Editora Pimenta Cultural.\n\n" \
          "❓ Pergunta aos Professores:\n" \
          "Qual o direcionamento dos docentes para o desdobramento posterior em artigo de periódico (ex: RAI Revista de Administração e Inovação ou Journal of Technology Management)?"
p2.font.size = Pt(11)
p2.font.color.rgb = C_TEXT_BODY

add_footer(slide10, 10)
set_speaker_notes(slide10,
"""FALA DO APRESENTADOR (SLIDE 10 - FECHAMENTO E PERGUNTAS):
'Para fechar nossa apresentação e abrir para as orientações dos Professores Yukio e Iraci, colocamos três dúvidas estratégicas na mesa:
1. Validação da amostragem (25 a 40 no survey + 6 a 8 entrevistas);
2. Equilíbrio teórico entre servitização, abandono MPT e capacidades de inovação;
3. Orientações editoriais para desdobrar este capítulo em artigo científico de alto impacto.
Agradecemos muito o tempo e as orientações dos professores e abrimos a palavra para o feedback!'""")

# Salvar apresentação diretamente no diretório atual
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Apresentacao_Capitulo_Livro_Professores_GETI2026.pptx")
prs.save(output_path)
print(f"SUCCESS: Presentation saved at: {output_path}")
