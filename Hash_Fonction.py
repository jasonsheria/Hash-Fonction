# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import hashlib


    def sha3_hash(input_string):
        # Convertir la chaîne de caractères en bytes (UTF-8)
        input_bytes = input_string.encode('utf-8')

        # Utiliser hashlib pour calculer la valeur de hachage SHA-3 (SHA3-256)

        sha3_hash = hashlib.sha3_256(input_bytes).hexdigest()

        return sha3_hash


    # Exemple d'utilisation
    input_data = input(print("entrer la phrase a scripter svp : "))
    hashed_result = sha3_hash(input_data)

    print(f"Input Data: {input_data}")
    print(f"SHA-3 Hash: {hashed_result}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
