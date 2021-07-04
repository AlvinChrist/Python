taknese = input().lower()
last_char = taknese[len(taknese) - 1]
if last_char == 's':
    taknese += 'es'
else:
    taknese += 's'
print(taknese)
