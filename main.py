import time
#InsertionSort
def InsertionSort(A, n):
    pivo = None
    for i in range(1, n-1):
        pivo = A[i]
        j = i-1
        while j>= 0 and A[j] > pivo:
            A[j+1] = A[j]
            j = j-1
            A[j+1] = pivo
    return A
#SelectionSort
def SelectionSort(A, n):
    for i in range(0, n-2):
        i_mim = i
        for j in range(i+1, n-1):
            if A[j] < i_mim:
                i_mim = j
        if A[i] != A[i_mim]:
            aux = A[i]
            A[i] = A[i_mim]
            A[i_mim] = aux
    return A

arquivo = open("num.1000.1.in", "r")
arquivo1 = open("num.10000.1.in", "r")
arquivo2 = open("num.100000.1.in", "r") 
linhas = arquivo.readlines()
linhas1 = arquivo1.readlines()
linhas2 = arquivo2.readlines()
numeros = [int(linha.strip()) for linha in linhas]
numeros1 = [int(linha.strip()) for linha in linhas1]
numeros2 = [int(linha.strip()) for linha in linhas2]
start_time = time.perf_counter()
new_numeros = InsertionSort(numeros, len(numeros))
end_time = time.perf_counter()
start_time2 = time.perf_counter()
new_numeros2 = SelectionSort(numeros, len(numeros))
end_time2 = time.perf_counter()
tempo_execucao = end_time - start_time
tempo_execucao2 = end_time2 - start_time2
print("Tempo InsertionSort: ", tempo_execucao, "\n")
print("Tempo SelectionSort: ", tempo_execucao2, "\n")
start_time = time.perf_counter()
new_numeros = InsertionSort(numeros1, len(numeros1))
end_time = time.perf_counter()
start_time2 = time.perf_counter()
new_numeros2 = SelectionSort(numeros1, len(numeros1))
end_time2 = time.perf_counter()
tempo_execucao = end_time - start_time
tempo_execucao2 = end_time2 - start_time2
print("Tempo InsertionSort: ", tempo_execucao, "\n")
print("Tempo SelectionSort: ", tempo_execucao2, "\n")
start_time = time.perf_counter()
new_numeros = InsertionSort(numeros2, len(numeros2))
end_time = time.perf_counter()
start_time2 = time.perf_counter()
new_numeros2 = SelectionSort(numeros2, len(numeros2))
end_time2 = time.perf_counter()
tempo_execucao = end_time - start_time
tempo_execucao2 = end_time2 - start_time2
print("Tempo InsertionSort: ", tempo_execucao, "\n")
print("Tempo SelectionSort: ", tempo_execucao2, "\n")
