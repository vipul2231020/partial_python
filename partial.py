from sympy import symbols, simplify, sympify, apart
class PartialFraction:
    def __init__(self, expr_intr):
        self.x = symbols('x')
        self.expr = sympify(expr_intr)
        self.partial = apart(self.expr)

    

    def __str__(self):
        return f"Partial Fraction Decomposition of {self.expr} is {self.partial}"
    
    def __add__(self, other):
        if isinstance(other, PartialFraction):
            new_expr = simplify(self.expr + other.expr)
            return PartialFraction(new_expr)
        else:
            raise TypeError("Operand must be an instance of PartialFraction")
        
    def __sub__(self, other):
        if isinstance(other, PartialFraction):
            new_expr = simplify(self.expr - other.expr)
            return PartialFraction(new_expr)
        else:
            raise TypeError("Operand must be an instance of PartialFraction")
        
    def __mul__(self, other):
        if isinstance(other, PartialFraction):
            new_expr = simplify(self.expr * other.expr)
            return PartialFraction(new_expr)
        else:
            raise TypeError("Operand must be an instance of PartialFraction")
        
    def __truediv__(self, other):
        if isinstance(other, PartialFraction):
            new_expr = simplify(self.expr / other.expr)
            return PartialFraction(new_expr)
        else:
            raise TypeError("Operand must be an instance of PartialFraction")
        
pf1 = PartialFraction("(2*x)/(x**2 -1)")
print(pf1)
