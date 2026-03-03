import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")  # dark ou light
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Consulta de CEP")
app.geometry("400x400")

def buscar_cep():
    cep = entrada_cep.get()
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            
            if "erro" not in dados:
                resultado_texto.configure(
                    text=f"Rua: {dados['logradouro']}\n"
                         f"Bairro: {dados['bairro']}\n"
                         f"Cidade: {dados['localidade']}\n"
                         f"Estado: {dados['uf']}"
                )
            else:
                resultado_texto.configure(text="CEP não encontrado.")
        else:
            resultado_texto.configure(text="Erro na requisição.")
    except Exception as e:
        resultado_texto.configure(text=f"Erro: {e}")

# Título
titulo = ctk.CTkLabel(app, text="Consulta de CEP", font=("Arial", 20))
titulo.pack(pady=20)

# Campo de entrada
entrada_cep = ctk.CTkEntry(app, placeholder_text="Digite o CEP")
entrada_cep.pack(pady=10)

# Botão
botao = ctk.CTkButton(app, text="Buscar", command=buscar_cep)
botao.pack(pady=10)

# Resultado
resultado_texto = ctk.CTkLabel(app, text="")
resultado_texto.pack(pady=20)

app.mainloop()
