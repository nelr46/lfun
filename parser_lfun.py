import ply.yacc as yacc

from lexer import tokens
from ast_nodes import IntLiteral, BoolLiteral, BinaryOp


precedence = (
    ("nonassoc", "LT", "GT", "LE", "GE", "EQ", "NE"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
)


def p_program(p):
    """
    program : statements
    """
    p[0] = p[1]


def p_statements_multiple(p):
    """
    statements : statements statement
    """
    p[0] = p[1] + [p[2]]


def p_statements_single(p):
    """
    statements : statement
    """
    p[0] = [p[1]]


def p_statement_expression(p):
    """
    statement : expression SEMI
    """
    p[0] = p[1]


def p_expression_binop(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression LT expression
               | expression GT expression
               | expression LE expression
               | expression GE expression
               | expression EQ expression
               | expression NE expression
    """
    p[0] = BinaryOp(p[2], p[1], p[3])


def p_expression_group(p):
    """
    expression : LPAREN expression RPAREN
    """
    p[0] = p[2]


def p_expression_int(p):
    """
    expression : INT
    """
    p[0] = IntLiteral(p[1])


def p_expression_true(p):
    """
    expression : TRUE
    """
    p[0] = BoolLiteral(p[1])


def p_expression_false(p):
    """
    expression : FALSE
    """
    p[0] = BoolLiteral(p[1])


def p_error(p):
    if p:
        raise Exception(f"Erro sintático perto de '{p.value}'")
    else:
        raise Exception("Erro sintático no fim do ficheiro")


parser = yacc.yacc(debug=False, write_tables=False)