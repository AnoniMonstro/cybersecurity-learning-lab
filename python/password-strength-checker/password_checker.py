import re
from getpass import getpass

print(" Verificando força de senha ")

senha = getpass("Digite sua senha: ")

score = 0

if len(senha) >= 8:
    score += 1

if re.search(r"[a-z]", senha):
    score += 1

if re.search(r"[A-Z]", senha):
    score += 1

if re.search(r"\d", senha):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
    score += 1


print("\n Verificando...")

if score <= 2:
    print(" Senha fraca")
elif score <= 4:
    print(" Senha média")
else:
    print(" Senha forte")
