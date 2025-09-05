""""
  LeetCode 14 - Longest Common Prefix

    Enunciado:
    Dada uma lista de strings, encontrar o maior prefixo comum entre todas elas.
    Se não houver prefixo comum, retornar uma string vazia "".

    Exemplos:

    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Explanation: As três palavras compartilham o prefixo "fl".

    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: Não existe prefixo comum entre as palavras.

    Abordagem:
    - Primeiro, encontrar a palavra com menor tamanho (ela limita o máximo possível do prefixo).
    - Percorrer as letras dessa palavra, comparando com as letras correspondentes em todas as outras palavras.
    - Se todas tiverem a mesma letra na posição i → adicionar ao prefixo.
    - Caso contrário, interromper a busca.

    Complexidade:
    - Tempo: O(n * m), onde n é o número de strings e m é o tamanho da menor palavra.
    - Espaço: O(1), pois usamos apenas variáveis auxiliares para armazenar o prefixo.



"""



List = ["ab","a"]
Menor_palavra =  min(List, key =len) # esta é a forma em python, possivelmente, tem uma com logica pura, veja esta assim que possivel
letras = " "


#analise se tem mais de duas palavras
if len(List) >= 2: 

    for i in range(len(Menor_palavra)):
            letra = List[0][i]
            if all(palavra[i] == letra for palavra in List):
                letras += letra
                i += 1
            else:
                print(letras)
else:
    letras = List[0]
    print(letras)
    
