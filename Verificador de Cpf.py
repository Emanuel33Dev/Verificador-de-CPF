# Interface Grafica
from tkinter import *

# Script
from validate_docbr import CPF
# Inicializar o validador
cpf = CPF()


def verificador_cpf():
    # Verificar se o CPF é valido
    usuario = entry_nome.get()
    verificador_cpf = entry_cpf.get()

    if cpf.validate(verificador_cpf):
        resultado_texto = f'o CPF {verificador_cpf} é válido'
    else:
        resultado_texto = f'O CPF {verificador_cpf} é inválido. Por favor. Digite Novamente'

    label_resultado.config(text=resultado_texto)
    label_usuario.config(text=f'Usuario: {usuario}')
    entry_cpf.delete(0, END) # Limpa o campo CPF


# Nome da Janela
janela = Tk()
janela.title('Verificador de CPF')

# Criar rótulo de entrada
label_nome = Label(janela, text='Digite seu nome: ', bg='black', fg='white')
label_nome.pack()


entry_nome = Entry(janela)
entry_nome.pack()

label_cpf = Label(janela, text='Digite seu CPF: ', bg='black', fg='white')
label_cpf.pack()

entry_cpf = Entry(janela)
entry_cpf.pack()

# Botão para verificar o CPF
botao_verificar = Button(janela, text='Verificar CPF', command=verificador_cpf)
botao_verificar.pack(side='top', pady=10)

# Rótulo para exibir o resultado e o nome de usuário
label_usuario = Label(janela, text="", bg='black', fg='white')
label_usuario.pack()

label_resultado = Label(janela, text="", bg='black', fg='white')
label_resultado.pack()


# Tamanho da janela
janela.geometry('400x210')
janela.wm_maxsize(width=400, height=210)# Tamanho padrão da janela

# Cor da Janela
janela.configure(background='black')

# Inicia o loop da aplicação
janela.mainloop()