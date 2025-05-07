"# TrabalhoLinguagensFormaisAltomatos" 

Projeto: Lema de Bombeamento
Este projeto implementa uma ferramenta simples para verificar o lema de bombeamento em linguagens formais. Ele permite testar se uma linguagem (definida por uma função Python) pode violar o lema de bombeamento para linguagens regulares.

📂 Descrição
O script bombeamento.py:
✅ Divide uma cadeia w em partes x, y, z conforme o lema de bombeamento.
✅ Testa repetições x yⁱ z para valores de i (até um máximo configurável).
✅ Usa uma função fornecida (language_fn) para verificar se a nova cadeia ainda pertence à linguagem.
✅ Exibe os resultados no terminal e indica se houve violação do lema.

🛠 Como usar
1️⃣ Defina a linguagem
No arquivo, você deve fornecer uma função que recebe uma string s e retorna True se s pertence à linguagem ou False caso contrário.
Exemplo incluído:

python
Copiar
Editar
def letras_anbn(s):
    a_count = 0
    b_count = 0
    stage = 'a'
    for c in s:
        if stage == 'a':
            if c == 'a':
                a_count += 1
            elif c == 'b':
                stage = 'b'
                b_count += 1
            else:
                return False
        elif stage == 'b':
            if c == 'b':
                b_count += 1
            else:
                return False
    return a_count == b_count and a_count > 0
2️⃣ Configure os parâmetros
No final do script:

python
Copiar
Editar
w = 'aaaaabbbbb'  # cadeia w para testar
p = 5             # comprimento p do lema
lema_bombeamento(letras_anbn, p, w)
3️⃣ Execute o script
No terminal:

bash
Copiar
Editar
python bombeamento.py
🔍 Exemplo de saída
O script imprime todas as combinações testadas e marca se pertencem ou não à linguagem.
Se encontrar uma violação (uma repetição que deveria estar na linguagem, mas não está), ele alerta que a linguagem pode não ser regular.

📦 Requisitos
Python 3.x
Nenhuma biblioteca externa é necessária.

✏️ Melhorias futuras
Ler funções de linguagem dinamicamente (ex: via import externo).

Salvar resultados em arquivo.

Interface gráfica simples ou interface web para testes interativos.
