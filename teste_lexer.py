from lexer import lexer

with open("teste.lf", "r", encoding="utf-8") as ficheiro:
    codigo = ficheiro.read()


lexer.input(codigo)

for token in lexer:
    print(token)