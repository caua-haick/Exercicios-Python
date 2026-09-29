import tkinter as tk
import math

# Constantes
VELOCIDADE_DA_LUZ = 299792458  # m/s
B_H_FIXO = 32.77  # Valor fixo (µT) apenas para simular os sensores da bússola


# ==========================================
# 1. FUNÇÕES DA BÚSSOLA
# ==========================================
def atualizar_bussola(angulo_str=None):
    if angulo_str is None:
        angulo_graus = slider.get()
    else:
        angulo_graus = float(angulo_str)

    canvas.delete("mostrador")

    centro_x, centro_y = 225, 250
    raio_externo = 130
    raio_texto = 155

    for angulo in range(0, 360, 10):
        rad = math.radians(angulo - 90 - angulo_graus)
        x_ext = centro_x + raio_externo * math.cos(rad)
        y_ext = centro_y + raio_externo * math.sin(rad)

        if angulo % 30 == 0:
            x_int = centro_x + (raio_externo - 15) * math.cos(rad)
            y_int = centro_y + (raio_externo - 15) * math.sin(rad)
            canvas.create_line(x_ext, y_ext, x_int, y_int, fill="black", width=2, tags="mostrador")

            x_txt = centro_x + raio_texto * math.cos(rad)
            y_txt = centro_y + raio_texto * math.sin(rad)

            if angulo == 0:
                canvas.create_text(x_txt, y_txt, text="N", font=("Arial", 14, "bold"), fill="red", tags="mostrador")
            elif angulo == 90:
                canvas.create_text(x_txt, y_txt, text="L", font=("Arial", 14, "bold"), tags="mostrador")
            elif angulo == 180:
                canvas.create_text(x_txt, y_txt, text="S", font=("Arial", 14, "bold"), tags="mostrador")
            elif angulo == 270:
                canvas.create_text(x_txt, y_txt, text="O", font=("Arial", 14, "bold"), tags="mostrador")
            else:
                canvas.create_text(x_txt, y_txt, text=str(angulo), font=("Arial", 10), fill="#555", tags="mostrador")
        else:
            x_int = centro_x + (raio_externo - 7) * math.cos(rad)
            y_int = centro_y + (raio_externo - 7) * math.sin(rad)
            canvas.create_line(x_ext, y_ext, x_int, y_int, fill="#888", width=1, tags="mostrador")

    label_angulo.config(text=f"Você está olhando para: {angulo_graus:.0f}°")

    angulo_rad_dir = math.radians(angulo_graus)
    b_frente_tras = B_H_FIXO * math.cos(angulo_rad_dir)
    b_direita_esq = B_H_FIXO * -math.sin(angulo_rad_dir)

    texto_vetores = f"Leitura dos Sensores Internos:\nFrente/Trás: {b_frente_tras:.2f} µT  |  Dir/Esq: {b_direita_esq:.2f} µT"
    label_comp_giro.config(text=texto_vetores)


def desenhar_ambiente_estatico():
    canvas.create_text(225, 25, text="↑ NORTE GEOGRÁFICO DA TERRA ↑", font=("Arial", 11, "bold"), fill="#d93636")
    canvas.create_text(225, 45, text="Polo SUL Magnético (-)\n(Atrai o Norte da agulha)", font=("Arial", 9),
                       fill="#555", justify="center")

    canvas.create_text(225, 475, text="↓ SUL GEOGRÁFICO DA TERRA ↓", font=("Arial", 11, "bold"), fill="#2980b9")
    canvas.create_text(225, 455, text="Polo NORTE Magnético (+)\n(Emite as linhas de campo)", font=("Arial", 9),
                       fill="#555", justify="center")

    for x in range(45, 420, 45):
        if x != 225:
            canvas.create_line(x, 420, x, 75, fill="#aed6f1", width=2, dash=(5, 5), arrow=tk.LAST)

    canvas.create_oval(75, 100, 375, 400, outline="#333", width=3, fill="white")
    canvas.create_line(225, 250, 225, 130, fill="red", width=6, arrow=tk.LAST)
    canvas.create_line(225, 250, 225, 370, fill="#0066cc", width=6)
    canvas.create_oval(215, 240, 235, 260, fill="black")


