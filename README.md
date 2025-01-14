# Gerador de Ficha de Exercícios

Este projeto é uma aplicação em **Python** com interface gráfica desenvolvida utilizando **Tkinter**. O objetivo é criar fichas personalizadas de exercícios físicos para treinadores e clientes, com opções de exportação para **Excel** e **PDF**.

# Funcionalidades

- **Interface amigável** para adicionar e gerenciar exercícios.
- Banco de dados local **SQLite** para armazenar os exercícios disponíveis.
- Exportação de fichas em formato **Excel** e **PDF**.
- Permite adicionar novos exercícios diretamente pela interface.
- Personalização com informações do treinador, cliente e especificações do treino.

# Pré-requisitos

1. **Python 3.6+** instalado.
2. As seguintes bibliotecas Python:
   - **Tkinter** (já incluída no Python padrão).
   - **SQLite3** (já incluída no Python padrão).
   - **openpyxl** para gerar arquivos Excel:
     ```bash
     pip install openpyxl
     ```
   - **reportlab** para gerar arquivos PDF:
     ```bash
     pip install reportlab
     ```

# Como Executar

## 1. Clone o Repositório

## 2. Execute o Script
bash
Copiar código
python nome_do_script.py
## 3. Interface Gráfica
Ao executar o script, será aberta uma janela onde você pode:

Inserir o nome do treinador e do cliente.
Adicionar exercícios com informações como tipo de treino, repetições, séries, peso e observações.
Gerar a ficha de treino em Excel e PDF.
## 4. Estrutura do Projeto
- Banco de Dados
O banco de dados local exercicios.db armazena a lista de exercícios disponíveis.
A tabela exercicios é criada automaticamente na primeira execução.
- Exportação
Excel: Gerado pelo módulo openpyxl, criando um arquivo chamado Ficha_de_Exercicios.xlsx.
PDF: Gerado pelo módulo reportlab, criando um arquivo chamado Ficha_de_Exercicios.pdf.
## 5. Interface Gráfica
Desenvolvida com Tkinter, inclui:
 ```bash
 - Campos de entrada para nome do treinador e cliente.
 - Campos para seleção de exercícios.
 - Exibição e gerenciamento dos exercícios adicionados.
```
Imagem do aplicativo:
![Img1](https://github.com/paulohique/Gerador-de-Ficha-Academia/assets/107517476/a7ff47ac-cf65-4696-a73d-d5baa9a92c10)
