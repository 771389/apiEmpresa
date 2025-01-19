import json
import re

# Função para corrigir o telefone (remover espaços extras e palavras como 'Whatsapp')
def corrigir_telefone(telefone):
    # Remover qualquer coisa que não seja número (incluindo espaços e palavras como "Whatsapp")
    telefone_corrigido = re.sub(r'\D', '', telefone)  # Remove qualquer caractere não numérico
    return telefone_corrigido

# Função para corrigir o arquivo JSON
def corrigir_json_telefone(input_file, output_file):
    # Abrir e carregar o JSON original
    with open(input_file, 'r', encoding='utf-8') as file:
        dados = json.load(file)

    # Iterar sobre os dados e corrigir os telefones
    for item in dados:
        if 'telefone' in item:
            item['telefone'] = corrigir_telefone(item['telefone'])
    
    # Salvar os dados corrigidos em um novo arquivo JSON
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

# Nome do arquivo de entrada e saída
input_file = 'EmpresasSP.json'  # Arquivo JSON original
output_file = 'EmpresasSP_corrigido.json'  # Arquivo JSON corrigido

# Chamar a função para corrigir o telefone no arquivo
corrigir_json_telefone(input_file, output_file)

print(f'Arquivo JSON corrigido foi salvo como {output_file}')
