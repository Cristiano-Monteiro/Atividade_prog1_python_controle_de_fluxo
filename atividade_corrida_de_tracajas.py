def casos_teste_tamanho(grupo):
    tamanho_lista = len(grupo)
    if(tamanho_lista > 50):
        print('___'*30)
        print('Erro: Tamanho da lista acima do permitido!')
        print('___'*30)
    else:
        casos_teste_velocidade(grupo)

def casos_teste_velocidade(grupo_animais):
    erro = False
    maior_velocidade = 0
    quantidade_grupo = len(grupo_animais)
    for velocidade in range(len(grupo_animais)):
        if(grupo_animais[velocidade] > 25):
            erro = True
            print('Erro: Velocidade {} na linha {} acima do permitido!'.format(grupo_animais[velocidade], velocidade + 1))
        for velocidade in grupo_animais:
            if(velocidade > maior_velocidade):
                maior_velocidade = velocidade

    if(erro):
        print('___'*30)
    else:
        classificacao_corrida(maior_velocidade, quantidade_grupo, grupo_animais)

def classificacao_corrida(maior_velocidade, quantidade_grupo, grupo):
    if(maior_velocidade < 10):
        nivel_mais_veloz = 'Nível 1'
    elif(10 <= maior_velocidade < 15):
        nivel_mais_veloz = 'Nível 2'
    else:
        nivel_mais_veloz = 'Nível 3'

    print('___'*30)
    print('Quantidade de animais:', quantidade_grupo)

    for velocidade in grupo:
        print('=== ',velocidade)

    print('Maior velocidade:', maior_velocidade)
    print('Nível de velocidade do tracajá mais veloz do grupo:', nivel_mais_veloz)

# Tamanho: 7
teste1 = [5, 2, 2, 6, 7, 8, 12]

# Tamanho: 50
teste2 = [5, 2, 2, 6, 7, 8, 12, 1, 9, 5,
          10, 15, 12, 17, 15, 20, 12, 1, 9, 5,
          20, 17, 19, 2, 1, 8, 12, 15, 19, 11,
          24, 12, 11, 5, 17, 19, 14, 7, 3, 13,
          12, 14, 10, 8, 23, 14, 12, 6, 20, 19]

# Tamanho: 65
teste3 = [5, 2, 2, 6, 7, 8, 2, 1, 9, 5,
          1, 5, 2, 7, 5, 2, 2, 1, 9, 5,
          1, 7, 9, 2, 1, 8, 2, 5, 1, 1,
          1, 2, 1, 5, 7, 1, 4, 7, 3, 1,
          2, 4, 1, 8, 3, 4, 1, 6, 2, 5,
          1, 9, 7, 5, 5, 1, 2, 2, 3, 9,
          5, 7, 2, 1, 4]

# Velocidade acima de 25
teste4 = [5, 2, 35, 2, 6, 7, 8, 12, 25]

casos_teste_tamanho(teste1)
casos_teste_tamanho(teste2)
casos_teste_tamanho(teste3)
casos_teste_tamanho(teste4)