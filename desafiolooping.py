#Usando laços de repetição faça um programa que leia as notas C1 , C2 E C3 de 10 alunos e 
# imprima as médias para cada aluno lido e conte quantos possuem média acima de 7.
contador = 0

for i in range(1, 11):
    
        try:
          c1 = float(input("Informe a nota da C1: "))
        except ValueError:
            print ("informe um numero novamente por favor: ")
            continue
        try:
         c2 = float(input("Informe a nota da C2: "))
        
        except ValueError:
           print ("informe um numero por favor: ")
           continue 
        try:
           c3 = float(input("Informe a nota da C3: "))
        except ValueError:
            print ("informe um numero por favor: ")
            continue
        media = (c1 + c2 + c3) / 3
        print(f"Aluno {i}, sua média é {media:.2f}")

        if media < 7:
            media *= 0.60
            avaliacao_final = float(input("Informe a nota da avaliação final: "))
            avaliacao_final *= 0.40
            media_final = media + avaliacao_final
            if media_final >= 4.95:
                print("Aprovado")
            else:
                print("Reprovado")
        else:
            contador += 1
            print("Aprovado sem ressalvas.")

    

print (f"quantidade de alunos que passou sem resalvas foi {contador}")
