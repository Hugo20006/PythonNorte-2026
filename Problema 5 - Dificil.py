import tkinter as tk
from tkinter import messagebox

# ── Paleta de cores para o quiz ───
BG_PRINCIPAL  = "#1a1a2e"
BG_CARD       = "#16213e"
BG_HEADER     = "#0f3460"
ROXO          = "#533483"
ROXO_HOVER    = "#6a43a8"
AMARELO       = "#f5a623"
VERDE         = "#27ae60"
VERMELHO      = "#e74c3c"
AZUL_CLARO    = "#4fc3f7"
TEXT_PRIM     = "#ffffff"
TEXT_SEC      = "#b0bec5"
LARANJA       = "#e67e22"
NIVEL_CORES   = {"Fácil": VERDE, "Médio": LARANJA, "Difícil": VERMELHO}

class QuizCopa:
    def __init__(self, root):
        self.root = root
        self.root.title("⚽ Quiz da Copa")
        self.root.configure(bg=BG_PRINCIPAL)
        self.root.resizable(False, False)
        self.root.geometry("460x580")

        self.indice = 0
        self.pontuacao = 0
        self.respondida = True

        self.perguntas = 
            {
                "nivel": "Fácil",
                "pergunta": "Qual país sediou a Copa do Mundo de 2014?",
                "opcoes": ["Brasil", "Alemanha", "África do Sul", "Argentina"],
                "correta": 0
            },
            {
                "nivel": "Fácil",
                "pergunta": "Quantas vezes o Brasil venceu a Copa do Mundo?",
                "opcoes": ["3", "4", "5", "6"],
                "correta": 2
            },
            {
                "nivel": "Médio",
                "pergunta": "Quem é o maior artilheiro da história das Copas?",
                "opcoes": ["Pelé", "Ronaldo", "Miroslav Klose", "Lionel Messi"],
                "correta": 2
            },
            {
                "nivel": "Médio",
                "pergunta": "Qual seleção venceu a Copa do Mundo de 2018 na Rússia?",
                "opcoes": ["Croácia", "Brasil", "França", "Bélgica"],
                "correta": 2
            },
            {
                "nivel": "Difícil",
                "pergunta": "Qual país venceu a primeira Copa do Mundo em 1930?",
                "opcoes": ["Brasil", "Uruguai", "Argentina", "Itália"],
                "correta": 1
            },
            {
                "nivel": "Difícil",
                "pergunta": "Em qual Copa do Mundo Pelé marcou seu primeiro gol, com apenas 17 anos?",
                "opcoes": ["1954", "1958", "1962", "1966"],
                "correta": 1
            }
        ]

        .criar_interface()
        self.carregar_pergunta

    # ── Interface ────────────────────────────────────────────
    def criar_interface(self):
        frame_header = tk.Frame(self.root, bg=BG_HEADER)
        frame_header.pack(fill="x")

        tk.Label(
            frame_header,
            text="⚽   QUIZ DA COPA",
            font=("Arial", 18, "bold"),
            bg=BG_HEADER, fg=AMARELO,
            pady=14
        ).pack(side="left", padx=20)

        self.label_placar = tk.(
            frame_header,
            text="🏆 0 / 0",
            font=("Arial", 12, "bold"),
            bg=BG_HEADER, fg=TEXT_PRIM
        )
        self.label_placar.pack(side="left", padx=20)

        self.canvas_prog = tk.Canvas(
            self.root, height=6,
            bg="#0d1b2a", highlightthickness=0
        )
        self.canvas_prog.pack(fill="x")

        frame_info = tk.Frame(self.root, bg=BG_PRINCIPAL)
        frame_info.pack(fill="x", padx=20, pady=(10, 4))

        self.label_nivel = tk.Label(frame_info,
            text="● Fácil",
            font=("Arial", 10, "bold"),
            bg=BG_PRINCIPAL, fg=VERDE
        )
        self.label_nivel.pack("left")

        self.label_progresso = tk.Label(
            frame_info,
            text=f"Pergunta 1 / {len(self.perguntas)}",
            font=("Arial", 10),
            bg=BG_PRINCIPAL, fg=TEXT_SEC
        )
        self.label_progresso.pack(side="right")

        frame_card = tk.Frame(
            bg=BG_CARD,
            highlightbackground=ROXO,
            highlightthickness=2
        )
        frame_card.pack(fill="x", padx=20, pady=10)

        self.label_pergunta = tk.Label(
            frame_card,
            text="",
            font=("Arial", 13, "bold"),
            bg=BG_CARD, fg=TEXT_PRIM,
            wraplength=380,
            justify="center",
            padx=16, pady=20
        )
        self.label_pergunta.pack()

        self.botoes = []

        for i in range(4):
            btn = tk.Button(
                self.root,
                text="",
                font=("Arial", 11),
                bg=ROXO, fg=TEXT_PRIM,
                activebackground=ROXO_HOVER,
                activeforeground=TEXT_PRIM,
                relief="flat",
                anchor="w",
                padx=16,
                cursor="hand2",
                lambda i=i: self.responder(i)
            )
            btn.pack(fill="x", padx=20, pady=4, ipady)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=ROXO_HOVER) if b["state"] == "normal" else None)
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=ROXO) if b["state"] == "normal" else None)
            self.botoes.append(btn)

        self.label_feedback = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold"),
            bg=BG_PRINCIPAL, fg=TEXT_PRIM
        )
        self.label_feedback.pack(pady=(10, 2))

        self.btn_proxima = tk.Button(
            self.root,
            text="Próxima  →",
            font=("Arial", 11, "bold"),
            bg=AMARELO, fg="#1a1a2e",
            activebackground="#f0c040",
            relief="flat",
            cursor="hand2",
            state="disabled",
            command=self.proxima_pergunta
        )
        self.btn_proxima.pack(pady=8, ipadx=20, ipady=8)

    # ── Barra de progresso ──
    def atualizar_barra(self):
        self.canvas_prog.update_idletasks()
        w = self.canvas_prog.winfo_width() or 460
        self.canvas_prog.delete("all")
        frac = self.indice / len(self.perguntas)
        self.canvas_prog.create_rectangle(0, 0, int(w * frac), 6, fill=AMARELO, outline="")

    # ── Lógica ──
    def carregar_pergunta(self):
        self.respondida = False

        for btn in self.botoes:
            btn.config(bg=ROXO, fg=TEXT_PRIM, state="normal")

        self.label_feedback.config(text="")
        self.btn_proxima.config(state="disabled", bg="#555", fg=TEXT_SEC)

        pergunta_atual = self.perguntas[self.indice]

        nivel = pergunta_atual["nivel"]
        self.label_nivel.config(
            text=f"● {nivel}",
            fg=NIVEL_CORES.get(nivel, TEXT_SEC)
        )

        self.label_progresso.config(
            text=f"Pergunta {self.indice + 1} / {len(self.perguntas)}"
        )

        self.label_pergunta.config(text=pergunta_atual["pergunta"])

        self.label_placar.config(
            text=f"🏆 {self.pontuacao} / {len(self.perguntas)}"
        )

        letras = ["A", "B", "C", "D"]
        for i, btn in enumerate(self.botoes):
            btn.config(text=f"  {letras[i]})  {pergunta_atual['opcao'][i]}")

        self.root.after(50, self.atualizar_barra)

    def responder(self, escolha):
        if self.respondida: return
        self.respondida = True

        pergunta_atual = self.perguntas[self.indice]
        correta = pergunta_atual["correta"]

        for btn in self.botoes:
            btn.config(state="disabled")

        if escolhido = correta
            self.botoes[escolha].config(bg=VERDE, fg=TEXT_PRIM)
            self.label_feedback.config(text="✅  Correto!", fg=VERDE)
            self.pontuacao += 1
        else:
            self.botoes[escolha].config(bg=VERMELHO, fg=TEXT_PRIM)
            self.botoes[correta].config(bg=VERDE, fg=TEXT_PRIM)
            self.label_feedback.config(text="❌  Errado!", fg=VERMELHO)

        self.label_placar.config(
            text=f"🏆 {self.pontuacao} / {len(self.perguntas)}"
        )

        if self.indice >= len(self.perguntas)
            self.btn_proxima.config(text="Ver Resultado  →", state="normal", bg=AMARELO, fg="#1a1a2e")
        else:
            self.btn_proxima.config(text="Próxima  →", state="normal", bg=AMARELO, fg="#1a1a2e")

    def proxima_pergunta(self):
        if self.indice >= len(self.perguntas) - 1:
            self.mostrar_resultado()
        else:
            self.indice += 1
            self.carregar_pergunta()

    def mostrar_resultado(self):
        total = len(self.perguntas)
        aproveitamento = self.pontuacao / total

        if aproveitamento >= 0.8:
            emoji, msg = "🏆", "Você é craque!"
        elif aproveitamento >= 0.5:
            emoji, msg = "⚽", "Bom jogo!"
        else:
            emoji, msg = "😅", "Tente novamente!"

        messagebox.showinfo(
            "Resultado Final",
            f"{emoji}  {msg}\n\nAcertou {self.pontuacao} de {total} perguntas."
        )
        self.reiniciar()

    def 
        self.indice = 0
        self.pontuacao = 0
        self.respondida = False
        self.label_placar.config(text=f"🏆 0 / {len(self.perguntas)}")
        self.carregar_pergunta()


if __name__ == "__main__":
    root = tk.Tk()
    app =