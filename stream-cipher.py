"""
Exercício de Stream Cipher (Cifra de Fluxo)

Enunciado Teórico/Prático: Considere uma cifra de fluxo baseada em XOR onde a chave inicial (seed) gera um vetor de keystream utilizando um registrador de deslocamento de feedback linear (LFSR) simples ou uma função pseudo-aleatória básica.

Pergunta: Dada a mensagem em binário M = 10110011 e o keystream gerado K = 11001010, aplique a operação de criptografia e descriptografia. Explique por que a reutilização de uma mesma chave (chave repetida) em uma cifra de fluxo compromete totalmente a segurança da comunicação.

"""
import operator



# C = M XOR K
# M = C XOR K

M = 0b10110011
K = 0b11001010

print(f'\nEsta é a mensagem = {M}\n')

print(f'Esta é a chave = {K}\n')


C = operator.xor(K, M) 
print(f'Esta é a mensagem cifrada = {C}\n')
# 0b0101001 (exemplo)

M = operator.xor(C, K) 
print(f'Esta é a mensagem após o XOR (decifrada) = {M}\n')

# ============================================================================

  
M1 = 0b10110011
M2 = 0b01110101
K  = 0b11001010

print(f'M1 = {bin(M1)}')
print(f'M2 = {bin(M2)}')
print(f'K  = {bin(K)}  (mesma chave usada nas duas mensagens)\n')

# --- Cada mensagem é cifrada com a mesma chave ---
C1 = operator.xor(M1, K)
C2 = operator.xor(M2, K)

print(f'C1 = M1 XOR K = {bin(C1)}')
print(f'C2 = M2 XOR K = {bin(C2)}\n')

# --- O que o ATACANTE faz: ele NUNCA viu M1, M2 ou K, só interceptou C1 e C2 ---
ataque = operator.xor(C1, C2)

# --- Prova: isso é EXATAMENTE igual a M1 XOR M2, sem nunca usar K ---
prova = operator.xor(M1, M2)

print(f'Atacante calcula C1 XOR C2 = {bin(ataque)}')
print(f'Isso é igual a M1 XOR M2?  = {bin(prova)}')
print(f'São idênticos? {ataque == prova}\n')    

print('--> O atacante conseguiu M1 XOR M2 sem nunca ter descoberto K.')
print('--> A chave sumiu da equação (K XOR K = 0), expondo a relação entre as duas mensagens.') 