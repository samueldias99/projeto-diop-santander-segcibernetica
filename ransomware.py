from cryptography.fernet import Fernet
import os

# 1. Gerar uma chave de criptografia
# IMPORTANTE: Salve essa chave em um local seguro para poder descriptografar depois
chave = Fernet.generate_key()
print(f"Chave gerada: {chave.decode()}") 

# 2. Criar um objeto Fernet com a chave
f = Fernet(chave)

# 3. Ler o conteúdo de um arquivo de teste (ex: 'documento_secreto.txt')
# Use um arquivo que você criou apenas para este teste
with open('documento_secreto.txt', 'rb') as file:
    conteudo_original = file.read()

# 4. Criptografar o conteúdo
conteudo_criptografado = f.encrypt(conteudo_original)

# 5. Salvar o conteúdo criptografado de volta no arquivo
with open('documento_secreto.txt', 'wb') as file:
    file.write(conteudo_criptografado)

print("Arquivo criptografado com sucesso.")