import tkinter as tk
from datetime import datetime
import time
import locale

# Configurar o locale para exibir data e hora em português
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Para Linux e Mac
# locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')  # Para Windows

def atualizar_horario():
    agora = datetime.now()
    data_hora_formatada = agora.strftime('%A, %d de %B de %Y  %H:%M:%S')
    label.config(text=data_hora_formatada)
    label.after(1000, atualizar_horario)  # Atualiza a cada 1 segundo

# Criação da janela principal
janela = tk.Tk()
janela.title("Data e Hora em Tempo Real")

# Configuração da interface gráfica
label = tk.Label(janela, font=('Arial', 16), fg='blue')
label.pack(pady=20)

# Inicialização do relógio
atualizar_horario()

# Execução da interface gráfica
janela.mainloop()
