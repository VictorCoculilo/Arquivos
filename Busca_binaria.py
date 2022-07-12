from ctypes import sizeof
from io import SEEK_END
from shutil import which
import struct
import sys

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
ufColumn = 5

with open("cep_ordenado.dat","rb") as f:
    f.seek(0, 2)
    posicao = f.tell()
    bloco = posicao // registroCEP.size
    inicio = 0
    fim = bloco-1
    c = 0
    while(inicio<=fim):
        meio = (inicio + fim) // 2
        f.seek(meio * registroCEP.size)
        linha = f.read(registroCEP.size)
        record = registroCEP.unpack(linha)
        c += 1
        if sys.argv[1] >  record[ufColumn].decode('latin1'):
            inicio = meio
        elif sys.argv[1] < record[ufColumn].decode('latin1'):
            fim = meio
        elif sys.argv[1] == record[ufColumn].decode('latin1'):
            print(f"A procura é: {linha}")
            print(f"Numero de procuras: {c}")
        break