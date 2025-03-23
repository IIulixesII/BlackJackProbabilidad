import tkinter as tk
from tkinter import messagebox

# Función para obtener el valor de la carta
def obtener_valor_carta(carta):
    if carta.upper() == "A":
        return "A"
    elif carta.isdigit() and 2 <= int(carta) <= 10:
        return int(carta)
    else:
        raise ValueError("Carta inválida")

# Función para determinar si se puede dividir las cartas
def Dividir(carta1, carta2, Crupier):
    if carta1 == carta2:  # Solo dividimos si son pares
        if carta1 == 8 and (Crupier == 7 or Crupier >= 10):
            return "Planta"
        elif carta1 == 9:
            return "Dividir"
        elif carta1 == 7 and Crupier >= 7:
            return "Hit"
        elif carta1 == 7:
            return "Dividir"
        elif carta1 == 6 and (Crupier == 2 or Crupier >= 7):
            return "Hit"
        elif carta1 == 6:
            return "Dividir"
        elif carta1 == 5 and Crupier >= 10:
            return "Hit"
        elif carta1 == 5:
            return "Dividir"
        elif carta1 == 4:
            return "Hit"
        elif carta1 == 3 and (Crupier >= 8 or Crupier <= 3):
            return "Hit"
        elif carta1 == 3:
            return "Dividir"
        elif carta1 == 2 and (Crupier >= 8 or Crupier <= 3):
            return "Hit"
        elif carta1 == 2:
            return "Dividir"
        elif carta1 == "A":
            return "Dividir"

    return None  # Si no es par, no se divide

# Función para calcular el total de la mano
def calcular_total(carta1, carta2):
    if (carta1 == "A" and carta2 == 10) or (carta2 == "A" and carta1 == 10):
        return "Blackjack"
    elif (carta1 == "A" and carta2 == 8) or (carta2 == "A" and carta1 == 8):
        return "Planta"
    elif (carta1 == "A" and carta2 == 7) or (carta2 == "A" and carta1 == 7):
        return "A7"
    elif isinstance(carta1, int) and isinstance(carta2, int):
        return carta1 + carta2
    else:
        return f"{carta1}{carta2}".strip()

# Función para tomar la decisión de la jugada
def quehacer(total, Crupier):
    if total == "Blackjack" or total == "Planta":
        return "Planta"
    elif total == "A7":
        if Crupier >= 9:
            return "Hit"
        elif 3 <= Crupier <= 6:
            return "Doble"
        else:
            return "Planta"
    elif total in ["A6", "A5", "A4"]:
        if Crupier >= 7 or Crupier == 2:
            return "Hit"
        elif 3 <= Crupier <= 6:
            return "Doble"
        else:
            return "Planta"
    elif total in ["A3", "A2"]:
        if Crupier >= 7 or Crupier == 2:
            return "Hit"
        elif 5 <= Crupier <= 6:
            return "Doble"
        else:
            return "Planta"
    elif total == "AA":
        return "Dividir"
    elif isinstance(total, int):
        if total <= 8:
            return "Hit"
        elif total == 9 and (Crupier == 2 or Crupier >= 7):
            return "Hit"
        elif total == 9:
            return "Doble"
        elif total == 10 and Crupier <= 10:
            return "Hit"
        elif total == 10:
            return "Doble"
        elif total == 11 and Crupier == 11:
            return "Hit"
        elif total == 11:
            return "Doble"
        elif total == 12 and (Crupier <= 3 or Crupier >= 7):
            return "Hit"
        elif total == 12:
            return "Planta"
        elif 13 <= total <= 17 and Crupier >= 7:
            return "Hit"
        elif 13 <= total <= 17:
            return "Planta"
        elif total >= 17:
            return "Planta"
    else:
        return "Hit"

# Función para manejar la interacción con la interfaz gráfica
def procesar_jugada():
    try:
        carta1 = obtener_valor_carta(entry_carta1.get())
        carta2 = obtener_valor_carta(entry_carta2.get())
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return
    
    try:
        Crupier = int(entry_crupier.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido para el Crupier.")
        return

    total = calcular_total(carta1, carta2)
    dividir_decision = Dividir(carta1, carta2, Crupier)
    
    if dividir_decision:
        resultado = dividir_decision
    else:
        resultado = quehacer(total, Crupier)
    
    label_resultado.config(text=f"Resultado: {resultado}")
    label_cartas.config(text=f"Cartas: {total}")
    label_crupier_2.config(text=f"Crupier: {Crupier}")

# Crear la ventana principal
root = tk.Tk()
root.title("Juego de Blackjack")

# Crear los elementos de la interfaz gráfica
label_carta1 = tk.Label(root, text="Carta 1 (número o 'A' para As):")
label_carta1.pack()
entry_carta1 = tk.Entry(root)
entry_carta1.pack()

label_carta2 = tk.Label(root, text="Carta 2 (número o 'A' para As):")
label_carta2.pack()
entry_carta2 = tk.Entry(root)
entry_carta2.pack()

label_crupier = tk.Label(root, text="Número del Crupier (A = 11):")
label_crupier.pack()
entry_crupier = tk.Entry(root)
entry_crupier.pack()

boton_procesar = tk.Button(root, text="Procesar Jugada", command=procesar_jugada)
boton_procesar.pack()

label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.pack()

label_cartas = tk.Label(root, text="Cartas: ")
label_cartas.pack()

label_crupier_2 = tk.Label(root, text="Crupier: ")
label_crupier_2.pack()

# Iniciar la interfaz gráfica
root.mainloop()
