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

Complexididade:   
Tempo: 
Espaço:
"""
S = "IIIX"
valores = {
"I":1,
"V": 5,
"X": 10,
"L": 50,
"C": 100,
"D": 500,
"M": 1000
    }


total = 0
for letra in S:
    total += valores[letra]


print(total)



#pensando como fazer para reconhecer a logica do x e i e tal, a logica que seria mais facil
#transformar em numero depois um if, se o maior for o que esta DEPOIS do menor, vc faz uma subtraçao de - o valor do indice da frente, trabalha com array basicamente
    
