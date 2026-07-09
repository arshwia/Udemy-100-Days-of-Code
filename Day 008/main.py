from art_caesar_cipher import logo
from data_caesar_cipher import valid_characters

print(logo)

encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n\t")
msg = str(input("Type your massage: \n\t").lower())
shift_number = int(input("Type the shift number: \n\t"))


def check_data(msg):
    """بررسی می‌کند که همه کاراکترهای پیام معتبر باشند."""

    for letter in msg:
        is_found = False

        for valid in valid_characters:
            if valid == letter:
                is_found = True
                break

        if not is_found:
            print(f"{letter} is invalid")
            return False

    return True


def encode(msg, shift_number):
    """اینجا بعداً الگوریتم رمزنگاری را کامل می‌کنیم."""

    encoded = ""

    for letter in msg:
        if letter == " ":
            encoded += " "
            continue

        for index, char in enumerate(valid_characters):
            if letter == char:
                new_index = (index + shift_number) % 26
                encoded += valid_characters[new_index]

    return encoded


def decode(msg, shift_number):
    decoded = ""

    for letter in msg:
        if letter == " ":
            decoded += " "
            continue

        for index, char in enumerate(valid_characters):
            if letter == char:
                new_index = (index - shift_number) % 26
                decoded += valid_characters[new_index]
                break

    return decoded


def main(encode_or_decode, msg, shift_number):

    if not check_data(msg):
        return

    if encode_or_decode == "encode":
        msg_encode = encode(msg, shift_number)
        print(f"Here's the encoded result: {msg_encode}")

    elif encode_or_decode == "decode":
        msg_decode = decode(msg, shift_number)
        print(f"Here's the decoded result: {msg_decode}")

    else:
        print("Your input must be 'encode' or 'decode'")


main(encode_or_decode, msg, shift_number)
