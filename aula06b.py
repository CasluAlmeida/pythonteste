n = input('Digite algo: ')

print(f'''O tipo primitivo do que você escreveu é {type(n)}
Essa informação é numerica: {n.isnumeric()}
Todos os caracteres digitados são letras do alfabeto {n.isalpha()}
Todos os caracteres digitados estão em maiúsculo {n.isupper()}
Todos os caracteres digitados estão em minúsculo {n.islower()}
''')
