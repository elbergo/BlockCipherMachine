def main():
    print('Welcome to the AFA English crypto machine')
    print('=================================')
    passphrase = input('Please enter a passphrase: ')
    clear_text = input('Please enter something to encrypt: ', )
    passphrase1 = bytearray(passphrase.encode('utf-8'))
    print(clear_text)

    b = []
    if len(clear_text) % 4 != 0:
        run = True
        while run:
            clear_text += ' '
            if len(clear_text) % 4 == 0:
                run = False
    clear_bytes = clear_text.encode('utf-8')
    clear_bytes = bytearray(clear_bytes)

    for i in range(0, len(clear_bytes), 4):
        b.append(clear_bytes[i: i + 4])



    for b_array in b:
        pos1 = passphrase1[0] % len(b_array)
        pos2 = passphrase1[1] % len(b_array)
        pos3 = passphrase1[2] % len(b_array)
        pos4 = passphrase1[3] % len(b_array)
        b_array[pos1], b_array[pos3] = b_array[pos3], b_array[pos1]
        b_array[pos2], b_array[pos4] = b_array[pos4], b_array[pos2]

    print(b)

    cipher = []
    count = 0
    for b_array in b:
        for c in b_array:
            cipher.append(c ^ ord(passphrase[count % len(passphrase)]))
            count += 1
    print(cipher)

    text = []
    count = 0
    for c in cipher:
        text.append(c ^ ord(passphrase[count % len(passphrase)]))
        count += 1

    string = ''
    for i in text:
        string += chr(i)
    print(f'string: {string}')

    x = []
    string = bytearray(string.encode('utf-8'))
    for i in range(0, len(string), 4):
        x.append(string[i: i + 4])

    print(x)

    for b_array in x:
        pos1 = passphrase1[0] % len(b_array)
        pos2 = passphrase1[1] % len(b_array)
        pos3 = passphrase1[2] % len(b_array)
        pos4 = passphrase1[3] % len(b_array)
        b_array[pos1], b_array[pos3] = b_array[pos3], b_array[pos1]
        b_array[pos2], b_array[pos4] = b_array[pos4], b_array[pos2]

    text = ''
    for i in x:
        text += i.decode('utf-8')
    print(text)


if __name__ == '__main__':
    main()
