i = 1
# Enquanto i < 6
while i < 6:
    print(i)
    i = i + 1 #somando i + 1

# Pare o codigo quando i = 3

i = 1
while i < 6:
    print(i)
    if i == 3:
        continue
    i = i + 1

# Break => para o loop
# Continue => pula para o próximo loop

i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue  # pula a impressão do número 3
    print(i)