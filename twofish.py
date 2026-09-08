import struct

# --- CONSTANTS & TABLES ---

MDS_MATRIX = [
    [0x01, 0xEF, 0x5B, 0x5B],
    [0x5B, 0xEF, 0xEF, 0x01],
    [0xEF, 0x5B, 0x01, 0xEF],
    [0xEF, 0x01, 0xEF, 0x5B]
]

RS_MATRIX = [
    [0x01, 0xA4, 0x55, 0x87, 0x5A, 0xC8, 0xA0, 0x6E],
    [0x00, 0x01, 0xA4, 0x55, 0x87, 0x5A, 0xC8, 0xA0],
    [0x00, 0x00, 0x01, 0xA4, 0x55, 0x87, 0x5A, 0xC8],
    [0x00, 0x00, 0x00, 0x01, 0xA4, 0x55, 0x87, 0x5A]
]

Q0 = [
    [0xA, 0x0, 0x9, 0xE, 0x6, 0x3, 0xF, 0x5, 0x1, 0xD, 0xC, 0x7, 0xB, 0x4, 0x2, 0x8],
    [0xD, 0x7, 0xF, 0x4, 0x1, 0x2, 0x6, 0xE, 0x9, 0xB, 0x3, 0x0, 0x8, 0x5, 0xC, 0xA]
]

Q1 = [
    [0x2, 0x8, 0xB, 0xD, 0xF, 0x7, 0x6, 0xE, 0x3, 0x1, 0x9, 0x4, 0x0, 0xA, 0xC, 0x5],
    [0x1, 0xE, 0x2, 0xB, 0x4, 0xC, 0x3, 0x7, 0x6, 0xD, 0xA, 0x5, 0xF, 0x9, 0x0, 0x8]
]

# --- GALOIS FIELD ARITHMETIC ---

def gf_mult(a, b, mod):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= mod
        b >>= 1
    return p & 0xFF

def q_perm(i, x):
    a0, b0 = (x >> 4) & 0xF, x & 0xF
    q = Q0 if i == 0 else Q1
    a1 = a0 ^ b0
    b1 = a0 ^ ((b0 >> 1) | ((b0 << 3) & 0xF)) ^ ((a0 << 3) & 0xF)
    a1, b1 = a1 & 0xF, b1 & 0xF
    a2 = q[0][a1] ^ b1
    b2 = q[1][b1] ^ a1
    a3 = q[0][a2] ^ b2
    b3 = q[1][b2] ^ a2
    return ((b3 & 0xF) << 4) | (a3 & 0xF)

