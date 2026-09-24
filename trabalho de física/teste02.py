import tkinter as tk
import math

# Variáveis globais para armazenar os valores do campo magnético
B_H_atual = 32.77  # Valor inicial padrão (40 * cos(-35°))
B_V_atual = -22.94  # Valor inicial padrão (40 * sin(-35°))


def atualizar_bussola(angulo_str=None):
    # Se chamado pelo botão, pega o valor atual do slider
    if angulo_str is None:
        angulo_graus = slider.get()
    else:
        angulo_graus = float(angulo_str)

    # 1. PARTE VISUAL: Girando a agulha na tela
    angulo_rad_desenho = math.radians(angulo_graus - 90)
    centro_x, centro_y = 200, 200
    tamanho_agulha = 120

    ponta_x = centro_x + tamanho_agulha * math.cos(angulo_rad_desenho)
    ponta_y = centro_y + tamanho_agulha * math.sin(angulo_rad_desenho)
    cauda_x = centro_x - tamanho_agulha * math.cos(angulo_rad_desenho)
    cauda_y = centro_y - tamanho_agulha * math.sin(angulo_rad_desenho)

    canvas.coords(agulha_norte, centro_x, centro_y, ponta_x, ponta_y)
    canvas.coords(agulha_sul, centro_x, centro_y, cauda_x, cauda_y)

    label_angulo.config(text=f"Direção da Agulha: {angulo_graus:.0f}°")

    # 2. PARTE FÍSICA: Calculando o efeito do giro no Campo Magnético
    angulo_rad_dir = math.radians(angulo_graus)

    # Decomposição do vetor Horizontal (Bh) usando a direção do giro
    b_norte = B_H_atual * math.cos(angulo_rad_dir)
    b_leste = B_H_atual * math.sin(angulo_rad_dir)

    # Atualizando o texto na tela em tempo real
    texto_vetores = (f"Força no eixo Norte/Sul (Bn): {b_norte:.2f} µT\n"
                     f"Força no eixo Leste/Oeste (Bl): {b_leste:.2f} µT")
    label_comp_giro.config(text=texto_vetores)


def calcular_campo():
    global B_H_atual, B_V_atual
    try:
        texto_b = entry_b.get().strip().replace(",", ".")
        texto_inc = entry_inc.get().strip().replace(",", ".")

        b_total = float(texto_b)
        inclinacao = float(texto_inc)
        inc_rad = math.radians(inclinacao)

        # Calcula as componentes base (Vertical e Horizontal)
        B_H_atual = b_total * math.cos(inc_rad)
        B_V_atual = b_total * math.sin(inc_rad)

        label_resultado.config(text=f"Horizontal Total (Bh): {B_H_atual:.2f} µT  |  Vertical (Bv): {B_V_atual:.2f} µT")

        # Chama a função de giro para atualizar os vetores Norte/Leste com o novo Bh
        atualizar_bussola()

    except ValueError:
        label_resultado.config(text="Erro: Digite apenas números válidos (ex: 40.5)")


# 1. Configuração da Janela Principal
janela = tk.Tk()
janela.title("Física - Simulador Vetorial de Bússola")
janela.geometry("450x760")
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
label_angulo = tk.Label(janela, text="Direção da Agulha: 0°", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_angulo.pack()

slider = tk.Scale(janela, from_=0, to=359, orient=tk.HORIZONTAL, length=350,
                  command=atualizar_bussola, bg="#f0f0f0", highlightthickness=0)
slider.pack()

# Painel de Vetores Dinâmicos (Que mudam com o giro)
label_comp_giro = tk.Label(janela, text="Aguardando giro...", font=("Consolas", 11, "bold"), bg="#d9f2d9", fg="#004d00",
                           pady=5, padx=10, relief="solid", borderwidth=1)
label_comp_giro.pack(pady=5)

# 4. Calculadora de Campo Magnético Terrestre (Base)
frame_calc = tk.LabelFrame(janela, text="Configuração Inicial do Campo Magnético", bg="#f0f0f0",
                           font=("Arial", 10, "bold"), padx=10, pady=10)
frame_calc.pack(pady=5, fill="x", padx=20)

tk.Label(frame_calc, text="Campo Total (B) em µT:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", pady=2)
entry_b = tk.Entry(frame_calc, width=10)
entry_b.grid(row=0, column=1, pady=2, padx=5)
entry_b.insert(0, "40.0")

tk.Label(frame_calc, text="Inclinação Magnética (°):", bg="#f0f0f0").grid(row=1, column=0, sticky="e", pady=2)
entry_inc = tk.Entry(frame_calc, width=10)
entry_inc.grid(row=1, column=1, pady=2, padx=5)
entry_inc.insert(0, "-35.0")

btn_calcular = tk.Button(frame_calc, text="Calcular", command=calcular_campo, bg="#0066cc", fg="white",
                         font=("Arial", 9, "bold"))
btn_calcular.grid(row=0, column=2, rowspan=2, padx=15)

label_resultado = tk.Label(frame_calc, text="Horizontal Total (Bh): 32.77 µT  |  Vertical (Bv): -22.94 µT",
                           bg="#f0f0f0", font=("Arial", 9), fg="#333")
label_resultado.grid(row=2, column=0, columnspan=3, pady=10)

# Inicializa os vetores no eixo 0 na primeira vez que abre o programa
atualizar_bussola("0")

janela.mainloop()