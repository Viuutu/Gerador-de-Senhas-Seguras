import random
import string

def generate_password(length=12, use_special_chars=True, use_numbers=True, use_uppercase=True):
    """Gera uma senha segura de acordo com os critérios fornecidos."""
    
    # Definir os tipos de caracteres a serem incluídos na senha
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Construir o pool de caracteres com base nas preferências do usuário
    pool = lower_chars
    if use_uppercase:
        pool += upper_chars
    if use_numbers:
        pool += digits
    if use_special_chars:
        pool += special_chars

    # Gerar a senha aleatória
    password = ''.join(random.choice(pool) for _ in range(length))

    return password

def main():
    print("Bem-vindo ao Gerador de Senhas Seguras!")
    
    # Solicitar ao usuário os parâmetros para a senha
    length = int(input("Digite o comprimento desejado da senha: "))
    use_special_chars = input("Incluir caracteres especiais? (S/N): ").
