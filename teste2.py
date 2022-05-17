p1 = 85 
p2 = 50 
p3 = 95 

med = (p1+p2+p3)/3
print("A nota do aluno foi de {0:.2f}".format(med))

if med>=70:
    print("Parabéns, você passou!")
else:
    print("Você foi reprovado!")