# ==========================================
# 2. FUNÇÕES DA FORÇA DE LORENTZ
# ==========================================
def atualizar_forca(*args):
    canvas_3d.delete("all")
    cx, cy = 175, 140

    # Eixos XYZ (Agora com lados positivos e negativos tracejados para todos)

    # Eixo Y (+ para cima, - para baixo na tela)
    canvas_3d.create_line(cx, cy, cx, cy - 110, fill="#ccc", dash=(2, 2))
    canvas_3d.create_line(cx, cy, cx, cy + 110, fill="#ccc", dash=(2, 2))
    canvas_3d.create_text(cx, cy - 120, text="Y", fill="#aaa")

    # Eixo X (+ direita, - esquerda)
    canvas_3d.create_line(cx, cy, cx + 140, cy, fill="#ccc", dash=(2, 2))
    canvas_3d.create_line(cx, cy, cx - 140, cy, fill="#ccc", dash=(2, 2))
    canvas_3d.create_text(cx + 150, cy, text="X", fill="#aaa")

    # Eixo Z (+ diagonal inf-esq, - diagonal sup-dir)
    canvas_3d.create_line(cx, cy, cx - 80, cy + 80, fill="#ccc", dash=(2, 2))
    canvas_3d.create_line(cx, cy, cx + 80, cy - 80, fill="#ccc", dash=(2, 2))
    canvas_3d.create_text(cx - 90, cy + 90, text="Z", fill="#aaa")

    # Legenda
    canvas_3d.create_text(260, 15, text="Legenda:", font=("Arial", 8, "bold"), anchor="w")
    canvas_3d.create_text(260, 30, text="B (Campo)", fill="blue", font=("Arial", 8, "bold"), anchor="w")
    canvas_3d.create_text(260, 45, text="v (Velocidade)", fill="green", font=("Arial", 8, "bold"), anchor="w")
    canvas_3d.create_text(260, 60, text="Fm (Força)", fill="red", font=("Arial", 8, "bold"), anchor="w")

    try:
        b_str = entry_b_lorentz.get().strip().replace(',', '.')
        q_str = entry_q.get().strip().replace(',', '.')
        v_str = entry_v.get().strip().replace(',', '.')

        if not q_str or not v_str or not b_str: return
        b_total_uT = float(b_str)
        q = float(q_str)
        v = float(v_str)

        if abs(v) > VELOCIDADE_DA_LUZ:
            label_forca.config(text="ERRO: Vel > Luz!", fg="red")
            return
        if q == 0:
            label_forca.config(text="ERRO: Carga = 0", fg="red")
            return

        b_tesla = b_total_uT * 1e-6

        angulo_v = slider_theta.get()
        theta_rad = math.radians(angulo_v)

        # Força Fm = q * v * B * sen(θ)
        forca = q * v * b_tesla * math.sin(theta_rad)

        # Atualiza o painel principal
        label_forca.config(text=f"{forca:.2e} N", fg="black")

        # 1. Vetor Campo (B) - Azul
        direcao_b = 1 if b_total_uT >= 0 else -1
        canvas_3d.create_line(cx, cy, cx, cy - (100 * direcao_b), fill="blue", width=3, arrow=tk.LAST)

        # 2. Vetor Velocidade (v) - Verde
        # Agora a direção visual da velocidade inverte se for negativa
        direcao_v = 1 if v >= 0 else -1
        vx = 90 * math.sin(theta_rad) * direcao_v
        vy = -90 * math.cos(theta_rad) * direcao_v
        canvas_3d.create_line(cx, cy, cx + vx, cy + vy, fill="green", width=3, arrow=tk.LAST)

        # 3. Vetor Força (Fm) - Vermelho
        # A força inverte automaticamente se a carga (q), a velocidade (v) ou o campo (b) forem negativos!
        if abs(forca) > 0:
            direcao_f = 1 if forca > 0 else -1
            fx = -75 * direcao_f
            fy = 75 * direcao_f
            canvas_3d.create_line(cx, cy, cx + fx, cy + fy, fill="red", width=3, arrow=tk.LAST)

    except ValueError:
        label_forca.config(text="Valores inválidos", fg="#cc0000")


# ==========================================
# INTERFACE GRÁFICA GERAL
# ==========================================
janela = tk.Tk()
janela.title("Simulador Físico - Bússola e Força de Lorentz")
janela.geometry("920x640")
janela.configure(bg="#f0f0f0")

