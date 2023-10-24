from cryptography.fernet import Fernet

key = "R0XC6ZEPMwU5PyowEFR9AcMitrxHGy_Of8p4cZ74JxM="

system_info_e = "e_system.txt"
clipboard_info_e = "e_clipboard.txt"
keys_info_e = "e_keys_logged.txt"

encrypted_files = [system_info_e, clipboard_info_e, keys_info_e]
count = 0

for decrypting_file in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_files[count], 'wb') as f:
        f.write(decrypted)

    count += 1

