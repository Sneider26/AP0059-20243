import time 
incio = time.time()

for i in range(1,31):
  conta = 0
  for n in range(1,31):
    residue = i%n
    if residue == 0:
      conta = conta + 1
  if conta == 2:
    print(f'{i} es un primo')
    print("\n")

fin = time.time()
print("t = ", (fin - inicio)*1000)
  
