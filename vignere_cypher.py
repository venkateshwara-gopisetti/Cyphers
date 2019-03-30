import sys



def vigenere_cipher(msg,cipher):

    alp = list(map(chr, range(97, 123)))

    key = [cipher[x%len(cipher)] for x in range(len(msg))]

    vs = {}

    for i in range(len(alp)):

        for j in range(len(alp)):

            vs[alp[i]+alp[j]] = alp[(i+j)%26]

    return(''.join([vs[x+y] for x,y in zip(msg,key)]))



print(vigenere_cipher(sys.argv[1],sys.argv[2]))