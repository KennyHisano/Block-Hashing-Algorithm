import hashlib
header_hex = ("01000000" + "ae178934851bfa0e83ccb6a3fc4bfddff3641e104b6c4680c31509074e699be2" + "bd672d8d2199ef37a59678f92443083e3b85edef8b45c71759371f823bab59a9" + "7126614f" + "44d5001d" + "45920180")

header_bin = header_hex.decode('hex')

hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
hash.encode('hex_codec')


print(hash[::-1].encode('hex_codec'))
