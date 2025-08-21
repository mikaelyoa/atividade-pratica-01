n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = (n1*2 + n2*3 + n3*4 + n4*1)/10
print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input("Nota do exame: "))
    print("Nota do exame: {:.1f}".format(exame))
    media_final = (media + exame)/2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media_final))