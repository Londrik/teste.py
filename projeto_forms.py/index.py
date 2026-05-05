from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox

# 1. Configuração da janela principal 
janela = Tk()
janela.title("Cadastro cliente:")
janela.geometry("700x500") # Aumentei um pouco a altura para caber tudo bem

# 2. Criação do Notebook (abas)
abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

# Aba 1 - Cadastro 
aba1 = Frame(abas)
abas.add(aba1, text="Cadastro")

# Aba 2 - Tabela 
aba2 = Frame(abas)
abas.add(aba2, text="Clientes Cadastrados")

### Aba Cadastro 
# Usando um LabelFrame para organizar melhor visualmente
frame_campos = LabelFrame(aba1, text=" Informações do Cliente ", padx=10, pady=10)
frame_campos.pack(pady=20)

Label(frame_campos, text="Nome").pack(anchor="w")
entry_nome = Entry(frame_campos, width=40)
entry_nome.pack(pady=5)

Label(frame_campos, text="Telefone").pack(anchor="w")
entry_telefone = Entry(frame_campos, width=40)
entry_telefone.pack(pady=5)

Label(frame_campos, text="Endereço").pack(anchor="w")
entry_endereco = Entry(frame_campos, width=40)
entry_endereco.pack(pady=5)

Label(frame_campos, text="E-mail").pack(anchor="w")
entry_email = Entry(frame_campos, width=40)
entry_email.pack(pady=5)

Label(frame_campos, text="Cidade").pack(anchor="w")
entry_cidade = Entry(frame_campos, width=40)
entry_cidade.pack(pady=5)

Button(
    aba1,
    text="Cadastrar Cliente",
    bg="#27ae60", # Um verde mais moderno
    fg="white",
    font=("Arial", 10, "bold"),
    width=25,
    command=lambda: messagebox.showinfo("Sucesso", "Dados prontos para salvar!")
).pack(pady=10)

### Aba Tabela (Treeview)
colunas = ("nome", "telefone", "email", "cidade")

tabela = ttk.Treeview(aba2, columns=colunas, show="headings")

# CONFIGURAÇÃO DOS CABEÇALHOS (O que faltava)
tabela.heading("nome", text="Nome Completo")
tabela.heading("telefone", text="Telefone")
tabela.heading("email", text="E-mail")
tabela.heading("cidade", text="Cidade")

# Ajuste opcional da largura das colunas
tabela.column("nome", width=150)
tabela.column("telefone", width=100)
tabela.column("email", width=150)
tabela.column("cidade", width=100)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)

tabela.pack(fill="both", expand=True, padx=10, pady=10)

# 3. O mainloop
janela.mainloop()