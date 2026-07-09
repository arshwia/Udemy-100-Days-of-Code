from art_caesar_cipher import logo
from data_caesar_cipher import valid_characters

# print(logo)
# encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n\t")
encode_or_decode = "encode"

msg = str(input("Type your massage: \n\t").lower())
shift_number = int(input("Type the shift number: \n\t"))


def split_msg(msg):
    msg_list = msg.split(" ")

    return msg_list


def encode():
    print("encoding")
    msg_list = split_msg(msg)

    msg_encode = msg_list
    return msg_encode


def main(encode_or_decode, msg, shift_num):
    if encode_or_decode == "encode":
        print("encode")

        msg_encode = encode()

        print(f"Here's the encoded result: {msg_encode}")

    elif encode_or_decode == "decode":
        print("decode")

    else:
        print("your input not 'encode' or 'decode'")


def check_data():
    for letter in msg:
        is_found = False

        for valid in valid_characters:
            if valid == letter:
                print(f"valid {valid, letter}")
                is_found = True
                break

        if not is_found:
            print(f"{letter} is invalid")

    main(encode_or_decode, msg, shift_number)


check_data()
