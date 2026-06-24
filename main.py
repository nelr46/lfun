import sys

from lexer import lexer
from parser_lfun import parser

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py ficheiro.lf")
        return

    nome_ficheiro = sys.argv[1]

    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as ficheiro:
            codigo = ficheiro.read()

        ast = parser.parse(codigo, lexer=lexer)

        for statement in ast:
            valor, tipo = statement.eval()
            print(f"resultado: {valor} tipo: {tipo}")

    except FileNotFoundError:
        print(f"Erro: ficheiro '{nome_ficheiro}' não encontrado.")

    except Exception as erro:
        print(f"Erro: {erro}")

if __name__ == "__main__":
    main()