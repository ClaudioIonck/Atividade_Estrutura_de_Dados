import random
import time

def gerar_lista_aleatoria(tamanho):
    return [random.randint(1, 100000) for _ in range(tamanho)]

def gerar_lista_decrescente(tamanho):
    return list(reversed(range(1, tamanho + 1)))

def gerar_lista_crescente(tamanho):
    return list(range(1, tamanho + 1))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerda = arr[:meio]
    direita = arr[meio:]
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivo]
    meio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]
    return quick_sort(esquerda) + meio + quick_sort(direita)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def selection_sort(arr):
    for i in range(len(arr)):
        indice_menor = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[indice_menor]:
                indice_menor = j
        arr[i], arr[indice_menor] = arr[indice_menor], arr[i]

def executar_experimento(cenario, algoritmo, tamanho, num_execucoes=10):
    tempo_total = 0
    for _ in range(num_execucoes):
        if cenario == "aleatorio":
            arr = gerar_lista_aleatoria(tamanho)
        elif cenario == "decrescente":
            arr = gerar_lista_decrescente(tamanho)
        elif cenario == "crescente":
            arr = gerar_lista_crescente(tamanho)
        tempo_inicio = time.time()
        algoritmo(arr)
        tempo_fim = time.time()
        tempo_total += tempo_fim - tempo_inicio
    return tempo_total / num_execucoes

### REPETIR 1 VEZ ###
""" 
tamanho = 100000

algoritmos = [merge_sort, quick_sort, bubble_sort, insertion_sort, selection_sort]

cenarios = ["aleatorio", "decrescente", "crescente"]

for cenario in cenarios:
    print(f"Cenario: {cenario}")
    for algoritmo in algoritmos:
        tempo_medio = executar_experimento(cenario, algoritmo, tamanho)
        print(f"{algoritmo.__name__}: {tempo_medio:.6f} segundos")
    print()
"""
### REPETIR 10 VEZES ###
tamanho = 100000
num_execucoes = 10

algoritmos = [merge_sort, quick_sort, bubble_sort, insertion_sort, selection_sort]
cenarios = ["aleatorio", "decrescente", "crescente"]

for _ in range(10):
    print(f"Cenario {_ + 1}")
    for cenario in cenarios:
        print(f"Cenario: {cenario}")
        for algoritmo in algoritmos:
            tempo_medio = executar_experimento(cenario, algoritmo, tamanho, num_execucoes)
            print(f"{algoritmo.__name__}: {tempo_medio:.6f} segundos")
        print()