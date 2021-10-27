import random
import time

n = list(range(1, 500))

# Embaralha a lista de números
random.shuffle(n)

nBuble = n
nSelection = n
nQuick = n

print("A lista não ordenada é: ", n, "\n")

startBubble = time.time()

def bubble_sort(nBuble):
    # Repassamos a lista tantas vezes quanto os elementos

    for i in range(0, len(nBuble) - 1):
        # Queremos que o último par de elementos adjacentes seja (n-2, n-1)
        for j in range(len(nBuble) - 1):

            if (nBuble[j] > nBuble[j + 1]):
                # Troca
                temp = nBuble[j]
                nBuble[j] = nBuble[j + 1]
                nBuble[j + 1] = temp
    return n

# Chamando a função de classificação por bolha
print("A lista ordenada pelo Bubble Sort: ", bubble_sort(nBuble), "\n")

endBubble = time.time()
print("Tempo decorrido pelo Bubble Sort:", endBubble - startBubble, "\n")

startSelection = time.time()

def selection_sort(nSelection):
    # i indica quantos itens foram classificados
    for i in range(len(nSelection) - 1):
        # Para encontrar o valor mínimo do segmento não classificado
        # Primeiro, assumimos que o primeiro elemento é o mais baixo
        min_index = i
        # Em seguida, usamos j para percorrer os elementos restantes
        for j in range(i + 1, len(nSelection) - 1):
            # Atualize o min_index se o elemento em j for menor que ele
            if nSelection[j] < nSelection[min_index]:
                min_index = j
        # Depois de encontrar o item mais baixo das regiões não classificadas, troque pelo primeiro item não classificado
        nSelection[i], nSelection[min_index] = nSelection[
            min_index], nSelection[i]

selection_sort(nSelection)
# Vamos ver a lista depois de executar a Classificação por Seleção
print("A lista ordenada pelo Seletion Sort: ", nSelection, "\n")

endSelection = time.time()
print("Tempo decorrido pelo Seletion Sort:", endSelection - startSelection,
      "\n")

startQuick = time.time()

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # Se o valor atual que estamos olhando for maior do que o pivô
        # está no lugar certo (lado direito do pivô) e podemos mover para a esquerda,
        # para o próximo elemento.
        # Também precisamos ter certeza de que não ultrapassamos o ponteiro baixo, desde que
        # indica que já movemos todos os elementos para o lado correto do pivô
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Processo oposto ao anterior
        while low <= high and array[low] <= pivot:
            low = low + 1

        # Encontramos um valor para alto e baixo que está fora de ordem
        # ou baixo é maior do que alto, caso em que saímos do loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # O loop continua
        else:
            # Saímos do circuito
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)

quick_sort(nQuick, 0, len(n) - 1)

endQuick = time.time()

print("A lista ordenada pelo Quick Sort: ", nQuick, "\n")
print("Tempo decorrido pelo Quick Sort:", endQuick - startQuick, "\n")
