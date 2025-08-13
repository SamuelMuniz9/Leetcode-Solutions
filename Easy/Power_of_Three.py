"""
LeetCode 326 – Power of Three

Enunciado:
Dado um inteiro n, retorne True se for potência de 3, caso contrário False.
Uma potência de 3 é um número da forma 3^x onde x é um inteiro não-negativo.

Exemplo:
Input: n = 27
Output: True
Explicação: 27 = 3^3

Abordagem: Fiz um loop para gerar potências de 3 começando de 3^0.
A cada iteração, comparamos o resultado com n:
- Se for igual, retornamos True.
- Se a potência gerada ultrapassar n, encerramos o loop e retornamos False.
Essa abordagem evita cálculos desnecessários e não requer estruturas extras.


Complexididade:  
Tempo: O(log₃ n) –> a cada iteração multiplicamos a potência por 3, logo o número de passos cresce proporcionalmente ao logaritmo na base 3 de n.
Espaço: O(1) –> usamos apenas variáveis simples, sem estruturas adicionais.
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 0
        while 3 ** x <= n:
            if n == 3 ** x:
                return True
            x += 1
        return False

# Exemplo de uso fora do LeetCode
if __name__ == "__main__":
    sol = Solution()    
    print(sol.isPowerOfThree(9))  #  Retornando True
    print()
    print(sol.isPowerOfThree(2))  #  Retornando False
