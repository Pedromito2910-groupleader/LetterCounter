'''
   Progamador....: (C) 2025 Pedro Sousa
   Data..........: 14/02/2025
   Observações...: Contador de vogais e consoantes.
'''

texto = input("Introduza um texto ")

contadorVogais = 0 
contadorConsoantes = 0

#Algoritmo
for letra in texto:
    if letra.upper() in "AEIOU":
        contadorVogais = contadorVogais + 1
    elif letra == ' ':
        pass
    else:
        contadorConsoantes = contadorVogais + 1
         
 

print(f"Vogais -> {contadorVogais}")
print(f"Consoantes -> {contadorConsoantes}")