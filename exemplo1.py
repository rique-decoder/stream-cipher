"""
Demonstração: Reutilização de chave (Two-Time Pad) em Stream Cipher com XOR
"""

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """XOR byte a byte entre duas sequências (usa o tamanho da menor)."""
    return bytes(x ^ y for x, y in zip(a, b))

# --- Cenário: mesma chave K usada para cifrar duas mensagens diferentes ---
M1 = "ola tudo bem".encode("utf-8")
M2 = "isso e um teste".encode("utf-8")

# Chave gerada uma vez (simulando um keystream), do tamanho da maior mensagem
K = bytes([173, 22, 9, 250, 41, 88, 3, 199, 64, 152, 71, 205, 30, 118, 6])

# Cada mensagem é cifrada com a MESMA chave (aqui está o erro fatal)
C1 = xor_bytes(M1, K)
C2 = xor_bytes(M2, K)

print("=== O que o ATACANTE vê (interceptado na rede) ===")
print("C1 (hex):", C1.hex())
print("C2 (hex):", C2.hex())
print()

# --- O ataque: o atacante NÃO sabe K, mas pode calcular C1 XOR C2 ---
attacker_result = xor_bytes(C1, C2)

# --- Prova teórica: isso deveria ser EXATAMENTE igual a M1 XOR M2 ---
real_M1_xor_M2 = xor_bytes(M1, M2)

print("=== O ataque (sem nunca conhecer K) ===")
print("C1 XOR C2      :", attacker_result.hex())
print("M1 XOR M2 (real):", real_M1_xor_M2.hex())
print("São idênticos?  :", attacker_result == real_M1_xor_M2)
print()

# --- "Quebrando" com known-plaintext: se o atacante ADIVINHAR um trecho de M1 ---
# (ex: sabe que mensagens costumam começar com "ola " -- ataque de crib dragging)
crib = "ola tudo".encode("utf-8")
recovered_piece_of_M2 = xor_bytes(attacker_result[:len(crib)], crib)

print("=== Crib dragging: atacante chuta que M1 começa com 'ola ' ===")
print("Trecho de M2 recuperado:", recovered_piece_of_M2)
print("M2 original (bytes)    :", M2[:len(crib)])