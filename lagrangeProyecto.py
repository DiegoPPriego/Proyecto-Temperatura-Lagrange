# Importamos las bibliotecas necesarias
import sympy as sp
from tkinter import simpledialog, messagebox
import tkinter as tk
import numpy as np

# Definimos la clase LagrangeInterpolator
class LagrangeInterpolator:
    # El método de inicialización de la clase
    def __init__(self, x_values, y_values):
        self.x_values = x_values  # Valores de x
        self.y_values = y_values  # Valores de y
        self.x = sp.symbols('x')  # Símbolo x para usar en sympy

    # Método para calcular un término del polinomio de interpolación
    def calculate_term(self, i):
        term = 1
        for j in range(len(self.x_values)):
            if i != j:
                term *= (self.x - self.x_values[j]) / (self.x_values[i] - self.x_values[j])
        return term

    # Método para calcular el polinomio de interpolación completo
    def interpolate(self):
        polynomial = sum(self.y_values[i] * self.calculate_term(i) for i in range(len(self.x_values)))
        return polynomial.expand()

# Aquí es donde comienza el programa principal
if __name__ == '__main__':
    # Definimos los valores de x e y
    x_values = [1, 2, 3, 4, 5, 6] #Semanas que tenemos
    y_values = [29, 28.85714286, 30.42857143, 26.85714286, 30.5714285714286, 31.7142857142857] #Temperatura promedio máxima

    # Creamos un objeto interpolador y calculamos el polinomio de interpolación
    interpolator = LagrangeInterpolator(x_values, y_values)
    polynomial = interpolator.interpolate()
    print(polynomial)

    # Simplificamos el polinomio
    polinomio_simplificado = sp.simplify(polynomial)

    # Creamos una ventana de Tkinter y la ocultamos
    root = tk.Tk()
    root.withdraw()

    # Pedimos al usuario que introduzca una fecha
    consola: str = simpledialog.askstring("Input", "¿Cuál es el dia que quieres obtener la temperatura?")
    dia, mes_string = consola.split(' de ')

    # Convertimos el día a un número y determinamos el mes
    valor = int(dia)
    mes_numero = 4 if mes_string == "abril" else 5

    # Si el mes es mayo, ajustamos el valor para que sea relativo al inicio de abril
    if mes_numero == 5:
        valor += 30

    # Dependiendo del valor del día, determinamos el rango y los límites inferior y superior
    if valor >= 1 and valor <=7:
        rango = 1
        limite_inferior = 1
        limite_superior = 8
    elif valor >= 8 and valor <=14:
        rango = 2
        limite_inferior = 8
        limite_superior = 15
    elif valor >= 15 and valor <=21:
        rango = 3
        limite_inferior = 15
        limite_superior = 22
    elif valor >= 22 and valor <=28:
        rango = 4
        limite_inferior = 22
        limite_superior = 29
    elif valor >= 29 and valor <=35:
        rango = 5
        limite_inferior = 29
        limite_superior = 36
    elif valor >= 36 and valor <=42:
        rango = 5
        limite_inferior = 36
        limite_superior = 42

    # Calculamos el valor de x basado en el rango y los límites
    valor_de_x = rango+ ((valor-limite_inferior)/(limite_superior-limite_inferior))

    # Sustituimos el valor de x en el polinomio para obtener la temperatura
    valor_en_x = polynomial.subs(interpolator.x, valor_de_x)
    messagebox.showinfo("Resultado", f"La temperatura para el dia {dia} del mes {mes_string} es: {valor_en_x}")

    resultados = []

    # Realizamos pruebas para todos los días desde el 1 de abril hasta el 12 de mayo
    for valor in range(1,43):
        if valor >= 1 and valor <=7:
            rango = 1
            limite_inferior = 1
            limite_superior = 8
        elif valor >= 8 and valor <=14:
            rango = 2
            limite_inferior = 8
            limite_superior = 15
        elif valor >= 15 and valor <=21:
            rango = 3
            limite_inferior = 15
            limite_superior = 22
        elif valor >= 22 and valor <=28:
            rango = 4
            limite_inferior = 22
            limite_superior = 29
        elif valor >= 29 and valor <=35:
            rango = 5
            limite_inferior = 29
            limite_superior = 36
        elif valor >= 36 and valor <=42:
            rango = 5
            limite_inferior = 36
            limite_superior = 42

        # Calculamos el valor de x basado en el rango y los límites
        valor_de_x = rango+ ((valor-limite_inferior)/(limite_superior-limite_inferior))
        
        # Sustituimos el valor de x en el polinomio para obtener la temperatura
        valor_en_x = polynomial.subs(interpolator.x, valor_de_x)

        # Imprimimos la fecha y la temperatura correspondiente
        print(f"{valor if valor <=30 else valor-30} de {'abril' if valor <=30 else 'mayo'}: {valor_en_x}")

        # insertamos el valor resultante en la lista de resultados
        resultados.append(valor_en_x)

    resultados = np.array(resultados)


    valores_reales = [30, 30, 30, 27, 28, 29, 29, 28, 28, 28, 27, 30, 31, 30, 32, 33, 32, 31, 30, 27, 28, 24, 26, 28, 27, 26, 28, 29, 30, 29, 30, 30, 33, 31, 31, 30, 32, 31, 33, 32, 33, 31]


    diferencias = np.abs(resultados-valores_reales).tolist()


    print("\nDiferencias:")
    for valor,diferencia in enumerate(diferencias):
        # Imprimimos la fecha y la diferencia de temperatura correspondiente
        valor+=1
        print(f"{valor if valor <=30 else valor-30} de {'abril' if valor <=30 else 'mayo'}: {diferencia}")
