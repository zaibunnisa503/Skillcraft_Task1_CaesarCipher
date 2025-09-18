from typing import Optional

def encrypt(text: str, shift: int) -> str:
    """
    Encrypt text using Caesar cipher with a given shift.
    
    Args:
        text (str): The input string to encrypt.
        shift (int): The shift value (positive integer).
    
    Returns:
        str: Encrypted text.
    """
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)


def decrypt(text: str, shift: int) -> str:
    """Decrypt text using Caesar cipher with given shift."""
    return encrypt(text, -shift)

def brute_force(cipher_text: str) -> None:
    """Try all possible shifts and print results."""
    print("\n🔎 Brute-force results:")
    for key in range(26):
        print(f"Key {key:2d}: {decrypt(cipher_text, key)}")


def run_interactive() -> None:
    """Run the tool in interactive mode (console prompts)."""
    print("=== Caesar Cipher Tool ===")
    mode = input("Choose mode (encrypt / decrypt / bruteforce): ").strip().lower()

    if mode in ["encrypt", "decrypt"]:
        text = input("Enter your text: ")
        try:
            shift = int(input("Enter shift value (integer): "))
        except ValueError:
            print("❌ Invalid shift: must be an integer.")
            return

        if mode == "encrypt":
            print("🔐 Encrypted:", encrypt(text, shift))
        else:
            print("🔓 Decrypted:", decrypt(text, shift))

    elif mode == "bruteforce":
        text = input("Enter the cipher text: ")
        brute_force(text)
    else:
        print("❌ Invalid mode selected.")


if __name__ == "__main__":
    run_interactive()
