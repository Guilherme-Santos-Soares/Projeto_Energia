# Simulador de Consumo de Energia

Este projeto é um simulador de consumo de energia elétrica para eletrodomésticos. Ele permite que os usuários adicionem eletrodomésticos, insiram
a potência e as horas de uso diário, e simulem o consumo mensal e diário em termos de custo.

# Funcionalidades

- Adicionar e remover eletrodomésticos.
- Inserir potência (em watts) e horas de uso diárias para cada eletrodoméstico.
- Calcular e exibir o consumo mensal e diário em reais (R$).
- Salvar e carregar dados de eletrodomésticos de arquivos JSON.
- Comparar consumo de eletrodomésticos entre diferentes períodos.
- Gerar gráficos de consumo mensal por eletrodoméstico.

# Tecnologias Utilizadas

- Python
- Tkinter (para a interface gráfica)
- Matplotlib (para gerar gráficos)
- Pandas (para manipulação de dados)
- JSON (para salvar e carregar dados)

# Estrutura do Projeto

├── energy_consumption_app.py
├── energy_consumption_gui.py
└── README.md

energy_consumption_app.py`: Contém a lógica de negócio do aplicativo.
energy_consumption_gui.py`: Contém a interface gráfica do usuário (GUI).

# Uso

# Adicionando um Eletrodoméstico

1. Insira o nome do eletrodoméstico.
2. Insira a potência (em watts).
3. Insira as horas de uso diário.
4. Insira o preço do kWh (em reais).
5. Clique em "Adicionar Eletrodoméstico".

# Removendo um Eletrodoméstico

1. Selecione o eletrodoméstico na lista.
2. Clique em "Remover Eletrodoméstico".

# Simulando o Consumo

1. Insira o preço do kWh (em reais).
2. Clique em "Simular Consumo".
3. O consumo mensal e diário serão exibidos na interface.

# Salvando Dados

1. Clique em "Salvar Dados".
2. Escolha um nome para o arquivo e salve-o.

# Carregando Dados

1. Clique em "Carregar Dados".
2. Selecione um arquivo JSON previamente salvo.

# Comparando Consumo

1. Clique em "Comparar Consumo".
2. Selecione um arquivo JSON com dados anteriores.
3. Selecione um arquivo JSON com dados atuais.
4. O gráfico de comparação será exibido.

# Exemplo de Uso

1. Adicione alguns eletrodomésticos com suas respectivas potências e horas de uso diário.
2. Simule o consumo e veja os resultados.
3. Salve os dados em um arquivo JSON.
4. Carregue os dados novamente para verificar a persistência das informações.
5. Compare os dados de consumo entre dois arquivos diferentes.


