import tkinter as tk
import math


def atualizar_bussola(angulo_str):
    angulo_graus = float(angulo_str)

    # Subtrai 90 graus para alinhar o 0° (Norte) com o eixo Y superior
    angulo_radianos = math.radians(angulo_graus - 90)

    centro_x, centro_y = 200, 200
    tamanho_agulha = 120

    ponta_x = centro_x + tamanho_agulha * math.cos(angulo_radianos)
    ponta_y = centro_y + tamanho_agulha * math.sin(angulo_radianos)

    cauda_x = centro_x - tamanho_agulha * math.cos(angulo_radianos)
    cauda_y = centro_y - tamanho_agulha * math.sin(angulo_radianos)

    canvas.coords(agulha_norte, centro_x, centro_y, ponta_x, ponta_y)
    canvas.coords(agulha_sul, centro_x, centro_y, cauda_x, cauda_y)

    label_angulo.config(text=f"Direção Magnética: {angulo_graus:.0f}°")


def calcular_campo():
    try:
        # Pega os textos, remove espaços extras e troca vírgula por ponto
        texto_b = entry_b.get().strip().replace(",", ".")
        texto_inc = entry_inc.get().strip().replace(",", ".")

        # Converte para número (float)
        b_total = float(texto_b)
        inclinacao = float(texto_inc)

        # Converte a inclinação para radianos
        inc_rad = math.radians(inclinacao)

        # Calcula as componentes do campo magnético
        b_h = b_total * math.cos(inc_rad)
        b_v = b_total * math.sin(inc_rad)

        # Atualiza a interface DIRETAMENTE no label (evita congelamento)
        label_resultado.config(text=f"Horizontal (Bh): {b_h:.2f} µT  |  Vertical (Bv): {b_v:.2f} µT")

    except ValueError:
        # Exibe erro caso o usuário digite letras
        label_resultado.config(text="Erro: Digite apenas números válidos (ex: 40.5)")


# 1. Configuração da Janela Principal
janela = tk.Tk()
janela.title("Simulador de Bússola e Campo Magnético")
janela.geometry("450x700")
janela.configure(bg="#f0f0f0")

# 2. Área da Bússola (Canvas)
canvas = tk.Canvas(janela, width=400, height=400, bg="white", highlightthickness=1, highlightbackground="black")
canvas.pack(pady=10)

canvas.create_oval(50, 50, 350, 350, outline="#333", width=3)
canvas.create_oval(60, 60, 340, 340, outline="#ccc", width=1)

canvas.create_text(200, 30, text="N", font=("Arial", 16, "bold"), fill="red")
canvas.create_text(200, 370, text="S", font=("Arial", 16, "bold"))
canvas.create_text(370, 200, text="L", font=("Arial", 16, "bold"))
canvas.create_text(30, 200, text="O", font=("Arial", 16, "bold"))

agulha_norte = canvas.create_line(200, 200, 200, 80, fill="red", width=6, arrow=tk.LAST)
agulha_sul = canvas.create_line(200, 200, 200, 320, fill="#0066cc", width=6)
canvas.create_oval(190, 190, 210, 210, fill="black")

# 3. Controle da Bússola
label_angulo = tk.Label(janela, text="Direção Magnética: 0°", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_angulo.pack()

slider = tk.Scale(janela, from_=0, to=359, orient=tk.HORIZONTAL, length=350,
                  command=atualizar_bussola, bg="#f0f0f0", highlightthickness=0)
slider.pack()

# 4. Calculadora de Campo Magnético Terrestre
frame_calc = tk.LabelFrame(janela, text="Cálculo do Campo Magnético Terrestre", bg="#f0f0f0",
                           font=("Arial", 10, "bold"), padx=10, pady=10)
frame_calc.pack(pady=15, fill="x", padx=20)

# Entradas de dados
tk.Label(frame_calc, text="Campo Total (B) em µT:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", pady=2)
entry_b = tk.Entry(frame_calc, width=10)
entry_b.grid(row=0, column=1, pady=2, padx=5)
entry_b.insert(0, "40.0")

tk.Label(frame_calc, text="Inclinação Magnética (°):", bg="#f0f0f0").grid(row=1, column=0, sticky="e", pady=2)
entry_inc = tk.Entry(frame_calc, width=10)
entry_inc.grid(row=1, column=1, pady=2, padx=5)
entry_inc.insert(0, "-35.0")

# Botão e Resultado
btn_calcular = tk.Button(frame_calc, text="Calcular", command=calcular_campo, bg="#0066cc", fg="white",
                         font=("Arial", 9, "bold"))
btn_calcular.grid(row=0, column=2, rowspan=2, padx=15)

# Label que receberá o resultado diretamente
label_resultado = tk.Label(frame_calc, text="Aguardando cálculo...", bg="#f0f0f0", font=("Arial", 10, "bold"),
                           fg="#333")
label_resultado.grid(row=2, column=0, columnspan=3, pady=10)

janela.mainloop()