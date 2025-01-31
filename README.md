
# 🔐 Desafio de Criptografia - Bootcamp de Cibersegurança da DIO

Este repositório contém dois scripts Python desenvolvidos como parte de um desafio do **Bootcamp de Cibersegurança** da [Digital Innovation One (DIO)](https://www.dio.me/). O objetivo do desafio era criar um **sistema de criptografia e decriptação de arquivos**, aplicando boas práticas de segurança e programação.

---

## 🛠️ Funcionalidades

### **🔹 Encriptação de Arquivos**
- Criptografa um arquivo usando o **algoritmo AES no modo CTR**.
- Gera uma **chave de criptografia segura e aleatória**.
- **Remove o arquivo original** após a criptografia.
- **Cria um backup** do arquivo original antes de criptografá-lo.
- Gera um **nome único** para o arquivo criptografado.

### **🔹 Decriptação de Arquivos**
- Decripta um arquivo criptografado usando a **chave fornecida**.
- **Valida a existência** do arquivo criptografado.
- Gera um **nome único** para o arquivo decriptado.
- **Trata possíveis erros** durante o processo de decriptação.

---

## 📁 Estrutura do Repositório

📌 **`encrypter.py`** → Script para criptografar arquivos.  
📌 **`decrypter.py`** → Script para decriptar arquivos.  
📌 **`README.md`** → Documentação do repositório (este arquivo).  

---

## 🚀 Como Usar

### **📌 Pré-requisitos**
- Python **3.x** instalado.
- Biblioteca `pyaes` instalada. Para instalar, execute:
  ```bash
  pip install pyaes
  ```


### **🔹 Encriptação**
1. Coloque o **arquivo que deseja criptografar** no mesmo diretório do script.
2. Execute o script `encrypter.py`:
   ```bash
   python encrypter.py
   ```
3. **Anote a chave de criptografia** gerada (em hexadecimal).
4. O arquivo criptografado será salvo com um nome único no formato:
   ```
   nome_do_arquivo.encrypted_hash
   ```

### **🔹 Decriptação**
1. Execute o script `decrypter.py`:
   ```bash
   python decrypter.py
   ```
2. **Insira a chave de criptografia** quando solicitado.
3. O arquivo decriptado será salvo com um nome único no formato:
   ```
   nome_do_arquivo_decrypted_timestamp.txt
   ```

## 🔒 Boas Práticas Implementadas

✅ **Validação de existência de arquivos** → Evita erros caso o arquivo não seja encontrado.  
✅ **Gerenciamento de recursos** → Uso de `with` para abrir e fechar arquivos automaticamente.  
✅ **Chave de criptografia segura** → Geração de chaves aleatórias usando a biblioteca `secrets`.  
✅ **Backup do arquivo original** → Cria uma cópia do arquivo antes de criptografá-lo.  
✅ **Logs e rastreamento** → Mensagens de log para acompanhar o processo.  
✅ **Tratamento de exceções** → Captura e exibe erros durante a execução.  

## 📝 Licença
Este projeto está licenciado sob a **MIT License**. Consulte o arquivo `LICENSE` para mais detalhes.

Desenvolvido com 💜 por **Ingrid** como parte do Bootcamp de Cibersegurança da DIO. 🚀
