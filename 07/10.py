shift = int(input())
message = input().upper()

encrypted_message = ""
for char in message:
    if 'А' <= char <= 'Я':
        encrypted_char = chr(((ord(char) - ord('А') + shift) % 33) + ord('А'))
    else:
        encrypted_char = char

    encrypted_message += encrypted_char

print(encrypted_message)
