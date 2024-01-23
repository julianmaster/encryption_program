from ferent import Ferent

def main():
    code = None
    with open('code.py', 'r') as file:
        code = file.read()

    key = b'2YO2wd6yZXxSKOldJVESjc79nugyGSLwmvob9e0XuLw='

    encryption_type = Ferent(key)
    encrypted_code = encryption_type.encrypt(code.encode('utf-8'))

    print(encrypted_code)

if __name__ == "__main__":
    main()