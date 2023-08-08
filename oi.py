import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext, filedialog
from datetime import datetime
import os

# Lista para armazenar as mensagens
mensagens = []

# Diretório padrão para salvar e carregar mensagens
diretorio_mensagens = ""

# Função para criar uma nova mensagem
def criar_mensagem():
    mensagem = simpledialog.askstring("Nova Mensagem", "Digite a sua mensagem:", parent=root)
    if mensagem:
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensagens.append((data_hora, mensagem))
        salvar_mensagens_arquivo()  # Salvar as mensagens no arquivo
        messagebox.showinfo("Mensagem Criada", "Mensagem criada com sucesso!")

# Função para exibir todas as mensagens salvas
def exibir_mensagens(mensagens):
    mensagem_texto = ""
    for i, (data, mensagem) in enumerate(mensagens):
        mensagem_texto += f"{i}: {data} - {mensagem}\n\n"
    return mensagem_texto

# Função para exibir janela com mensagens
def exibir_janela_mensagens(titulo, mensagem_texto):
    janela_mensagens = tk.Toplevel(root)
    janela_mensagens.title(titulo)
    janela_mensagens.iconbitmap("C:\\sharing_share_icon_255901.ico")
    janela_mensagens.geometry("1920x1080")  # Definir tamanho da janela

    # Área rolável para exibir mensagens
    text_box = scrolledtext.ScrolledText(janela_mensagens, wrap=tk.WORD, width=150, height=40)  # Ajustar largura e altura
    text_box.insert(tk.INSERT, mensagem_texto)
    text_box.configure(state="disabled")
    text_box.pack()

# Função para exibir todas as mensagens salvas
def ver_mensagens():
    mensagem_texto = exibir_mensagens(mensagens)
    exibir_janela_mensagens("Mensagens Carregadas", mensagem_texto)

# Função para exibir mensagens carregadas
def ver_mensagens_carregadas():
    mensagem_texto = exibir_mensagens(mensagens)
    exibir_janela_mensagens("Mensagens Carregadas", mensagem_texto)

# Função para salvar as mensagens em um arquivo de texto
def salvar_mensagens_arquivo():
    file_path = os.path.join(diretorio_mensagens, "mensagens.txt")
    with open(file_path, "w") as file:
        for data, mensagem in mensagens:
            file.write(f"{data} - {mensagem}\n")

# Função para carregar mensagens de um arquivo de texto
def carregar_mensagens():
    file_path = filedialog.askopenfilename(initialdir=diretorio_mensagens, filetypes=[("Arquivos de Texto", "*.txt")])
    if file_path:
        mensagens.clear()
        try:
            with open(file_path, "r") as file:
                content = file.read()
                mensagens.append(content)
            messagebox.showinfo("Mensagens Carregadas", "Mensagens foram carregadas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro ao Carregar Mensagens", f"Ocorreu um erro ao carregar as mensagens: {str(e)}")

# Função para selecionar o diretório de mensagens
def selecionar_diretorio():
    global diretorio_mensagens
    diretorio_mensagens = filedialog.askdirectory(title="Selecione o Diretório de Mensagens")
    carregar_arquivos_txt_diretorio(diretorio_mensagens)

# Função para carregar arquivos .txt no diretório
def carregar_arquivos_txt_diretorio(diretorio):
    lista_arquivos.delete(0, tk.END)  # Limpar a lista de arquivos
    for filename in os.listdir(diretorio):
        if filename.endswith(".txt"):
            lista_arquivos.insert(tk.END, filename)

# Função para visualizar o conteúdo do arquivo selecionado
def visualizar_conteudo_arquivo():
    selected_file = lista_arquivos.get(tk.ACTIVE)
    if selected_file:
        file_path = os.path.join(diretorio_mensagens, selected_file)
        with open(file_path, "r") as file:
            content = file.read()
            exibir_janela_mensagens(selected_file, content)

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
botao3 = tk.Button(root, text="Salvar Mensagens", command=salvar_mensagens_arquivo)
botao4 = tk.Button(root, text="Carregar Mensagens", command=carregar_mensagens)
botao5 = tk.Button(root, text="Ver Mensagens Carregadas", command=ver_mensagens_carregadas)
botao6 = tk.Button(root, text="Selecionar Diretório", command=selecionar_diretorio)
botao7 = tk.Button(root, text="Visualizar Arquivo Selecionado", command=visualizar_conteudo_arquivo)
botao1.pack(pady=10)
botao2.pack(pady=10)
botao3.pack(pady=10)
botao4.pack(pady=10)
botao5.pack(pady=10)
botao6.pack(pady=10)
botao7.pack(pady=10)

# Criação da lista de arquivos
lista_arquivos = tk.Listbox(root, selectmode=tk.SINGLE)
lista_arquivos.pack(pady=10)

# Função para carregar e exibir os arquivos da pasta selecionada
def carregar_arquivos_pasta():
    try:
        global diretorio_mensagens
        diretorio_mensagens = filedialog.askdirectory(title="Selecione a Pasta com Arquivos TXT")
        arquivos_txt = [arquivo for arquivo in os.listdir(diretorio_mensagens) if arquivo.lower().endswith('.txt')]
        lista_arquivos.delete(0, tk.END)
        for arquivo in arquivos_txt:
            lista_arquivos.insert(tk.END, arquivo)
    except Exception as e:
        messagebox.showerror("Erro ao Carregar Arquivos", f"Ocorreu um erro ao carregar os arquivos: {str(e)}")

# Botão para carregar arquivos da pasta selecionada
botao_carregar_arquivos = tk.Button(root, text="Carregar Arquivos da Pasta", command=carregar_arquivos_pasta)
botao_carregar_arquivos.pack(pady=10)

# Função para exibir o conteúdo do arquivo selecionado na lista
def exibir_conteudo_arquivo_selecionado():
    selected_file = lista_arquivos.get(tk.ACTIVE)
    if selected_file:
        file_path = os.path.join(diretorio_mensagens, selected_file)
        with open(file_path, "r") as file:
            content = file.read()
            exibir_janela_mensagens(selected_file, content)

# Botão para exibir conteúdo do arquivo selecionado
botao8 = tk.Button(root, text="Exibir Conteúdo do Arquivo Selecionado", command=exibir_conteudo_arquivo_selecionado)
botao8.pack(pady=10)

# Loop principal da interface
root.mainloop()

