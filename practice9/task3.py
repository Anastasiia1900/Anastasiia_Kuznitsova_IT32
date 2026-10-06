about = (
    "Your eyes are little lanterns, your gaze is five-star, "
    "flashes in my head - as if it were only a dream."
)

words = about.split()

print("Number of words:", len(words))
print("Longest word:", max(words, key=len))
print("Words in reverse order:", " ".join(words[::-1]))
print("Number of letter a:", about.lower().count("a"))
print("Capitalized:", about.title())
print("Spaces replaced with underscores:", about.replace(" ", "_"))

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print("Is Anastasiia a palindrome:", is_palindrome("Anastasiia"))
print(
    "Is Never odd or even a palindrome:",
    is_palindrome("Never odd or even")
)

day = 19
def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord("a")
            new_char = chr(
                (ord(char.lower()) - start + shift) % 26 + start
            )
            result += new_char
        else:
            result += char

    return result

encrypted = caesar_encrypt("Anastasiia", day)
decrypted = caesar_encrypt(encrypted, -day)

print("Encrypted name:", encrypted)
print("Decrypted name:", decrypted)