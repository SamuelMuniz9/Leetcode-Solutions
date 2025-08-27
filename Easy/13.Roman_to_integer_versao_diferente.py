"""
    LeetCode 13 - Roman to Integer

    Enunciado:
    Converter um número romano (string) para um número inteiro.

    Exemplo:


    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    Example 1:

    Input: s = "III"
    Output: 3
    Explanation: III = 3.
    Example 2:

    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    Example 3:

    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    

   Abordagem:
    - Percorrer a string de trás para frente (direita para esquerda).
    - Manter o valor do símbolo anterior para decidir se o símbolo atual
      deve ser somado ou subtraído do total:
        * Se o valor atual < valor anterior → subtrai
        * Caso contrário → soma
    - Isso cobre todos os casos de subtração especial automaticamente (IV, IX, XL, XC, CD, CM).

    Complexidade:
    - Tempo: O(n), onde n é o tamanho da string `s`, pois percorremos cada caractere uma vez.
    - Espaço: O(1), já que usamos apenas um dicionário fixo de valores.

    """
s="XIV"

valores = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

total = 0
anterior = ""

for i in s[::-1]:
    if total == 0:
        anterior = i
        total = valores[i]
    elif valores[anterior] > valores[i]:
        anterior = i
        total -= valores[i]
    else:  # valores[anterior] <= valores[i]
        anterior = i
        total += valores[i]

print(total)