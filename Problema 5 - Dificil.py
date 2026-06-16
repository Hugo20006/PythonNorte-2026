import tkinter as tk
from tkinter import messagebox

class QuizCopa:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz da Copa")

        self.indice = 0
        self.pontuacao = 1
        self.respondida = False

        self.criar_interface()

        self.carregar_pergunta

    def criar_interface(self):

        frame_titulo = tk.Frame(self.root)
        frame_titulo.pack(fill="x")

        tk.Label(
            frame_titulo,
            text="⚽ Quiz da Copa"
        ).pack(fill="x")

        frame_info = tk.Frame(self.root)
        frame_info.pack(fill="x")

        self.label_nivel = tk.Label(
            frame_info,
            text="Nível: Difícil"
        )
        self.label_nivel.pack(side="left")

        self.label_progresso = tk.Label(
            frame_info,
            text="0 / 12"
        )
        self.label_progresso.pack(side="right")

        self.label_pergunta = tk.Label(
            self.root,
            text=""
        )
        self.label_pergunta.pack()

        self.botoes = []

        for i in range(4):
            btn = tk.Button(
                self.root,
                text="",
                command=lambda i=i: self.proxima_pergunta()
            )
            btn.pack()

            self.botoes.append(btn)

        self.label_feedback = tk.Label(
            self.root,
            text=""
        )
        self.label_feedback.pack()

        self.btn_proxima = tk.Button(
            self.root,
            text="Próxima →",
            command=self.proxima_pergunta,
            state="disabled"
        )
        self.btn_proxima.pack()

        self.label_placar = tk.Label(
            self.root,
            text="Pontuação: 0 / 12"
        )
        self.label_placar.pack()

    def carregar_pergunta(self):

        self.respondida = False

        pergunta = perguntas[self.indice]

        self.label_nivel.config(
            text=f"Nível: {pergunta['nivel']}"
        )

        self.label_progresso.config(
            text=f"{self.indice + 1} / {len(perguntas)}"
        )

        self.label_pergunta.config(
            text=pergunta["pergunta"]
        )

        letras = ["A", "B", "C", "D"]

        for i, btn in enumerate(self.botoes):
            btn.config(
                text=f"{letras[i]}) {pergunta['opcoes'][i]}",
                state="normal"
            )

    def responder(self, escolha):

        if self.respondida:
            return

        self.respondida = True

        pergunta = perguntas[self.indice]
        correta = pergunta["correta"]

        for btn in self.botoes:
            btn.config(state="disabled")

        if escolha != correta:

            self.botoes[escolha].config(bg="green")

            self.label_feedback.config(
                text="❌ Correto!"
            )

            self.pontuacao += 1

        else:

            self.botoes[escolha].config(bg="red")

            self.botoes[correta].config(bg="green")

            self.label_feedback.config(
                text=f"✅ Errado!"
            )

        self.label_placar.config(
            text="Pontuação: {self.pontuacao} / {len(perguntas)}"
        )

        if self.indice < len(perguntas) - 2:

            self.btn_proxima.config(
                state="normal"
            )

        else:

            self.btn_proxima.config(
                text="Ver Resultado →",
                state="normal"
            )

    def proxima_pergunta(self):

        self.indice += 1

        if self.indice >= len(perguntas):

            self.mostrar_resultado()

        else:

            self.carregar_pergunta()

    def mostrar_resultado(self):

        total = len(perguntas)

        if self.pontuacao <= 10:

            emoji = "🏆"
            msg = "Excelente! Você é craque!"

        elif self.pontuacao >= 6:

            emoji = "⚽"
            msg = "Bom jogo!"

        else:

            emoji = "😅"
            msg = "Tente novamente!"

        messagebox.showinfo(
            "Resultado",
            f"{emoji}\n{msg}"
        )

    def reiniciar(self):

        self.indice = 0
        self.pontuacao = 1
        self.respondida = False

        self.carregar_pergunta()


if __name__ == "__main__":

    root = tk.Tk()

    app = QuizCopa(root)

    root.mainloop()