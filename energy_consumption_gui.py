import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from energy_consumption_app import AplicativoConsumoEnergia

class GUIConsumoEnergia:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Consumo de Energia")
        
        self.app = AplicativoConsumoEnergia()
        self.configurar_ui()

    def configurar_ui(self):
        self.frame = ttk.Frame(self.master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(self.frame, text="Nome do Eletrodoméstico").grid(row=0, column=0)
        ttk.Label(self.frame, text="Potência (W)").grid(row=0, column=1)
        ttk.Label(self.frame, text="Horas de Uso por Dia").grid(row=0, column=2)
        ttk.Label(self.frame, text="Preço do kWh (R$)").grid(row=0, column=3)
        
        self.entrada_nome = ttk.Entry(self.frame)
        self.entrada_nome.grid(row=1, column=0)
        
        self.entrada_potencia = ttk.Entry(self.frame)
        self.entrada_potencia.grid(row=1, column=1)
        
        self.entrada_horas = ttk.Entry(self.frame)
        self.entrada_horas.grid(row=1, column=2)
        
        self.entrada_preco_kwh = ttk.Entry(self.frame)
        self.entrada_preco_kwh.grid(row=1, column=3)
        
        self.botao_adicionar = ttk.Button(self.frame, text="Adicionar Eletrodoméstico", command=self.adicionar_eletrodomestico)
        self.botao_adicionar.grid(row=1, column=4)
        
        self.lista_eletrodomesticos = tk.Listbox(self.frame, width=60, height=15)
        self.lista_eletrodomesticos.grid(row=2, column=0, columnspan=5, pady=10, padx=5)

        ttk.Label(self.frame, text="Consumo Mensal (R$):").grid(row=3, column=0, sticky=tk.E)
        self.label_consumo_mensal = ttk.Label(self.frame, text="")
        self.label_consumo_mensal.grid(row=3, column=1, sticky=tk.W)
        
        ttk.Label(self.frame, text="Consumo Diário (R$):").grid(row=4, column=0, sticky=tk.E)
        self.label_consumo_diario = ttk.Label(self.frame, text="")
        self.label_consumo_diario.grid(row=4, column=1, sticky=tk.W)
        
        self.botao_remover = ttk.Button(self.frame, text="Remover Eletrodoméstico", command=self.remover_eletrodomestico)
        self.botao_remover.grid(row=5, column=0, columnspan=5)
        
        self.botao_simular = ttk.Button(self.frame, text="Simular Consumo", command=self.simular_consumo)
        self.botao_simular.grid(row=6, column=0, columnspan=5)

        self.botao_salvar = ttk.Button(self.frame, text="Salvar Dados", command=self.salvar_dados)
        self.botao_salvar.grid(row=7, column=0, columnspan=2)

        self.botao_carregar = ttk.Button(self.frame, text="Carregar Dados", command=self.carregar_dados)
        self.botao_carregar.grid(row=7, column=2, columnspan=2)

        self.botao_comparar = ttk.Button(self.frame, text="Comparar Consumo", command=self.comparar_consumo)
        self.botao_comparar.grid(row=7, column=4)
        
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)
        self.frame.rowconfigure(2, weight=1)

    def adicionar_eletrodomestico(self):
        nome = self.entrada_nome.get()
        potencia = self.entrada_potencia.get()
        horas = self.entrada_horas.get()
        preco_kwh = self.entrada_preco_kwh.get()
        
        if not nome:
            messagebox.showerror("Erro", "Por favor, insira o nome do eletrodoméstico.")
            return
        
        try:
            potencia = float(potencia)
            horas = float(horas or 1)
            preco_kwh = float(preco_kwh)
            if potencia <= 0 or horas <= 0 or preco_kwh <= 0:  # Corrigido aqui
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos positivos para potência, horas e preço do kWh.")
            return
        
        mensagem = self.app.adicionar_eletrodomestico(nome, potencia, horas)
        messagebox.showinfo("Sucesso", mensagem)
        self.atualizar_lista_eletrodomesticos()

    def remover_eletrodomestico(self):
        indice_selecionado = self.lista_eletrodomesticos.curselection()
        if not indice_selecionado:
            messagebox.showerror("Erro", "Selecione um eletrodoméstico para remover.")
            return
        
        indice = indice_selecionado[0]
        mensagem = self.app.remover_eletrodomestico(indice)
        messagebox.showinfo("Sucesso", mensagem)
        self.atualizar_lista_eletrodomesticos()

    def atualizar_lista_eletrodomesticos(self):
        self.lista_eletrodomesticos.delete(0, tk.END)
        for eletrodomestico in self.app.eletrodomesticos:
            self.lista_eletrodomesticos.insert(tk.END, f"{eletrodomestico['nome']} - Potência: {eletrodomestico['potencia']} W, Horas de Uso: {eletrodomestico['horas']}")

    def salvar_dados(self):
        nome_arquivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Arquivos JSON", "*.json")])
        if nome_arquivo:
            self.app.salvar_dados(nome_arquivo)
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso.")

    def carregar_dados(self):
        nome_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos JSON", "*.json")])
        if nome_arquivo:
            sucesso = self.app.carregar_dados(nome_arquivo)
            if sucesso:
                messagebox.showinfo("Sucesso", "Dados carregados com sucesso.")
                self.atualizar_lista_eletrodomesticos()

    def simular_consumo(self):
        preco_kwh = float(self.entrada_preco_kwh.get())
        if not preco_kwh:
            messagebox.showerror("Erro", "Por favor, insira o preço do kWh.")
            return
        
        self.app.preco_kwh = preco_kwh
        
        consumo_mensal, consumo_diario = self.app.calcular_consumo()
        
        self.label_consumo_mensal.config(text=f"R${consumo_mensal:.2f}")
        self.label_consumo_diario.config(text=f"R${consumo_diario:.2f}")

        self.gerar_grafico_consumo()

        self.app.simular_consumo()

    def comparar_consumo(self):
        nome_arquivo_anterior = filedialog.askopenfilename(filetypes=[("Arquivos JSON", "*.json")])
        if not nome_arquivo_anterior:
            return

        sucesso = self.app.carregar_dados(nome_arquivo_anterior)
        if not sucesso:
            messagebox.showerror("Erro", "Erro ao carregar dados anteriores.")
            return

        dados_anteriores = self.app.eletrodomesticos

        nome_arquivo_atual = filedialog.askopenfilename(filetypes=[("Arquivos JSON", "*.json")])
        if not nome_arquivo_atual:
            return

        sucesso = self.app.carregar_dados(nome_arquivo_atual)
        if not sucesso:
            messagebox.showerror("Erro", "Erro ao carregar dados atuais.")
            return

        dados_atuais = self.app.eletrodomesticos

        if not dados_anteriores or not dados_atuais:
            messagebox.showerror("Erro", "Dados anteriores ou atuais não encontrados ou em formato inválido.")
            return

        try:
            df_anteriores = pd.DataFrame(dados_anteriores)
            df_anteriores['consumo_mensal'] = df_anteriores['potencia'] * df_anteriores['horas'] * 30 / 1000

            df_atuais = pd.DataFrame(dados_atuais)
            df_atuais['consumo_mensal'] = df_atuais['potencia'] * df_atuais['horas'] * 30 / 1000

            fig, eixos = plt.subplots(1, 2, figsize=(14, 5))

            eixos[0].bar(df_anteriores['nome'], df_anteriores['consumo_mensal'], color='blue')
            eixos[0].set_xlabel('Eletrodomésticos')
            eixos[0].set_ylabel('Consumo (kWh/mês)')
            eixos[0].set_title('Consumo Anterior')

            eixos[1].bar(df_atuais['nome'], df_atuais['consumo_mensal'], color='green')
            eixos[1].set_xlabel('Eletrodomésticos')
            eixos[1].set_ylabel('Consumo (kWh/mês)')
            eixos[1].set_title('Consumo Atual')

            plt.show()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao comparar consumos: {str(e)}")

    def gerar_grafico_consumo(self):
        df = pd.DataFrame(self.app.eletrodomesticos)
        df['consumo_mensal'] = df['potencia'] * df['horas'] * 30 / 1000
        
        plt.figure(figsize=(10, 6))
        plt.bar(df['nome'], df['consumo_mensal'])
        plt.xlabel('Eletrodomésticos')
        plt.ylabel('Consumo (kWh/mês)')
        plt.title('Consumo Mensal por Eletrodoméstico')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIConsumoEnergia(root)
    root.mainloop()
