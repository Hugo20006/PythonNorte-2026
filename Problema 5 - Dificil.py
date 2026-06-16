import tkinter as tk
from tkinter import messagebox

class QuizCopa:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz da Copa")

        self.indice = 0
        self.pontuacao = 0
        self.respondida = False

        # 1. CORREÇÃO: Criação da lista de perguntas do quiz (salva no objeto self)
        self.perguntas = [
            {
                "nivel": "Fácil",
                "pergunta": "Qual país sediou a Copa do Mundo de 2014?",
                "opcoes": ["Brasil", "Alemanha", "África do Sul", "Argentina"],
                "correta": 0
            },
            {
                "nivel": "Médio",
                "pergunta": "Quem é o maior artilheiro da história das Copas?",
                "opcoes": ["Pelé", "Ronaldo", "Miroslav Klose", "Lionel Messi"],
                "correta": 2
            },
            {
                "nivel": "Difícil",
                "pergunta": "Qual país venceu a primeira Copa do Mundo em 1930?",
                "opcoes": ["Brasil", "Uruguai", "Argentina", "Itália"],
                "correta": 1
            }
        ]

        self.criar_interface()
        self.carregar_pergunta()

    def criar_interface(self):
        frame_titulo = tk.Frame(self.root)
        frame_titulo.pack(fill="x", pady=5)

        tk.Label(
            frame_titulo,
            text="⚽ Quiz da Copa",
            font=("Arial", 16, "bold")
        ).pack(fill="x")

        frame_info = tk.Frame(self.root)
        frame_info.pack(fill="x", padx=10, pady=5)

        self.label_nivel = tk.Label(
            frame_info,
            text="Nível: Fácil",
            font=("Arial", 10, "italic")
        )
        self.label_nivel.pack(side="left", padx=10)

        # 2. CORREÇÃO: Ajustado o total dinamicamente baseado na lista
        self.label_progresso = tk.Label(
            frame_info,
            text=f"1 / {len(self.perguntas)}"
        )
        self.label_progresso.pack(side="right", padx=10)

        self.label_pergunta = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            wraplength=350,
            justify="center"
        )
        self.label_pergunta.pack(pady=15)

        self.botoes = []

        for i in range(4):
            btn = tk.Button(
                self.root,
                text="",
                width=30,
                command=lambda i=i: self.responder(i)
            )
            btn.pack(pady=5)
            self.botoes.append(btn)

        self.label_feedback = tk.Label(
            self.root,
            text="",
            font=("Arial", 11, "bold")
        )
        self.label_feedback.pack(pady=10)

        self.btn_proxima = tk.Button(
            self.root,
            text="Próxima →",
            command=self.proxima_pergunta,
            state="disabled"
        )
        self.btn_proxima.pack(pady=5)

        self.label_placar = tk.Label(
            self.root,
            text=f"Pontuação: 0 / {len(self.perguntas)}"
        )
        self.label_placar.pack(pady=10)

    def carregar_pergunta(self):
        self.respondida = False
        
        # Reseta a cor dos botões para o padrão do sistema
        for btn in self.botoes:
            btn.config(bg=self.root.cget("bg"))

        self.label_feedback.config(text="")
        self.btn_proxima.config(state="disabled")

        # 3. CORREÇÃO: Acessa a pergunta atual usando self.perguntas
        pergunta_atual = self.perguntas[self.indice]

        self.label_nivel.config(
            text=f"Nível: {pergunta_atual['nivel']}"
        )

        self.label_progresso.config(
            text=f"{self.indice + 1} / {len(self.perguntas)}"
        )

        self.label_pergunta.config(
            text=pergunta_atual["pergunta"]
        )

        letras = ["A", "B", "C", "D"]

        for i, btn in enumerate(self.botoes):
            btn.config(
                text=f"{letras[i]}) {pergunta_atual['opcoes'][i]}",
                state="normal"
            )

    def responder(self, escolha):
        if self.respondida:
            return

        self.respondida = True

        # 4. CORREÇÃO: Uso correto de self.perguntas
        pergunta_atual = self.perguntas[self.indice]
        correta = pergunta_atual["correta"]

        for btn in self.botoes:
            btn.config(state="disabled")

        if escolha == correta:
            self.botoes[escolha].config(bg="green")
            self.label_feedback.config(
                text="✅ Correto!",
                fg="green"
            )
            self.pontuacao += 1
        else:
            self.botoes[escolha].config(bg="red")
            self.botoes[correta].config(bg="green")
            self.label_feedback.config(
                text="❌ Errado!",
                fg="red"
            )

        self.label_placar.config(
            text=f"Pontuação: {self.pontuacao} / {len(self.perguntas)}"
        )

        # 5. CORREÇÃO: Removidas as chaves '{}' incorretas que causavam erro de sintaxe
        if self.indice < len(self.perguntas) - 1:
            self.btn_proxima.config(
                text="Próxima →",
                state="normal"
            )
        else:
            self.btn_proxima.config(
                text="Ver Resultado →",
                state="normal"
            )

    def proxima_pergunta(self):
        self.indice += 1

        # 6. CORREÇÃO: Uso correto de self.perguntas para verificar o fim do quiz
        if self.indice >= len(self.perguntas):
            self.mostrar_resultado()
        else:
            self.carregar_pergunta()

    def mostrar_resultado(self):
        total = len(self.perguntas)

        # Proporção de acertos para definir a mensagem de forma justa
        aproveitamento = self.pontuacao / total

        if aproveitamento >= 0.8:
            emoji = "🏆"
            msg = f"Excelente! Você é craque!\nAcertou {self.pontuacao} de {total}."
        elif aproveitamento >= 0.5:
            emoji = "⚽"
            msg = f"Bom jogo!\nAcertou {self.pontuacao} de {total}."
        else:
            emoji = "😅"
            msg = f"Tente novamente!\nAcertou {self.pontuacao} de {total}."

        messagebox.showinfo(
            "Resultado",
            f"{emoji}\n{msg}"
        )
        self.reiniciar()

    def reiniciar(self):
        self.indice = 0
        self.pontuacao = 0 # CORREÇÃO: Placar deve reiniciar em 0, e não em 1
        self.respondida = False
        self.label_placar.config(text=f"Pontuação: 0 / {len(self.perguntas)}")
        self.carregar_pergunta()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizCopa(root)
    root.mainloop()
