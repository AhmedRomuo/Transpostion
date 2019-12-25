ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']


# get key chars position
def key_assign(key):
    init = 0
    ls_key_sort = [None] * len(key)

    for i in range(len(ls)):
        k = 0
        while k < len(key):
            if ls[i] == key[k]:
                init += 1
                ls_key_sort[k] = init
            k += 1
        i += 1
    return ls_key_sort


# get number location order
def get_num_loc(key, key_list):
    key_sort = ""
    i = 1
    while i < len(key)+1:
        for x in range(len(key)):
            if key_list[x] == i:
                key_sort += str(x)
        i += 1
    return key_sort


# encryption
def encryption(message, key):
    key_to_print = ""
    key_chars_position = key_assign(key)

# print the key and his order
    for i in range(len(key)):
        key_to_print += key[i] + " "

    key_to_print += "\n"

    for item in key_chars_position:
        key_to_print += str(item) + " "

    print(key_to_print)
    print("------------------------------")

# to know the message is fit the matrix
    external_chars = len(message) % len(key)
    alpha_to_external_chars = len(key) - external_chars

# put the external chars to the message
    if external_chars != 0:
        for i in range(alpha_to_external_chars):
            message += ls[i]

    # print(message)
    num_row = len(message) / len(key)
    matrix_message = [[0] * len(key) for i in range(int(num_row))]
    z = 0

    for _row in range(len(matrix_message)):
        for _column in range(len(matrix_message[_row])):
            matrix_message[_row][_column] = message[z]
            z += 1

    # print message
    modify_msg = ""
    for r in range(len(matrix_message)):
        for c in range(len(matrix_message[r])):
            modify_msg += matrix_message[r][c] + " "
        modify_msg += "\n"

    print(modify_msg)

    key_order = get_num_loc(key, key_chars_position)
    cipher_text = ""

    for x_column in range(len(key)):
        x_row = 0
        while x_row < int(num_row):
            cipher_text += matrix_message[x_row][int(key_order[x_column])]
            x_row += 1

    print("Cipher Text : " + cipher_text)


# decryption
def decryption(message, key):
    num_of_row = len(message) / len(key)
    matrix_message = [[0] * len(key) for i in range(int(num_of_row))]
    key_chars_position = key_assign(key)
    key_order = get_num_loc(key, key_chars_position)

    z = 0
    x_row = 0
    for x_column in range(len(matrix_message[x_row])):
        while x_row != len(matrix_message):
            matrix_message[x_row][int(key_order[x_column])] = message[z]
            x_row += 1
            z += 1
        x_row = 0

    plain_text = ""
    for row in range(len(matrix_message)):
        for column in range(len(matrix_message[row])):
            plain_text += matrix_message[row][column]

    print("Plain Text : " + plain_text)


def main():
    type_message = int(input("1- Encryption\n2- Decryption\nEnter your choice : "))
    message = input("the message : ")
    key = input("key : ")
    print("------------------------------")
    msg = message.replace(" ", "")

    if type_message == 1:
        encryption(msg.lower(), key.lower())
    elif type_message == 2:
        decryption(msg.lower(), key.lower())


if __name__ == '__main__': main()
