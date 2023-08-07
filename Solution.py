class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def menor(strs):
            aux = len(strs[0])
            for i in strs:
                if len(i) < aux:
                    aux = len(i)
            return aux
        tam_menor_palavra = menor(strs)
        index_letra = 0
        letra_iguais = True
        while letra_iguais:
            for i in range(len(strs)):
                if index_letra < tam_menor_palavra:
                    if i != 0:
                        if anterior != strs[i][index_letra]:
                            letra_iguais = False
                            break                   
                    else:
                        anterior = strs[i][index_letra]
                else:
                    letra_iguais = False
            
            if letra_iguais:
                index_letra +=1
        return strs[0][:index_letra:]
