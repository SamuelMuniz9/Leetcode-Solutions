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
    - Primeiro, verificar os "combos" (subtrações especiais: IV=4, IX=9, etc.).
    - Remover esses combos da string e adicionar seus valores diretamente ao total.
    - Depois, somar os valores restantes dos símbolos romanos.

    Complexidade:
    - Tempo: O(n), onde n é o tamanho da string `S`, pois percorremos cada caractere uma vez.
    - Espaço: O(1), já que usamos apenas dicionários fixos de valores.

    """
S = "XIV"
valores = {
    "I":1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
        }
combo_numero = {
            "IV" : 4, 
            "IX" : 9,
            "XL" : 40, 
            "XC" : 90, 
            "CD" : 400, 
            "CM" : 900
              }



total = 0
for indice, valor in combo_numero.items():
    if indice in S: #verifica se possui algum combo)numero no texto
        total += valor
        S = S.replace(indice, "")
    
    

for letra in S:
        total += valores[letra]


print(total)


