"""
Demonstração: ataque estatístico usando o caractere ESPAÇO
(sem depender de "chutar" uma palavra específica)
"""

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

# Duas mensagens cifradas com a MESMA chave (o erro fatal)
M1 = "the secret meeting is tonight".encode("ascii")
M2 = "attack will start at midnight".encode("ascii")

K = bytes([ (i * 37 + 91) % 256 for i in range(len(M1)) ])  # keystream qualquer

C1 = xor_bytes(M1, K)
C2 = xor_bytes(M2, K)

# --- O atacante só tem C1 e C2, calcula isto: ---
combined = xor_bytes(C1, C2)   # == M1 XOR M2, sem nunca ter visto K

SPACE = ord(' ')  # 0x20

print("Testando, posição por posição, 'e se um dos dois tinha um ESPAÇO aqui?'\n")
recovered = [' '] * len(combined)

for i, byte in enumerate(combined):
    candidate = byte ^ SPACE     # supõe que M1[i] era espaço
    ch = chr(candidate)
    if ch.isalpha():
        # Se vira uma letra válida, é forte sinal de que a OUTRA mensagem
        # tinha essa letra nessa posição (e a mensagem 1 tinha um espaço)
        recovered[i] = ch
        origem = "M2" if chr(M1[i]) == ' ' else "M1"
        print(f"pos {i:2d}: combined={byte:3d}  chute_espaço -> '{ch}'  (letra real vinda de {origem})")
    else:
        print(f"pos {i:2d}: combined={byte:3d}  chute_espaço -> não é letra, ignora")

print("\nTexto parcialmente recuperado (sem nunca ter chutado uma palavra):")
print("".join(recovered))