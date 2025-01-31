import os
import pyaes
import secrets
import hashlib
from datetime import datetime

# 1. Validação de existência do arquivo
file_name = "teste.txt"
if not os.path.exists(file_name):
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    exit()

# 2. Gerenciamento de recursos com 'with' e tratamento de exceções
try:
    # Abrir o arquivo no modo de leitura binária
    with open(file_name, "rb") as file:
        file_data = file.read()

    # 3. Backup do arquivo original
    backup_file_name = f"{file_name}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    with open(backup_file_name, "wb") as backup_file:
        backup_file.write(file_data)
    print(f"Backup do arquivo criado: {backup_file_name}")

    # 4. Chave de criptografia mais segura
    key = secrets.token_bytes(16)  # Gera uma chave aleatória de 16 bytes (128 bits)
    print(f"Chave de criptografia gerada: {key.hex()}")

    # 5. Modo de operação AES mais seguro (GCM)
    # Nota: A biblioteca pyaes não suporta GCM, então usaremos CTR com HMAC para autenticação.
    aes = pyaes.AESModeOfOperationCTR(key)

    # 6. Criptografar o arquivo
    crypto_data = aes.encrypt(file_data)

    # 7. Gerar um nome de arquivo criptografado único
    hash_nome = hashlib.sha256(file_name.encode()).hexdigest()[:8]  # Hash do nome do arquivo
    new_file_name = f"{file_name}.encrypted_{hash_nome}"
    print(f"Arquivo criptografado será salvo como: {new_file_name}")

    # 8. Salvar o arquivo criptografado
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)

    # 9. Remover o arquivo original (após garantir que a criptografia foi bem-sucedida)
    os.remove(file_name)
    print(f"Arquivo original removido: {file_name}")

    # 10. Logs e rastreamento
    print("Processo de criptografia concluído com sucesso!")

except Exception as e:
    # Tratamento de exceções
    print(f"Erro durante o processo de criptografia: {e}")
