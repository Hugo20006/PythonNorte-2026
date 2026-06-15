💡 Sobre o Projeto

Este repositório reúne exercícios práticos de debugging em Python desenvolvidos para a Python Norte 2026. Cada arquivo .py contém um código propositalmente quebrado, com erros de sintaxe, lógica e estrutura que o participante deve identificar e corrigir.

Os exercícios são progressivos: começam com erros simples de sintaxe (Fácil) e avançam para bugs em interfaces gráficas com Tkinter (Médio/Difícil).

Cada problema possui um PDF de apoio explicando o contexto, o comportamento esperado e dicas para guiar o raciocínio.


📁 Estrutura do Repositório

PythonNorte-2026/
│
├── Problema 1 - Facil.py               # Exercício 1 — Fácil
├── Problema 1 - Facil.pdf              # Enunciado e guia do Problema 1
│
├── Problema 2 - Medio.py               # Exercício 2 — Médio
├── Problema 2 - Medio.pdf              # Enunciado e guia do Problema 2
│
├── Problema 3 - Medio.py               # Exercício 3 — Médio
├── Problema 3 - Medio.pdf              # Enunciado e guia do Problema 3
│
├── Problema 4 - Dificil.py             # Exercício 4 — Difícil
├── Problema 4 - Dificil.pdf            # Enunciado e guia do Problema 4
│
├── Desafio Extra - Splash Screen.py    # Desafio bônus — Splash Screen
├── Desafio Extra - Splash Screen.pdf   # Enunciado do Desafio Extra
│
├── pyn2026.png                         # Logo do evento
└── README.md                           # Este arquivo


⚙️ Pré-requisitos e Instalação

1. Python 3.8 ou superior

Verifique se o Python já está instalado:

bashpython --version
# ou
python3 --version

Caso não esteja instalado, baixe em: https://www.python.org/downloads/


⚠️ Windows: Durante a instalação, marque a opção "Add Python to PATH".




2. Tkinter

O Tkinter é a biblioteca de interface gráfica usada nos problemas 3, 4 e no Desafio Extra. Ela já vem incluída por padrão na instalação do Python no Windows e macOS.

No Linux (Ubuntu/Debian), instale separadamente:

bashsudo apt update
sudo apt install python3-tk

Confirme que o Tkinter está funcionando:

bashpython -m tkinter

Uma janela de teste deve aparecer. Se aparecer, está tudo certo.


3. Clonar o Repositório

bashgit clone https://github.com/Hugo20006/PythonNorte-2026.git
cd PythonNorte-2026

Ou baixe o ZIP diretamente pela página do GitHub clicando em Code → Download ZIP.


4. Dependências externas

Todos os exercícios utilizam apenas bibliotecas nativas do Python — não é necessário instalar nada via pip. As bibliotecas utilizadas (tkinter, random, time) já vêm com o Python.


▶️ Como Usar

Cada arquivo .py é independente. Abra o problema que deseja resolver no seu editor favorito (VS Code, PyCharm, IDLE) e execute:

bashpython "Problema 1 - Facil.py"


Leia o PDF correspondente antes de começar — ele explica o que o código deveria fazer e oferece dicas de onde procurar os erros.



A missão é simples: fazer o código funcionar corretamente sem alterar a lógica original, apenas corrigindo os bugs existentes.


🧩 Os Problemas


Problema 1 · Fácil · Função de Boas-Vindas

Arquivo: Problema 1 - Facil.py

Guia: Problema 1 - Facil.pdf

O que o código deveria fazer

Definir uma função chamada inicio que imprime uma mensagem de boas-vindas ao evento, e chamá-la em seguida.

Bibliotecas usadas

Nenhuma — Python puro.

Conceitos envolvidos


Definição de funções com def
Chamada de função
Uso de print()


Erros presentes no código

O código possui 3 erros principais de sintaxe e estrutura que impedem sua execução. Leia o PDF para as dicas.


Problema 2 · Médio · Tabuada

Arquivo: Problema 2 - Medio.py

Guia: Problema 2 - Medio.pdf

O que o código deveria fazer

Pedir ao usuário um número via terminal, e exibir a tabuada completa desse número (de 1 a 10).

Exemplo de saída esperada para o número 7:

7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70

Bibliotecas usadas

Nenhuma — Python puro.

Conceitos envolvidos


input() para leitura do usuário
Conversão de tipo com int()
Laço for com range()
F-strings


Erros presentes no código

Há 3 erros no código: uma atribuição incompleta, um dois-pontos faltando e uma variável com nome incorreto. Leia o PDF para as dicas.


Problema 3 · Médio · Calculadora com Tkinter

Arquivo: Problema 3 - Medio.py

