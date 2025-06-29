import secrets
import hashlib
from bitcoin import *

def generate_mnemonic():
    # Fake mnemonic (untuk demo)
    mnemonic = ' '.join([secrets.token_hex(2) for _ in range(12)])
    priv = sha256(mnemonic.encode()).hex()
    wif = encode_privkey(priv, 'wif')
    address = privkey_to_address(wif)
    return mnemonic, wif, address

def import_from_mnemonic(mnemonic: str):
    priv = sha256(mnemonic.encode()).hex()
    wif = encode_privkey(priv, 'wif')
    address = privkey_to_address(wif)
    return wif, address
