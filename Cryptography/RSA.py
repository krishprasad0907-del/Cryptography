import random

def is_prime(n, k=5):
    """Miller-Rabin primality test."""
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << (bits - 1)) | 1
        if is_prime(num):
            return num

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Modular inverse does not exist")
    return x % phi

def generate_keypair(keysize=2048):
    p = generate_prime(keysize // 2)
    q = generate_prime(keysize // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt_text(e, n, text):
    data_bytes = text.encode('utf-8')
    m = int.from_bytes(data_bytes, byteorder='big')
    if m >= n:
        raise ValueError("Message is too large for this key size!")
    return pow(m, e, n)

def decrypt_ciphertext(d, n, ciphertext_int):
    m = pow(ciphertext_int, d, n)
    byte_len = (m.bit_length() + 7) // 8
    decrypted_bytes = m.to_bytes(byte_len, byteorder='big')
    return decrypted_bytes.decode('utf-8')

def main():
    # Active keys stored in memory for the current session
    current_pub = None   # (e, n)
    current_priv = None  # (d, n)

    while True:
        print("\n" + "=" * 50)
        print("RSA ENCRYPTION / DECRYPTION TOOL")
        print("=" * 50)
        print("1. Generate NEW Keypair")
        print("2. Input EXISTING Keys (Enter e/d and n)")
        print("3. Encrypt Text")
        print("4. Decrypt Ciphertext Integer")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            print("\nGenerating new 2048-bit RSA keypair...")
            current_pub, current_priv = generate_keypair(keysize=2048)
            e, n = current_pub
            d, _ = current_priv
            print("\n--- NEW KEYS GENERATED ---")
            print(f"Public Exponent (e): {e}")
            print(f"Private Exponent (d):\n{d}")
            print(f"Modulus (n):\n{n}")

        elif choice == "2":
            print("\n--- LOAD EXISTING KEYS ---")
            try:
                mod_str = input("Enter Modulus (n): ").strip()
                if not mod_str:
                    continue
                n = int(mod_str)

                e_str = input("Enter Public Exponent (e) [Press Enter to skip]: ").strip()
                d_str = input("Enter Private Exponent (d) [Press Enter to skip]: ").strip()

                if e_str:
                    current_pub = (int(e_str), n)
                if d_str:
                    current_priv = (int(d_str), n)

                print("\nKeys loaded into session successfully!")
            except ValueError:
                print("\nError: Key components must be valid integers.")

        elif choice == "3":
            if not current_pub:
                print("\nNo Public Key loaded! Choose Option 1 (Generate) or Option 2 (Input Existing).")
                continue
            
            text = input("\nEnter plaintext message to encrypt: ")
            try:
                e, n = current_pub
                cipher_int = encrypt_text(e, n, text)
                print(f"\nEncrypted Ciphertext (Integer):\n{cipher_int}")
            except Exception as err:
                print(f"\nEncryption error: {err}")

        elif choice == "4":
            if not current_priv:
                print("\nNo Private Key loaded! Choose Option 1 (Generate) or Option 2 (Input Existing).")
                continue

            cipher_str = input("\nEnter ciphertext integer to decrypt: ").strip()
            try:
                cipher_int = int(cipher_str)
                d, n = current_priv
                decrypted_str = decrypt_ciphertext(d, n, cipher_int)
                print(f"\nDecrypted Message:\n{decrypted_str}")
            except ValueError:
                print("\nError: Ciphertext must be a valid numerical integer.")
            except Exception as err:
                print(f"\nDecryption failed: {err}")

        elif choice == "5":
            print("\nExiting program.")
            break
        else:
            print("\nInvalid selection, please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()