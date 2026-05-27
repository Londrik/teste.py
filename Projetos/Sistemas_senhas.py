from tkinter import *
from tkinter import messagebox

# JANELA PRINCIPAL (CLIENTE)
cliente = Tk()
cliente.title("Solicitar Senha")
cliente.geometry("300x250")
cliente.configure(bg="lightgreen")

# VARIÁVEIS COMPARTILHADAS
contador = 1
fila = []
senha_atual = StringVar()
senha_atual.set("---")

# FUNÇÕES DO SISTEMA
def gerar_senha():
    global contador
    nova_senha = f"S{contador:03d}"
    fila.append(nova_senha)
    lista_admin.insert(END, nova_senha)
    contador += 1
    messagebox.showinfo("Senha Gerada", f"Sua senha é: {nova_senha}")

def chamar_proxima():
    if fila:
        proxima = fila.pop(0)
        senha_atual.set(proxima)
        lista_admin.delete(0)
    else:
        messagebox.showwarning("Aviso", "Não há senhas na fila!")

# INTERFACE CLIENTE
Label(cliente, text="Bem-vindo", bg="lightgreen", font=("Arial", 14, "bold")).pack(pady=20)
Button(cliente, text="Gerar Senha", command=gerar_senha, width=20, height=2).pack(pady=10)

# TELA 2 (ADMINISTRADOR)
admin = Toplevel(cliente)
admin.title("Administrador")
admin.geometry("300x400")
admin.configure(bg="lightgreen")

Label(admin, text="Fila de Senhas", font=("Arial", 14), bg="lightgreen").pack(pady=10)
lista_admin = Listbox(admin, width=20, height=10)
lista_admin.pack(pady=10)

Button(admin, text="Chamar Próxima", command=chamar_proxima, width=20).pack(pady=5)

# TELA 3 (PAINEL)
painel = Toplevel(cliente)
painel.title("Painel de Senhas")
painel.geometry("400x300")
painel.configure(bg="lightgreen")

Label(painel, text="SENHA ATUAL", font=("Arial", 20, "bold"), bg="lightgreen").pack(pady=30)
Label(painel, textvariable=senha_atual, font=("Arial", 60, "bold"), bg="white", width=10).pack(pady=10)

cliente.mainloop()