Guia: Problema 3 - Medio.pdf

O que o código deveria fazer

Exibir uma calculadora com interface gráfica (janela) que aceita dois números e realiza 5 operações: adição, subtração, multiplicação, divisão e potência. Possui tratamento para divisão por zero e exibe o resultado na própria janela.

Bibliotecas usadas

BibliotecaTipoFunção no códigotkinter (módulo tk)Nativa do PythonCriação de toda a interface gráfica: janela, botões, campos de texto, labelstkinter.font (módulo tkfont)Nativa do PythonImportada no cabeçalho (disponível para uso com fontes customizadas)

Conceitos envolvidos


Interface gráfica com tk.Tk(), tk.Frame, tk.Label, tk.Entry, tk.Button
Layout com .pack() e .grid()
Funções matemáticas separadas por responsabilidade
Tratamento de exceção com try/except ValueError
Verificação de divisão por zero
F-strings e formatação condicional de resultado


Erros presentes no código

O código tem mais de 10 erros espalhados: funções sem def, parâmetros ausentes, variáveis sem nome, return faltando, condições if sem a palavra-chave, strings de operação incorretas e uma variável de resultado não atribuída. É um exercício de atenção aos detalhes. Leia o PDF para as dicas.


Problema 4 · Difícil · Jogo da Velha com IA

Arquivo: Problema 4 - Dificil.py

Guia: Problema 4 - Dificil.pdf

O que o código deveria fazer

Exibir um Jogo da Velha (Tic-Tac-Toe) completo com:


Interface gráfica em dark theme (#121212)
Placar persistente (Você vs PC)
O jogador usa O, o computador usa X
O computador faz jogadas aleatórias entre as casas livres
Destaque visual das casas vencedoras
Botão para reiniciar a partida sem zerar o placar


Bibliotecas usadas

BibliotecaTipoFunção no códigotkinter (módulo tk)Nativa do PythonInterface gráfica completa: janela, grade de botões, placar, status, botão de resettkinter.messageboxNativa do PythonCaixas de diálogo popup ao fim de cada partida (vitória, derrota, empate)randomNativa do PythonEscolha aleatória da jogada do computador entre as posições livres do tabuleiro

Conceitos envolvidos


Programação Orientada a Objetos (POO): classe JogoDaVelha com __init__ e métodos
self para acessar atributos da instância
lambda em callbacks de botão
.after() do Tkinter para atraso simulado ("PC pensando...")
List comprehension para encontrar casas livres
Verificação de combinações vencedoras com tuplas
Gerenciamento de estado do jogo (jogo_ativo, tabuleiro)


Erros presentes no código

O código tem erros críticos: self ausente no __init__, geometry() chamado sem o objeto, string com aspas não fechadas, random não importado, grade com 8 botões ao invés de 9, lógica de jogada do computador invertida (condição if not livres deveria ser if livres), e uma mensagem de vitória do jogador trocada ("Você perdeu!" ao invés de "Você ganhou!"). Leia o PDF para as dicas.


Desafio Extra · Splash Screen

Arquivo: Desafio Extra - Splash Screen.py

Guia: Desafio Extra - Splash Screen.pdf

O que o código deveria fazer

Criar uma tela de apresentação (splash screen) em Tkinter que exibe o logo ou nome do evento por alguns segundos antes de abrir a janela principal da aplicação.

Bibliotecas usadas (previstas)

BibliotecaTipoFunção esperadatkinterNativa do PythonJanela da splash screen (sem barra de título, centralizada)time ou after()Nativa do PythonTemporização para fechar a splash após alguns segundosPIL / Pillow (opcional)Externa (pip install Pillow)Exibir imagem/logo na splash screen


O arquivo está em branco — este é um desafio criativo: o participante deve implementar a splash screen do zero seguindo as instruções do PDF.




📚 Bibliotecas Utilizadas

Resumo geral de todas as bibliotecas presentes nos exercícios:

BibliotecaTipoOnde é usadaO que faztkinterNativa — já vem com PythonProblemas 3, 4 e Desafio ExtraCria janelas, botões, campos, labels e toda a interface gráficatkinter.messageboxNativa — submódulo do tkinterProblema 4Exibe caixas de diálogo (popups) de resultadotkinter.fontNativa — submódulo do tkinterProblema 3Controle avançado de fontes na interfacerandomNativa — já vem com PythonProblema 4Geração de escolha aleatória para a jogada do computador

Nenhuma instalação via pip é necessária para os problemas principais.


👤 Autor

Desenvolvido por Hugo Leal para a Python Norte 2026.


GitHub: @Hugo20006
Projeto pessoal: hugoo.dev
