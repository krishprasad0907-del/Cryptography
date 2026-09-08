# --- DES S-BOXES & PERMUTATION TABLES ---

IP = [
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
]

S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ]
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


# --- HELPER FUNCTIONS ---

def permute(bits, table):
    """Permutes bits according to a mapping table."""
    return [bits[i - 1] for i in table]

def bytes_to_bits(data):
    """Converts bytes to list of integer bits (0/1)."""
    bits = []
    for b in data:
        bits.extend([(b >> i) & 1 for i in range(7, -1, -1)])
    return bits

def bits_to_bytes(bits):
    """Converts list of integer bits (0/1) to bytes."""
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i+8]:
            byte = (byte << 1) | b
        bytes_list.append(byte)
    return bytes(bytes_list)

def left_shift(bits, n):
    """Circular left shift on bit array."""
    return bits[n:] + bits[:n]

def xor(bits1, bits2):
    """Bitwise XOR between two bit arrays."""
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]


# --- CORE DES ALGORITHM ---

def generate_subkeys(key_bytes):
    """Generates 16 subkeys (48 bits each) from a 64-bit key."""
    bits = bytes_to_bits(key_bytes)
    permuted_key = permute(bits, PC1)
    
    C = permuted_key[:28]
    D = permuted_key[28:]
    
    subkeys = []
    for shift in SHIFTS:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        subkeys.append(permute(C + D, PC2))
        
    return subkeys

def feistel_f(R, subkey):
    """DES Feistel function."""
    expanded_R = permute(R, E)
    xored = xor(expanded_R, subkey)
    
    output_bits = []
    for i in range(8):
        block = xored[i*6:(i+1)*6]
        row = (block[0] << 1) | block[5]
        col = (block[1] << 3) | (block[2] << 2) | (block[3] << 1) | block[4]
        val = S_BOXES[i][row][col]
        
        for j in range(3, -1, -1):
            output_bits.append((val >> j) & 1)
            
    return permute(output_bits, P)

def des_block(block_bits, subkeys, decrypt=False):
    """Processes a single 64-bit block through DES."""
    bits = permute(block_bits, IP)
    L = bits[:32]
    R = bits[32:]
    
    keys = reversed(subkeys) if decrypt else subkeys
    
    for subkey in keys:
        L_next = R
        R_next = xor(L, feistel_f(R, subkey))
        L, R = L_next, R_next
        
    final_bits = R + L  # Swap L and R in final round
    return permute(final_bits, FP)


# --- TRIPLE DES (3DES) EDE ENGINE ---

def des_encrypt_block(block_bytes, key_bytes):
    subkeys = generate_subkeys(key_bytes)
    bits = bytes_to_bits(block_bytes)
    return bits_to_bytes(des_block(bits, subkeys, decrypt=False))

def des_decrypt_block(block_bytes, key_bytes):
    subkeys = generate_subkeys(key_bytes)
    bits = bytes_to_bits(block_bytes)
    return bits_to_bytes(des_block(bits, subkeys, decrypt=True))

def triple_des_encrypt_block(block, k1, k2, k3):
    """3DES EDE Mode: Encrypt(k1) -> Decrypt(k2) -> Encrypt(k3)"""
    step1 = des_encrypt_block(block, k1)
    step2 = des_decrypt_block(step1, k2)
    step3 = des_encrypt_block(step2, k3)
    return step3

def triple_des_decrypt_block(block, k1, k2, k3):
    """3DES EDE Mode: Decrypt(k3) -> Encrypt(k2) -> Decrypt(k1)"""
    step1 = des_decrypt_block(block, k3)
    step2 = des_encrypt_block(step1, k2)
    step3 = des_decrypt_block(step2, k1)
    return step3


# --- PADDING & STREAM ENCRYPTION/DECRYPTION ---

def pkcs7_pad(data, block_size=8):
    """Pads arbitrary bytes to match the 8-byte (64-bit) DES block size."""
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len] * pad_len)

def pkcs7_unpad(data):
    """Removes PKCS#7 padding."""
    pad_len = data[-1]
    return data[:-pad_len]

def encrypt_3des(plaintext_str, key_24bytes):
    """Encrypts arbitrary text string using 3DES EDE mode."""
    if len(key_24bytes) != 24:
        raise ValueError("3DES key must be exactly 24 bytes (192 bits) long.")
    
    k1 = key_24bytes[0:8]
    k2 = key_24bytes[8:16]
    k3 = key_24bytes[16:24]
    
    raw_bytes = pkcs7_pad(plaintext_str.encode('utf-8'))
    encrypted_bytes = bytearray()
    
    for i in range(0, len(raw_bytes), 8):
        block = raw_bytes[i:i+8]
        encrypted_bytes.extend(triple_des_encrypt_block(block, k1, k2, k3))
        
    return bytes(encrypted_bytes)

def decrypt_3des(ciphertext_bytes, key_24bytes):
    """Decrypts ciphertext bytes back into plain text string."""
    if len(key_24bytes) != 24:
        raise ValueError("3DES key must be exactly 24 bytes (192 bits) long.")
        
    k1 = key_24bytes[0:8]
    k2 = key_24bytes[8:16]
    k3 = key_24bytes[16:24]
    
    decrypted_bytes = bytearray()
    for i in range(0, len(ciphertext_bytes), 8):
        block = ciphertext_bytes[i:i+8]
        decrypted_bytes.extend(triple_des_decrypt_block(block, k1, k2, k3))
        
    return pkcs7_unpad(decrypted_bytes).decode('utf-8')


# --- INTERACTIVE CLI ---

def main():
    print("=" * 60)
    print("TRIPLE DES (3DES) ENCRYPTION TOOL")
    print("=" * 60)
    
    # 3DES requires a 24-byte (192-bit) key split into K1, K2, K3
    default_key = b"12345678abcdefgh87654321"  
    
    key_input = input("Enter a 24-character key [Press Enter to use default]: ")
    if len(key_input) == 24:
        key = key_input.encode('utf-8')
    else:
        print(f"Using default 24-byte key: {default_key.decode('utf-8')}")
        key = default_key

    while True:
        print("\n--- MENU ---")
        print("1. Encrypt Text")
        print("2. Decrypt Hex Ciphertext")
        print("3. Exit")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == "1":
            text = input("\nEnter message to encrypt: ")
            encrypted_bytes = encrypt_3des(text, key)
            print(f"\nEncrypted (HEX Format):\n{encrypted_bytes.hex()}")
            
        elif choice == "2":
            hex_str = input("\nEnter Hex ciphertext to decrypt: ").strip()
            try:
                cipher_bytes = bytes.fromhex(hex_str)
                decrypted = decrypt_3des(cipher_bytes, key)
                print(f"\nDecrypted Message:\n{decrypted}")
            except Exception as e:
                print(f"\nDecryption failed: {e}")
                
        elif choice == "3":
            print("\nExiting program.")
            break
        else:
            print("Invalid choice, select 1, 2, or 3.")

if __name__ == "__main__":
    main()