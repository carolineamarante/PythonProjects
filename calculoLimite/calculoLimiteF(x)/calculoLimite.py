import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# Função para calcular o limite padrão (f(x) - f(a)) / (x - a) com a função f(x)
def calcular_limite(f_expr_str, var_str, a):
    # Definir variável simbólica
    var = sp.symbols(var_str)

    # Converter a expressão de f(x) para formato simbólico
    f_expr = sp.sympify(f_expr_str)

    # Calcular o valor de f(a)
    f_a = f_expr.subs(var, a)

    # Definir a expressão de limite (f(x) - f(a)) / (x - a)
    expr_limite = (f_expr - f_a) / (var - a)

    # Calcular o limite
    limite = sp.limit(expr_limite, var, a)

    return limite


# Função para plotar gráfico da função f(x) e ponto de limite
def plotar_funcao_e_limite(f_expr_str, var_str, a, limite):
    # Definir variável simbólica
    var = sp.symbols(var_str)

    # Converter a expressão de f(x) para formato simbólico
    f_expr = sp.sympify(f_expr_str)

    # Criar uma função NumPy a partir da expressão simbólica de f(x)
    f = sp.lambdify(var, f_expr, 'numpy')

    # Gerar valores de x para o gráfico
    x_vals = np.linspace(a - 2, a + 2, 100)

    # Calcular valores de y usando a função f(x)
    y_vals = f(x_vals)

    # Plotar gráfico de f(x)
    plt.figure()
    plt.plot(x_vals, y_vals, label=f'f(x) = {sp.latex(f_expr)}')

    # Calcular o valor de f(a)
    f_a = f_expr.subs(var, a)

    # Marcar o ponto de limite no gráfico
    plt.scatter([a], [f_a], color='r', label=f'lim {var_str} -> {a} = {limite}')
    plt.axvline(a, color='r', linestyle='--')

    # Adicionar a fórmula de f(x) e a fórmula de limite em LaTeX no canto inferior direito do gráfico
    plt.text(0.95, 0.05,
             f"Fórmula de f(x): ${sp.latex(f_expr)}$\nFórmula do limite: $\\lim_{{{var_str} \to {a}}} \\left(\\frac{{f(x) - f({a})}}{{{var_str} - {a}}}\\right)$",
             transform=plt.gca().transAxes, verticalalignment='bottom', horizontalalignment='right',
             fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

    # Configurar título e legendas
    plt.title(f'Função f(x) e limite em {a}')
    plt.xlabel(var_str)
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()


# Solicite ao usuário a função f(x), a variável, e o ponto em que calcular o limite
f_expr_str = input("Digite a função f(x) desejada: ")
var_str = input("Digite a variável da função (por exemplo, 'x'): ")
a = float(input("Insira o ponto que o limite se aproxima: "))

# Calcular o limite com a fórmula (f(x) - f(a)) / (x - a)
limite = calcular_limite(f_expr_str, var_str, a)

# Plotar a função f(x) e o ponto de limite
plotar_funcao_e_limite(f_expr_str, var_str, a, limite)
