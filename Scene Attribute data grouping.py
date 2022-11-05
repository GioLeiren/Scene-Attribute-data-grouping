

t, n, k = map(int, input().split())
lista1_atributos = []
lista1 = []
o = []
s = []
u = []

def inicializar_k_medoids(n):
    distancias_pre = []
    distancias_pos = []
    distancias_pre2 = []
    distancias_pos2 = []
    soma = 0
    mais_perto = 0
    mais_perto_index = 0
    for alcance in range(0, n):
        nome = str(input())
        with open('vectors.txt', 'r') as file:
            for line in file:
                file2 = line.split()
                if nome in file2:
                    for coisa in file2:
                        if coisa == file2[0]:
                            lista1_atributos.append(coisa)
                        else:
                            lista1_atributos.append(float(coisa))
                    lista1.append(lista1_atributos[:])
                    lista1_atributos.clear()
    for e in range(0, len(lista1)):
        for f in range(0, len(lista1)):
            for g in range(0, 26):
                a =  (lista1[e][1 + g] - lista1[f][1 + g])
                if a < 0:
                    a *= -1
                soma += a
            distancias_pre.append(soma)
            soma = 0
        distancias_pos.append(distancias_pre[:])
        distancias_pre.clear()
    for g in range(0, len(distancias_pos)):
        distancias_pre2.append(sum(distancias_pos[g]))
    distancias_pos2.append(distancias_pre2[:])
    amaia = distancias_pos2[0]
    mais_perto = min(amaia)
    mais_perto_index = amaia.index(mais_perto)
    print(lista1[mais_perto_index][0])


def build_k_medoids(n):
    nomes_lista = []
    distancias_pre = []
    distancias_pos = []
    distancias_pre2 = []
    distancias_pos2 = []
    lista_S = []
    lista_O = []
    lista_U = []
    soma_maluca1 = []
    soma_maluca2 = []
    distancias_S = []
    distancia_S = 0
    ganho = 0
    ganhos_pre = []
    ganhos_pos = []
    ganhos_pre2 = []
    ganhos_pos2 = []
    soma1 = 0
    soma2 = 0
    mais_perto = 0
    mais_perto_index = 0
    mais_perto2 = 0
    mais_perto_index2 = 0
    for alcance in range(0, n):
        nome = str(input())
        with open('vectors.txt', 'r') as file:
            for line in file:
                file2 = line.split()
                if nome in file2:
                    for coisa in file2:
                        if coisa == file2[0]:
                            lista1_atributos.append(coisa)
                        else:
                            lista1_atributos.append(float(coisa))
                    lista_O.append(lista1_atributos[:])
                    lista1_atributos.clear()
    lista_O.sort()
    for e in range(0, len(lista_O)):
        for f in range(0, len(lista_O)):
            for g in range(0, 26):
                a = (lista_O[e][1 + g] - lista_O[f][1 + g])
                if a < 0:
                    a *= -1
                soma1 += a
            distancias_pre.append(soma1)
            soma1 = 0
        distancias_pos.append(distancias_pre[:])
        distancias_pre.clear()
    for g in range(0, len(distancias_pos)):
        distancias_pre2.append(sum(distancias_pos[g]))
    distancias_pos2.append(distancias_pre2[:])
    amaia = distancias_pos2[0]
    mais_perto = min(amaia)
    mais_perto_index = amaia.index(mais_perto)
    lista_S.append(lista_O[mais_perto_index])
    nomes_lista.append(lista_O[mais_perto_index][0])
    lista_O.remove(lista_O[mais_perto_index])
    for pum in range(0, k-1):
        for e in range(0, len(lista_O)):
            for coisa in range(0, len(lista_S)):
                for pericles in range(0, 26):
                    ab = (lista_O[e][1 + pericles] - lista_S[coisa][1 + pericles])
                    if ab < 0:
                        ab *= -1
                    soma2 += ab
                soma_maluca1.append(soma2)
                soma2 = 0
            soma_maluca2.append(soma_maluca1[:])
            soma_maluca1.clear()
            distancia_S = min(soma_maluca2[e])
            distancias_S.append(distancia_S)

        for estamos in range(0, len(lista_O)):
            for quase in range(0, len(lista_O)):
                for la in range(0, 26):
                    abc = (lista_O[estamos][1 + la] - lista_O[quase][1 + la])
                    if abc < 0:
                        abc *= -1
                    soma2 += abc
                distancias_pre.append(soma2)
                ganho = distancias_S[quase] - soma2
                if ganho <= 0:
                    ganhos_pre.append(0.0)
                elif ganho == distancias_S[quase]:
                    ganhos_pre.append(0.0)
                else:
                    ganhos_pre.append(ganho)
                soma2 = 0
            ganhos_pos.append(ganhos_pre[:])
            ganhos_pre.clear()

        for raio in range(0, len(ganhos_pos)):
            ganhos_pre2.append(sum(ganhos_pos[raio]))
        ganhos_pos2.append(ganhos_pre2[:])
        amaia2 = ganhos_pos2[0]
        mais_perto2 = max(amaia2)
        mais_perto_index2 = amaia2.index(mais_perto2)
        lista_S.append(lista_O[mais_perto_index2])
        nomes_lista.append(lista_O[mais_perto_index2][0])
        lista_O.remove(lista_O[mais_perto_index2])

        soma_maluca1 = []
        soma_maluca2 = []
        distancias_S = []
        distancia_S = 0
        ganho = 0
        ganhos_pre = []
        ganhos_pos = []
        ganhos_pre2 = []
        ganhos_pos2 = []
        soma2 = 0
        mais_perto = 0
        mais_perto_index = 0
        mais_perto2 = 0
        mais_perto_index2 = 0
    nomes_lista.sort()
    for morre_diabo in nomes_lista:
        print(morre_diabo)

