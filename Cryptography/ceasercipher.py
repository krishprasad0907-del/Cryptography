def caesar_cipher(text, shift):
	"""Encrypt text using a Caesar cipher while preserving case and symbols."""
	encrypted = []

	for character in text:
		if character.isalpha():
			base = ord("A") if character.isupper() else ord("a")
			encrypted.append(chr((ord(character) - base + shift) % 26 + base))
		else:
			encrypted.append(character)

	return "".join(encrypted)


if __name__ == "__main__":
	operation = input("Encrypt or decrypt? ").strip().lower()
	message = input("Enter a message: ")
	shift = int(input("Enter the shift amount: "))

	if operation == "encrypt":
		print("Encrypted message:", caesar_cipher(message, shift))
	elif operation == "decrypt":
		print("Decrypted message:", caesar_cipher(message, -shift))
	else:
		raise ValueError("Operation must be 'encrypt' or 'decrypt'.")
