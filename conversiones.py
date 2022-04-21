import sys

print(f'archivo: {sys.argv[0]}')

sol = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar = float(sys.argv[3])
peso_chileno = float(sys.argv[4])

print(f'Los {peso_chileno} pesos equivalen a:')
print(f'{sol * peso_chileno} Soles')
print(f'{peso_argentino * peso_chileno} Pesos Argentinos')
print(f'{dolar * peso_chileno} Dólares')