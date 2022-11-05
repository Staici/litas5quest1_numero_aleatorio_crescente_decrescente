lista=[]
for n in range(10):
  n=int(input("Digite um valor aleátorio"))
  lista.append(n)
  
  
print(sorted(lista))
print(sorted(lista, reverse=True))