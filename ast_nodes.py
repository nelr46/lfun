class IntLiteral:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value, "Int"

class BoolLiteral:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value, "Bool"

class BinaryOp:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        left_value, left_type = self.left.eval()
        right_value, right_type = self.right.eval()

        if self.operator in ["+", "-", "*", "/"]:
            if left_type != "Int" or right_type != "Int":
                raise Exception(f"Erro de tipos: operador {self.operator} exige Int e Int")

            if self.operator == "+":
                return left_value + right_value, "Int"

            if self.operator == "-":
                return left_value - right_value, "Int"

            if self.operator == "*":
                return left_value * right_value, "Int"

            if self.operator == "/":
                return left_value // right_value, "Int"

        if self.operator in ["<", ">", "<=", ">="]:
            if left_type != "Int" or right_type != "Int":
                raise Exception(f"Erro de tipos: operador {self.operator} exige Int e Int")

            if self.operator == "<":
                return left_value < right_value, "Bool"

            if self.operator == ">":
                return left_value > right_value, "Bool"

            if self.operator == "<=":
                return left_value <= right_value, "Bool"

            if self.operator == ">=":
                return left_value >= right_value, "Bool"

        if self.operator in ["==", "!="]:
            if left_type != right_type:
                raise Exception(f"Erro de tipos: operador {self.operator} exige operandos do mesmo tipo")

            if self.operator == "==":
                return left_value == right_value, "Bool"

            if self.operator == "!=":
                return left_value != right_value, "Bool"



        raise Exception(f"Operador desconhecido: {self.operator}")
        