#!/bin/bash

# Nome do diretório principal
diretorio_principal="app"

# Criando o diretório principal e subdiretórios
mkdir -p "$diretorio_principal"/{contas,relatorios,utils}

# Criando o arquivo __init__.py no diretório principal
touch "$diretorio_principal"/__init__.py

# Criando o arquivo __init__.py nos diretorios filhos
touch "$diretorio_principal"/contas/__init__.py
touch "$diretorio_principal"/relatorios/__init__.py
touch "$diretorio_principal"/utils/__init__.py

touch "$diretorio_principal"/contas/banco.py
touch "$diretorio_principal"/contas/contas.py
touch "$diretorio_principal"/relatorios/despesas.py
touch "$diretorio_principal"/relatorios/receitas.py

touch "$diretorio_principal"/utils/data.py
touch "$diretorio_principal"/utils/math.py

echo "Estrutura de pastas e arquivos criada com sucesso!"