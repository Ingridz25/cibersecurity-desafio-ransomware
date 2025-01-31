import os
import pyaes
import hashlib
from datetime import datetime

# 1. Validação de existência do arquivo criptografado
encrypted_file_name = "teste.txt.encrypted_44788fea"  # Nome do arquivo criptografado
if not os.path.exists(encrypted_file_name):
    print(f"Erro: O arquivo criptografado '{encrypted_file_name}' não foi encontrado.")
    exit()

# 2. Gerenciamento de recursos com 'with' e tratamento de exceções
try:
    # Abrir o arquivo criptografado no modo de leitura binária
    with open(encrypted_file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # 3. Solicitar a chave de criptografia
    key_hex = input("Digite a chave de criptografia (em hexadecimal): ").strip()
    try:
        key = bytes.fromhex(key_hex)  # Converte a chave de hexadecimal para bytes
    except ValueError:
        print("Erro: A chave fornecida não é um valor hexadecimal válido.")
        exit()

    # 4. Modo de operação AES (CTR)
    aes = pyaes.AESModeOfOperationCTR(key)

    # 5. Decriptar o arquivo
    decrypted_data = aes.decrypt(encrypted_data)

    # 6. Gerar o nome do arquivo decriptado
    original_file_name = encrypted_file_name.split(".encrypted_44788fea")[0]  # Remove o sufixo
    decrypted_file_name = f"{original_file_name}_decrypted_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    print(f"Arquivo decriptado será salvo como: {decrypted_file_name}")

    # 7. Salvar o arquivo decriptado
    with open(decrypted_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    # 8. Logs e rastreamento
    print("Processo de decriptação concluído com sucesso!")

except Exception as e:
    # Tratamento de exceções
    print(f"Erro durante o processo de decriptação: {e}")