# --- COLUNA DA ESQUERDA ---
frame_esquerda = tk.Frame(janela, bg="#f0f0f0")
frame_esquerda.pack(side="left", padx=10, pady=10, fill="y")

canvas = tk.Canvas(frame_esquerda, width=450, height=500, bg="#f8fcfd", highlightthickness=1,
                   highlightbackground="#ccc")
canvas.pack()
desenhar_ambiente_estatico()

# --- COLUNA DA DIREITA ---
frame_direita = tk.Frame(janela, bg="#f0f0f0")
frame_direita.pack(side="right", padx=10, pady=10, fill="both", expand=True)

frame_controles = tk.LabelFrame(frame_direita, text="Giro e Sensores da Bússola", bg="#f0f0f0",
                                font=("Arial", 10, "bold"), padx=10, pady=10)
frame_controles.pack(fill="x", pady=(0, 10))

label_angulo = tk.Label(frame_controles, text="Você está olhando para: 0°", font=("Arial", 11, "bold"), bg="#f0f0f0")
label_angulo.pack()

slider = tk.Scale(frame_controles, from_=0, to=359, orient=tk.HORIZONTAL, length=300, command=atualizar_bussola,
                  bg="#f0f0f0", highlightthickness=0)
slider.pack()

label_comp_giro = tk.Label(frame_controles, text="...", font=("Consolas", 9), bg="#d9f2d9", fg="#004d00", pady=5,
                           padx=5, relief="solid", borderwidth=1)
label_comp_giro.pack(pady=5)

frame_lorentz = tk.LabelFrame(frame_direita, text="Força Magnética (Regra da Mão Direita)", bg="#f0f0f0",
                              font=("Arial", 10, "bold"), padx=10, pady=5)
frame_lorentz.pack(fill="both", expand=True)

frame_inputs = tk.Frame(frame_lorentz, bg="#f0f0f0")
frame_inputs.pack(fill="x")

tk.Label(frame_inputs, text="Campo B (µT):", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=2)
entry_b_lorentz = tk.Entry(frame_inputs, width=12)
entry_b_lorentz.grid(row=0, column=1, padx=5, pady=2);
entry_b_lorentz.insert(0, "40.0")
entry_b_lorentz.bind("<KeyRelease>", atualizar_forca)

tk.Label(frame_inputs, text="Carga q (C):", bg="#f0f0f0").grid(row=0, column=2, sticky="w", pady=2)
entry_q = tk.Entry(frame_inputs, width=12)
entry_q.grid(row=0, column=3, padx=5, pady=2);
entry_q.insert(0, "1.6e-19")
entry_q.bind("<KeyRelease>", atualizar_forca)

tk.Label(frame_inputs, text="Veloc. v (m/s):", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=2)
entry_v = tk.Entry(frame_inputs, width=12)
entry_v.grid(row=1, column=1, padx=5, pady=2);
entry_v.insert(0, "5000")
entry_v.bind("<KeyRelease>", atualizar_forca)

tk.Label(frame_inputs, text="Ângulo v/B (°):", bg="#f0f0f0").grid(row=1, column=2, sticky="w", pady=2)
slider_theta = tk.Scale(frame_inputs, from_=0, to=360, orient=tk.HORIZONTAL, length=140, command=atualizar_forca,
                        bg="#f0f0f0", highlightthickness=0)
slider_theta.set(90)
slider_theta.grid(row=1, column=3, padx=5, pady=2)

frame_resultado = tk.Frame(frame_lorentz, bg="white", highlightbackground="black", highlightthickness=2)
frame_resultado.pack(fill="x", padx=10, pady=(10, 5))

tk.Label(frame_resultado, text="FORÇA MAGNÉTICA (Fm)", font=("Arial", 9, "bold"), bg="white", fg="#555").pack(
    pady=(5, 0))

label_forca = tk.Label(frame_resultado, text="0.00e+00 N", font=("Arial", 18, "bold"), bg="white", fg="black")
label_forca.pack(pady=(0, 5))

canvas_3d = tk.Canvas(frame_lorentz, width=350, height=250, bg="white", highlightthickness=1,
                      highlightbackground="#ccc")
canvas_3d.pack(pady=5)

atualizar_bussola("0")
atualizar_forca()

janela.mainloop()