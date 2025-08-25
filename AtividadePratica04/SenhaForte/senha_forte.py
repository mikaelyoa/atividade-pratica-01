while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte! Acesso permitido.")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e 1 número.")