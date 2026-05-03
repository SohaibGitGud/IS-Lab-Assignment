p = 17
a = 2
b = 2
#  Modular Inverse
def mod_inv(x, p):
    return pow(x, p - 2, p)   # Fermat's little theorem


def point_add(P, Q):
    if P == "O":
        return Q
    if Q == "O":
        return P

    x1, y1 = P
    x2, y2 = Q

    if P != Q:
        m = (y2 - y1) * mod_inv(x2 - x1, p)
    else:
        m = (3 * x1 * x1 + a) * mod_inv(2 * y1, p)

    m = m % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

# Scalar Multiplication
def scalar_mult(k, P):
    result = "O"
    temp = P

    while k > 0:
        if k % 2 == 1:
            result = point_add(result, temp)
        temp = point_add(temp, temp)
        k = k // 2

    return result


G = (5, 1)

# Key Generation
private_key = 7
public_key = scalar_mult(private_key, G)


# Encryption
def encrypt(M, public_key):
    k = 3
    C1 = scalar_mult(k, G)
    C2 = point_add(M, scalar_mult(k, public_key))
    return C1, C2


#  Decryption
def decrypt(C1, C2, private_key):
    S = scalar_mult(private_key, C1)
    minus_S = (S[0], (-S[1]) % p)
    return point_add(C2, minus_S)



M = (6, 3)

C1, C2 = encrypt(M, public_key)
print("Encrypted:", C1, C2)

M2 = decrypt(C1, C2, private_key)
print("Decrypted:", M2)