def impressao_k_medoids(n):
    nomes_lista = []
    distancias_pre = []
    distancias_pos = []
    distancias_pre2 = []
    distancias_pos2 = []
    lista_S = []
    lista_O = []
    lista_U = []
    soma_maluca1 = []
    soma_maluca2 = []
    distancias_S = []
    distancia_S = 0
    ganho = 0
    ganhos_pre = []
    ganhos_pos = []
    ganhos_pre2 = []
    ganhos_pos2 = []
    soma1 = 0
    soma2 = 0
    mais_perto = 0
    mais_perto_index = 0
    mais_perto2 = 0
    mais_perto_index2 = 0
    lista_pre_manezilda = []
    lista_manezilda = []
    soma_dist = 0
    vetores_pertencentes_as_medoids = {}
    vetor_S_distancia = []
    lista_semi_final = []
    lista_final = []
    for alcance in range(0, n):
        nome = str(input())
        with open('vectors.txt', 'r') as file:
            for line in file:
                file2 = line.split()
                if nome in file2:
                    for coisa in file2:
                        if coisa == file2[0]:
                            lista1_atributos.append(coisa)
                        else:
                            lista1_atributos.append(float(coisa))
                    lista_O.append(lista1_atributos[:])
                    lista1_atributos.clear()
    lista_O.sort()
    for e in range(0, len(lista_O)):
        for f in range(0, len(lista_O)):
            for g in range(0, 26):
                a = (lista_O[e][1 + g] - lista_O[f][1 + g])
                if a < 0:
                    a *= -1
                soma1 += a
            distancias_pre.append(soma1)
            soma1 = 0
        distancias_pos.append(distancias_pre[:])
        distancias_pre.clear()
    for g in range(0, len(distancias_pos)):
        distancias_pre2.append(sum(distancias_pos[g]))
    distancias_pos2.append(distancias_pre2[:])
    amaia = distancias_pos2[0]
    mais_perto = min(amaia)
    mais_perto_index = amaia.index(mais_perto)
    lista_S.append(lista_O[mais_perto_index])
    nomes_lista.append(lista_O[mais_perto_index][0])
    lista_O.remove(lista_O[mais_perto_index])
    for pum in range(0, k - 1):
        for e in range(0, len(lista_O)):
            for coisa in range(0, len(lista_S)):
                for pericles in range(0, 26):
                    ab = (lista_O[e][1 + pericles] - lista_S[coisa][1 + pericles])
                    if ab < 0:
                        ab *= -1
                    soma2 += ab
                soma_maluca1.append(soma2)
                soma2 = 0
            soma_maluca2.append(soma_maluca1[:])
            soma_maluca1.clear()
            distancia_S = min(soma_maluca2[e])
            distancias_S.append(distancia_S)

        for estamos in range(0, len(lista_O)):
            for quase in range(0, len(lista_O)):
                for la in range(0, 26):
                    abc = (lista_O[estamos][1 + la] - lista_O[quase][1 + la])
                    if abc < 0:
                        abc *= -1
                    soma2 += abc
                distancias_pre.append(soma2)
                ganho = distancias_S[quase] - soma2
                if ganho <= 0:
                    ganhos_pre.append(0.0)
                elif ganho == distancias_S[quase]:
                    ganhos_pre.append(0.0)
                else:
                    ganhos_pre.append(ganho)
                soma2 = 0
            ganhos_pos.append(ganhos_pre[:])
            ganhos_pre.clear()

        for raio in range(0, len(ganhos_pos)):
            ganhos_pre2.append(sum(ganhos_pos[raio]))
        ganhos_pos2.append(ganhos_pre2[:])
        amaia2 = ganhos_pos2[0]
        mais_perto2 = max(amaia2)
        mais_perto_index2 = amaia2.index(mais_perto2)
        lista_S.append(lista_O[mais_perto_index2])
        nomes_lista.append(lista_O[mais_perto_index2][0])
        lista_O.remove(lista_O[mais_perto_index2])

        soma_maluca1 = []
        soma_maluca2 = []
        distancias_S = []
        distancia_S = 0
        ganho = 0
        ganhos_pre = []
        ganhos_pos = []
        ganhos_pre2 = []
        ganhos_pos2 = []
        soma2 = 0
        mais_perto = 0
        mais_perto_index = 0
        mais_perto2 = 0
        mais_perto_index2 = 0
    nomes_lista.sort()
    with open('vectors.txt', 'r') as file2:
        for line2 in file2:
            file3 = line2.split()
            for tumbalaka in nomes_lista:
                if tumbalaka in file3:
                    for coisa2 in file3:
                        if coisa2 == file3[0]:
                            lista_pre_manezilda.append(coisa2)
                        else:
                            lista_pre_manezilda.append(float(coisa2))
                    lista_manezilda.append(lista_pre_manezilda[:])
                    lista_pre_manezilda.clear()
    lista_manezilda.sort()
    for vetor in nomes_lista:
        vetores_pertencentes_as_medoids[vetor] = ''
        lista_semi_final.append(vetor)
        lista_final.append(lista_semi_final[:])
        lista_semi_final.clear()
    for um in range(len(lista_O)):
        for dois in range(len(lista_manezilda)):
            for tres in range(0, 26):
                distancia = (lista_O[um][1 + tres] - lista_manezilda[dois][1 + tres])
                if distancia < 0:
                    distancia *= -1
                soma_dist += distancia
            vetor_S_distancia.append(soma_dist)
            soma_dist = 0
        menor_distancia_ate_S = min(vetor_S_distancia)
        index = vetor_S_distancia.index(menor_distancia_ate_S)
        lista_final[index].append(lista_O[um][0])
        vetores_pertencentes_as_medoids[lista_manezilda[index][0]] = lista_final[index][1:]
        vetor_S_distancia.clear()
    for chave, valor in vetores_pertencentes_as_medoids.items():
        print(chave)
        if valor != '':
            for nomes in valor:
                print(f'  {nomes}')

if t == 1:
    inicializar_k_medoids(n)

elif t == 2:
    build_k_medoids(n)

elif t == 3:
    impressao_k_medoids(n)