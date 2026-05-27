import tkinter as tk
from tkinter import ttk, messagebox

class SistemaPacientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro de Pacientes")
        self.root.geometry("800x600")

        # Configuração das Abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.aba_cadastro = ttk.Frame(self.notebook)
        self.aba_listagem = ttk.Frame(self.notebook)

        self.notebook.add(self.aba_cadastro, text="Cadastro do Paciente")
        self.notebook.add(self.aba_listagem, text="Pacientes Cadastrados")

        # Variáveis para armazenar dados
        self.dados_pacientes = []
        
        self.setup_aba_cadastro()
        self.setup_aba_listagem()

    def setup_aba_cadastro(self):
        # Container centralizado
        frame_form = ttk.LabelFrame(self.aba_cadastro, text="Informações Pessoais")
        frame_form.pack(padx=20, pady=20, fill="x")

        campos = [
            ("Nome Completo:", "nome"),
            ("CPF:", "cpf"),
            ("Data de Nascimento:", "nascimento"),
            ("Telefone:", "telefone"),
            ("Email:", "email"),
            ("Convênio/SUS:", "convenio"),
            ("Contato de Emergência:", "emergencia")
        ]

        self.entries = {}

        for i, (label_text, key) in enumerate(campos):
            lbl = ttk.Label(frame_form, text=label_text)
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            
            ent = ttk.Entry(frame_form, width=40)
            ent.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            self.entries[key] = ent

        btn_salvar = ttk.Button(self.aba_cadastro, text="Salvar Cadastro", command=self.salvar_paciente)
        btn_salvar.pack(pady=10)

    def setup_aba_listagem(self):
        # Definição das colunas da Treeview
        colunas = ("nome", "cpf", "nascimento", "telefone", "email", "convenio", "emergencia")
        
        self.tree = ttk.Treeview(self.aba_listagem, columns=colunas, show="headings")
        
        # Cabeçalhos
        self.tree.heading("nome", text="Nome")
        self.tree.heading("cpf", text="CPF")
        self.tree.heading("nascimento", text="Nascimento")
        self.tree.heading("telefone", text="Telefone")
        self.tree.heading("email", text="Email")
        self.tree.heading("convenio", text="Convênio")
        self.tree.heading("emergencia", text="Emergência")

        # Ajuste de largura das colunas
        for col in colunas:
            self.tree.column(col, width=100)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.aba_listagem, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(expand=True, fill="both", side="left")
        scrollbar.pack(side="right", fill="y")

    def salvar_paciente(self):
        # Coleta de dados
        dados = {k: v.get() for k, v in self.entries.items()}

        # Validação simples de campos vazios
        if any(not v.strip() for v in dados.values()):
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios!")
            return

        # Adiciona à lista "banco de dados"
        self.dados_pacientes.append(dados)

        # Atualiza a Treeview
        self.tree.insert("", "end", values=list(dados.values()))

        # Limpa os campos
        for ent in self.entries.values():
            ent.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
        self.notebook.select(1)  # Muda para a aba de listagem automaticamente

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaPacientes(root)
    root.mainloop()