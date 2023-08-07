import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext, filedialog
from datetime import datetime

# Lista para armazenar as mensagens
mensagens = []

# Função para criar uma nova mensagem
def criar_mensagem():
    mensagem = simpledialog.askstring("Nova Mensagem", "Digite a sua mensagem:", parent=root)
    if mensagem:
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensagens.append((data_hora, mensagem))
        messagebox.showinfo("Mensagem Criada", "Mensagem criada com sucesso!")

# Função para exibir todas as mensagens salvas
def ver_mensagens():
    mensagem_texto = ""
    for i, (data, mensagem) in enumerate(mensagens):
        mensagem_texto += f"{i}: {data} - {mensagem}\n\n"

    # Criar uma nova janela para exibir mensagens
    janela_mensagens = tk.Toplevel(root)
    janela_mensagens.title("Mensagens Carregadas")
    janela_mensagens.iconbitmap("C:\\sharing_share_icon_255901.ico")

    # Área rolável para exibir mensagens
    text_box = scrolledtext.ScrolledText(janela_mensagens, wrap=tk.WORD, width=60, height=20)
    text_box.insert(tk.INSERT, mensagem_texto)
    text_box.configure(state="disabled")
    text_box.pack()

# Função para salvar as mensagens em um arquivo de texto
def salvar_mensagens():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for data, mensagem in mensagens:
                file.write(f"{data} - {mensagem}\n")

# Função para carregar mensagens de um arquivo de texto
def carregar_mensagens():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if file_path:
        mensagens.clear()
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(" - ", 1)
                if len(parts) == 2:
                    mensagens.append((parts[0], parts[1]))

# Função para exibir as mensagens carregadas em uma janela rolável
def ver_mensagens_carregadas():
    mensagem_texto = ""
    for i, (data, mensagem) in enumerate(mensagens):
        mensagem_texto += f"{i}: {data} - {mensagem}\n\n"

    janela_mensagens_carregadas = tk.Toplevel(root)
    janela_mensagens_carregadas.title("Mensagens Carregadas")
    janela_mensagens_carregadas.iconbitmap("C:\\sharing_share_icon_255901.ico")

    text_box = scrolledtext.ScrolledText(janela_mensagens_carregadas, wrap=tk.WORD, width=60, height=20)
    text_box.insert(tk.INSERT, mensagem_texto)
    text_box.configure(state="disabled")
    text_box.pack()

# Configuração da interface
root = tk.Tk()
root.title("Diário")

# Definir o ícone da janela (substitua "caminho/para/icone.ico" pelo caminho do seu ícone)
root.iconbitmap("C:\\sharing_share_icon_255901.ico")

# Ajustar o tamanho da janela principal
largura_janela = 500
altura_janela = 300
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
x_pos = (largura_tela - largura_janela) // 2
y_pos = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

# Botões
botao1 = tk.Button(root, text="Criar Mensagem", command=criar_mensagem)
botao2 = tk.Button(root, text="Ver Mensagens", command=ver_mensagens)
botao3 = tk.Button(root, text="Salvar Mensagens", command=salvar_mensagens)
botao4 = tk.Button(root, text="Carregar Mensagens", command=carregar_mensagens)
botao5 = tk.Button(root, text="Ver Mensagens Carregadas", command=ver_mensagens_carregadas)
botao1.pack(pady=10)
botao2.pack(pady=10)
botao3.pack(pady=10)
botao4.pack(pady=10)
botao5.pack(pady=10)

# Loop principal da interface
root.mainloop()

