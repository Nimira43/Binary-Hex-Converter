print('[*]Binary / Hexadecimal Converter')

max_value = int(input('\n[+]Calculate binary and hexadecimal values up to what number?: '))

decimal = list(range(1, max_value + 1))
binary = []
hexadecimal = []

for num in decimal:
  binary.append(bin(num))
  hexadecimal.append(hex(num))

print('Generating list...')

