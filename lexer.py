import ply.lex as lex


tokens = (
    "INT",
    "TRUE",
    "FALSE",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LT",
    "GT",
    "LE",
    "GE",
    "EQ",
    "NE",
    "LPAREN",
    "RPAREN",
    "SEMI",
)

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"

t_LE = r"<="
t_GE = r">="
t_EQ = r"=="
t_NE = r"!="
t_LT = r"<"
t_GT = r">"

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_SEMI = r";"

t_ignore = " \t\r"

def t_TRUE(t):
    r"true"
    t.value = True
    return t

def t_FALSE(t):
    r"false"
    t.value = False
    return t

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise Exception(f"Caracter Inválido: {t.value[0]}")

lexer = lex.lex()