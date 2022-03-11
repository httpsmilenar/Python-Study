#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times, b) Os últimos 4 colocados, c) Times em ordem alfabética e d) Em que posição está o time da Chapecoense.
times = ('corinthians', 'palmeiras', 'santos', 'grêmio',
        'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
        'atlético', 'botafogo', 'atlético-PR', 'bahia',
        'são paulo', 'fluminense', 'sport recife',
        'EC vitória', 'coritiba', 'avaí', 'ponte preta',
        'atlético-GO')
print('-=' * 15)
print(f'lista de times do brasileirão: {times}')
print('-=' * 15)
print(f'os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'o chapecoense está na {times.index("chapecoense")+1}ª posição.')