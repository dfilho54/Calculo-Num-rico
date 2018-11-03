# A MATRIZ DA QUESTÃO ESTÁ NO FINAL DO CÓDIGO!!
# O CÓDIGO VAI CALCULAR QUAL O RESULTADO QUANDO CONVERGIR 

#Recebe a matriz A, o vetor resposta b, o "chute" inicial, elementos na resposta, e o erro.
def gaussSeidel(A, b, x, N, erro): 
    maxInteracao = 1000 #máximo de interações
    x_anterior = [0.0 for i in range(N)]
#verifica se pode executar a interação, caso não tenha chegado ao seu limite.
    for i in range(maxInteracao):
        for j in range(N):
#cada x do result vai ser armazenado em um vetor auxiliar
            x_anterior[j] = x[j]
            soma = 0.0
#loop para calcular o valor da soma de cada item da matriz para achar o "novo" x            
            for k in range(N): 
                if (k != j):
                    soma = soma + A[j][k] * x[k]
#calcula o valor de cada novo x, baseado no resultado e matriz fornecidos
            x[j] = (b[j] - soma) / A[j][j]
            
            #printa o novo x[j] e indica qual a atual interação
            #for j in range(N): 
            #    print (x[j])
            #print (i)        

# Confirmar o resultado!!!!!!               
        for j in range(N):
#diferenca é o valor do novo resultado subtraido do anterior/ semelhante para norma, 
            diferenca = 0.0
            diferenca = diferenca + abs(x[j] - x_anterior[j]) 
            norma = 0.0
            norma = norma + abs(x_anterior[j])                             
        if norma == 0.0:
            norma = 1.0
        norm = diferenca / norma
        
#verifica a condição de parada, com o erro atual sendo calculado pelo norm e o erro sendo fornecido
        if (norm < erro) and i != 0: 
            print("Os resultados convergem para [", end="")
            for j in range(N - 1):
                print(x[j], ",", end="")
            print(x[N - 1], "]. Levou", i + 1, "interações!")
            return
    print("Não convergiu durante o máximo de interações!")

matriz = [[4,0,2,0,-1], [2,9,0,0,-1], [0,2,7,-1,0], [0,2,0,5,-2], [0,3,1,0,9]]
vector = [95, 163,543,-21,657]
result = [0.0, 0.0, 0.0,0.0,0.0]

#Teste de comparação com o Slide sobre Gauss Jacobi.
#matriz = [[10,2,1], [1,5,1], [2,3,10]]
#vector = [7,-8,6]
#result = [0.7, -1.6, 0.6]

gaussSeidel(matriz, vector, result, 5, 0.0005)
