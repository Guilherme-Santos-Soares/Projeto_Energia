import pandas as pd
import tkinter.messagebox as messagebox
import json

class AplicativoConsumoEnergia:
    def __init__(self):
        self.eletrodomesticos = []
        self.preco_kwh = None

    def adicionar_eletrodomestico(self, nome, potencia, horas):
        try:
            potencia = float(potencia)
            horas = float(horas or 1)
            if potencia <= 0 or horas <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
            return

        self.eletrodomesticos.append({"nome": nome, "potencia": potencia, "horas": horas})
        return f"{nome} adicionado com sucesso!"

    def remover_eletrodomestico(self, indice):
        eletrodomestico = self.eletrodomesticos.pop(indice)
        return f"{eletrodomestico['nome']} removido com sucesso!"

    def simular_consumo(self):
        if not self.eletrodomesticos:
            messagebox.showerror("Erro", "Adicione pelo menos um eletrodoméstico.")
            return

        consumo_total_kwh = sum(eletrodomestico['potencia'] * eletrodomestico['horas'] * 30 for eletrodomestico in self.eletrodomesticos) / 1000
        custo_mensal = consumo_total_kwh * self.preco_kwh
        custo_diario = custo_mensal / 30

        print(f"Consumo Mensal (R$): {custo_mensal:.2f}")
        print(f"Consumo Diário (R$): {custo_diario:.2f}")

    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(self.eletrodomesticos, arquivo)

    def carregar_dados(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                self.eletrodomesticos = json.load(arquivo)
            return True
        except FileNotFoundError:
            messagebox.showerror("Erro", f"Arquivo {nome_arquivo} não encontrado.")
            return False

    def comparar_consumo(self, dados_anteriores, dados_atuais):
        consumo_total_anterior = sum(eletrodomestico['potencia'] * eletrodomestico['horas'] * 30 for eletrodomestico in dados_anteriores) / 1000
        consumo_total_atual = sum(eletrodomestico['potencia'] * eletrodomestico['horas'] * 30 for eletrodomestico in dados_atuais) / 1000

        custo_anterior = consumo_total_anterior * self.preco_kwh
        custo_atual = consumo_total_atual * self.preco_kwh

        return custo_anterior, custo_atual, custo_atual - custo_anterior

    def calcular_consumo(self):
        consumo_total_kwh = sum(eletrodomestico['potencia'] * eletrodomestico['horas'] * 30 for eletrodomestico in self.eletrodomesticos) / 1000
        custo_mensal = consumo_total_kwh * self.preco_kwh
        custo_diario = custo_mensal / 30
        return custo_mensal, custo_diario
