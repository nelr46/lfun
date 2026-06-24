from lexer import lexer
from parser_lfun import parser

with open("teste.lf", "r", encoding="utf-8") as ficheiro:
    codigo = ficheiro.read()

ast = parser.parse(codigo, lexer=lexer)

for statement in ast:
    value, type_name = statement.eval()
    print(f"resultado: {value} tipo: {type_name}")