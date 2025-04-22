import os                   # importamos o modulo OS

print(os.listdir())         # printamos os diretórios existentes com o os.listdir()

for i in os.listdir():      # usamos o for para iterar sobre os diretórios e exibi-los individualmente no console
    print(i)