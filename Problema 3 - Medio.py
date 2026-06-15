import tkinter as tk
from tkinter import font as tkfont

def adicao(a, b)
    

def subtracao(a, b):
    pass

def multiplicacao(a, b):
    return a * b

def divisao(, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def potencia(a,):
    return a ** b

 calcular(operacao):
    try:
        numero1 = (entry_num1.get())
         = float(entry_num2.get())
    except ValueError:
        mostrar_resultado("Insira números válidos!")
        return

     operacao == "1":
        resultado = adicao(numero1, numero2)
    elif operacao == "2":
        resultado = subtracao(numero1, numero2)
     elif operacao == "":
        resultado = multiplicacao(numero1, numero2)
    elif operacao == "4":
        resultado = divisao(numero1, numero2)
    elif operacao == "5":
        resultado = (numero1, numero2)
    else:
         = "Operação não encontrada."

    mostrar_resultado(resultado)

def mostrar_resultado(valor):
    if isinstance(valor, float) and valor == int(valor):
        label_resultado.config(text=f"Resultado:  {int(valor)}")
    else:
        label_resultado.config(text=f"Resultado:  {valor}")

# ─── Interface ─────────────────────────────────────────────────────────────────

janela = tk.Tk()
janela.title("Calculadora — Problema 4")
janela.configure(bg="#0f172a")
janela.resizable(False, False)

FONTE_TITULO  = ("Consolas", 15, "bold")
FONTE_LABEL   = ("Consolas", 11)
FONTE_ENTRY   = ("Consolas", 13)
FONTE_BTN     = ("Consolas", 11, "bold")
FONTE_RESULT  = ("Consolas", 13, "bold")

COR_BG        = "#0f172a"
COR_CARD      = "#1e293b"
COR_ACENTO    = "#06b6d4"   # cyan
COR_BTN       = "#164e63"
COR_BTN_HV    = "#0e7490"
COR_TEXTO     = "#e2e8f0"
COR_SUBTEXT   = "#94a3b8"
COR_RESULTADO = "#34d399"   # verde esmeralda

# Título
frame_titulo = tk.Frame(janela, bg=COR_ACENTO, pady=1)
frame_titulo.pack(fill="x")

tk.Label(
    frame_titulo, text="  Calculadora  ", bg=COR_BG,
    fg=COR_ACENTO, font=FONTE_TITULO, pady=12
).pack(fill="x")

# Card principal
frame_card = tk.Frame(janela, bg=COR_CARD, padx=28, pady=22)
frame_card.pack(padx=20, pady=16, fill="both")

# Entradas
def criar_campo(parent, label_text, row):
    tk.Label(parent, text=label_text, bg=COR_CARD, fg=COR_SUBTEXT,
             font=FONTE_LABEL, anchor="w").grid(row=row, column=0, sticky="w", pady=(0,4))
    entry = tk.Entry(parent, font=FONTE_ENTRY, bg="#0f172a", fg=COR_TEXTO,
                     insertbackground=COR_ACENTO, relief="flat",
                     highlightthickness=1, highlightcolor=COR_ACENTO,
                     highlightbackground="#334155", width=18)
    entry.grid(row=row+1, column=0, columnspan=2, sticky="ew", pady=(0,14), ipady=6)
    return entry

entry_num1 = criar_campo(frame_card, "Primeiro número", 0)
entry_num2 = criar_campo(frame_card, "Segundo número",  2)

# Separador
tk.Frame(frame_card, bg="#334155", height=1).grid(
    row=4, column=0, columnspan=2, sticky="ew", pady=(0, 14))

# Botões de operação
operacoes = [
    ("1", "＋  Adição"),
    ("2", "－  Subtração"),
    ("3", "×  Multiplicação"),
    ("4", "÷  Divisão"),
    ("5", "^  Potência"),
]

def hover_on(btn):  btn.config(bg=COR_BTN_HV)
def hover_off(btn): btn.config(bg=COR_BTN)

for i, (codigo, nome) in enumerate(operacoes):
    col = i % 2
    row = 5 + (i // 2) * 2
    btn = tk.Button(
        frame_card, text=nome, font=FONTE_BTN,
        bg=COR_BTN, fg=COR_TEXTO, activebackground=COR_BTN_HV,
        activeforeground=COR_TEXTO, relief="flat", cursor="hand2",
        padx=10, pady=8,
        command=lambda c=codigo: calcular(c)
    )
    btn.grid(row=row, column=col, sticky="ew", padx=4, pady=4)
    btn.bind("<Enter>", lambda e, b=btn: hover_on(b))
    btn.bind("<Leave>", lambda e, b=btn: hover_off(b))

frame_card.columnconfigure(0, weight=1)
frame_card.columnconfigure(1, weight=1)

# Resultado
tk.Frame(frame_card, bg="#334155", height=1).grid(
    row=10, column=0, columnspan=2, sticky="ew", pady=(12, 10))

label_resultado = tk.Label(
    frame_card, text="Resultado:  —", bg=COR_CARD,
    fg=COR_RESULTADO, font=FONTE_RESULT, anchor="center"
)
label_resultado.grid(row=11, column=0, columnspan=2, pady=(0, 4))

# Rodapé
tk.Label(
    janela, text="Python Norte 2026 · Unama Ananindeua",
    bg=COR_BG, fg="#475569", font=("Consolas", 9)
).pack(pady=(0, 10))

janela.mainloop()