def rol32(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def ror32(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

# --- TWOFISH CLASS ---

class Twofish:
    def __init__(self, key: bytes):
        if len(key) not in (16, 24, 32):
            raise ValueError("Key size must be 16, 24, or 32 bytes.")
        
        self.key = key
        self.k_bytes = len(key)
        self.k_words = self.k_bytes // 8
        
        self.S = []
        self.K = []
        self._key_schedule()

    def _h(self, X, L):
        y = [(X >> (8 * i)) & 0xFF for i in range(4)]
        
        if len(L) == 4:
            y[0] = q_perm(1, y[0]) ^ L[3][0]
            y[1] = q_perm(0, y[1]) ^ L[3][1]
            y[2] = q_perm(0, y[2]) ^ L[3][2]
            y[3] = q_perm(1, y[3]) ^ L[3][3]
        if len(L) >= 3:
            y[0] = q_perm(1, y[0]) ^ L[2][0]
            y[1] = q_perm(1, y[1]) ^ L[2][1]
            y[2] = q_perm(0, y[2]) ^ L[2][2]
            y[3] = q_perm(0, y[3]) ^ L[2][3]
        if len(L) >= 2:
            y[0] = q_perm(0, q_perm(0, y[0]) ^ L[1][0]) ^ L[0][0]
            y[1] = q_perm(0, q_perm(1, y[1]) ^ L[1][1]) ^ L[0][1]
            y[2] = q_perm(1, q_perm(0, y[2]) ^ L[1][2]) ^ L[0][2]
            y[3] = q_perm(1, q_perm(1, y[3]) ^ L[1][3]) ^ L[0][3]

        z = [0] * 4
        for i in range(4):
            z[i] = (gf_mult(MDS_MATRIX[i][0], y[0], 0x169) ^
                    gf_mult(MDS_MATRIX[i][1], y[1], 0x169) ^
                    gf_mult(MDS_MATRIX[i][2], y[2], 0x169) ^
                    gf_mult(MDS_MATRIX[i][3], y[3], 0x169))
        return z[0] | (z[1] << 8) | (z[2] << 16) | (z[3] << 24)

    def _key_schedule(self):
        M = [struct.unpack("<I", self.key[i*4:(i+1)*4])[0] for i in range(self.k_bytes // 4)]
        Me = M[0::2]
        Mo = M[1::2]

        for i in range(self.k_words - 1, -1, -1):
            s_vec = [0] * 4
            m_bytes = self.key[i*8:(i+1)*8]
            for row in range(4):
                val = 0
                for col in range(8):
                    val ^= gf_mult(RS_MATRIX[row][col], m_bytes[col], 0x14D)
                s_vec[row] = val
            self.S.append(s_vec)

        L_e = [[(m >> (8 * j)) & 0xFF for j in range(4)] for m in Me]
        L_o = [[(m >> (8 * j)) & 0xFF for j in range(4)] for m in Mo]

        rho = 0x01010101
        for i in range(20):
            A = self._h(2 * i * rho, L_e)
            B = self._h((2 * i + 1) * rho, L_o)
            B = rol32(B, 8)
            K0 = (A + B) & 0xFFFFFFFF
            K1 = rol32((A + 2 * B) & 0xFFFFFFFF, 9)
            self.K.append(K0)
            self.K.append(K1)

    def _g(self, X):
        return self._h(X, self.S)

    def encrypt_block(self, block: bytes) -> bytes:
        R = list(struct.unpack("<4I", block))
        
        for i in range(4):
            R[i] ^= self.K[i]

        for r in range(16):
            T0 = self._g(R[0])
            T1 = self._g(rol32(R[1], 8))
            
            F0 = (T0 + T1 + self.K[2 * r + 8]) & 0xFFFFFFFF
            F1 = (T0 + 2 * T1 + self.K[2 * r + 9]) & 0xFFFFFFFF
            
            R[2] = ror32(R[2] ^ F0, 1)
            R[3] = rol32(R[3], 1) ^ F1
            
            if r < 15:
                R[0], R[1], R[2], R[3] = R[2], R[3], R[0], R[1]

        for i in range(4):
            R[i] ^= self.K[i + 4]

        return struct.pack("<4I", *R)

    def decrypt_block(self, block: bytes) -> bytes:
        R = list(struct.unpack("<4I", block))

        for i in range(4):
            R[i] ^= self.K[i + 4]

        for r in range(15, -1, -1):
            if r < 15:
                R[0], R[1], R[2], R[3] = R[2], R[3], R[0], R[1]

            T0 = self._g(R[0])
            T1 = self._g(rol32(R[1], 8))
            
            F0 = (T0 + T1 + self.K[2 * r + 8]) & 0xFFFFFFFF
            F1 = (T0 + 2 * T1 + self.K[2 * r + 9]) & 0xFFFFFFFF
            
            R[2] = rol32(R[2], 1) ^ F0
            R[3] = ror32(R[3] ^ F1, 1)

        for i in range(4):
            R[i] ^= self.K[i]

        return struct.pack("<4I", *R)

    def encrypt_bytes(self, text_bytes: bytes) -> bytes:
        pad_len = 16 - (len(text_bytes) % 16)
        padded = text_bytes + bytes([pad_len] * pad_len)
        out = bytearray()
        for i in range(0, len(padded), 16):
            out.extend(self.encrypt_block(padded[i:i+16]))
        return bytes(out)

    def decrypt_bytes(self, cipher_bytes: bytes) -> bytes:
        if len(cipher_bytes) % 16 != 0:
            raise ValueError("Ciphertext length must be a multiple of 16 bytes.")
        out = bytearray()
        for i in range(0, len(cipher_bytes), 16):
            out.extend(self.decrypt_block(cipher_bytes[i:i+16]))
        pad_len = out[-1]
        if pad_len < 1 or pad_len > 16:
            raise ValueError("Invalid padding detected or incorrect key.")
        return bytes(out[:-pad_len])

# --- INTERACTIVE USER INPUT INTERFACE ---

def get_valid_key():
    while True:
        key_input = input("\nEnter key (16, 24, or 32 characters): ").strip()
        key_bytes = key_input.encode('utf-8')
        if len(key_bytes) in (16, 24, 32):
            return key_bytes
        print(f"Error: Key must be exactly 16, 24, or 32 bytes long (yours was {len(key_bytes)}).")

def main():
    print("=" * 60)
    print("TWOFISH ENCRYPTION / DECRYPTION TOOL")
    print("=" * 60)

    key_bytes = get_valid_key()
    cipher = Twofish(key_bytes)

    while True:
        print("\n--- MENU ---")
        print("1. Encrypt Plaintext")
        print("2. Decrypt Hex Ciphertext")
        print("3. Change Key")
        print("4. Exit")

        choice = input("\nSelect Option (1-4): ").strip()

        if choice == "1":
            text = input("\nEnter message to encrypt: ")
            encrypted = cipher.encrypt_bytes(text.encode('utf-8'))
            print(f"\nCiphertext (Hex): {encrypted.hex()}")

        elif choice == "2":
            hex_str = input("\nEnter Hex ciphertext to decrypt: ").strip()
            try:
                cipher_bytes = bytes.fromhex(hex_str)
                decrypted = cipher.decrypt_bytes(cipher_bytes).decode('utf-8')
                print(f"\nDecrypted Message: {decrypted}")
            except ValueError as ve:
                print(f"\nDecryption Failed: {ve}")
            except Exception as e:
                print(f"\nError: Could not decode ciphertext. ({e})")

        elif choice == "3":
            key_bytes = get_valid_key()
            cipher = Twofish(key_bytes)
            print("Key updated successfully.")

        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid option. Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()