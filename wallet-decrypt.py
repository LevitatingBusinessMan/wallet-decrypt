#!/usr/bin/env python
from __future__ import print_function

import argparse
import base64
from hashlib import md5
from Crypto.Cipher import AES
import wallet_pb2
from binascii import hexlify, unhexlify

def derive_key_and_iv(password, salt, key_len, iv_len):
    data = tmp2 = b''
    tmp = password.encode() + salt
    while len(data) < key_len + iv_len:
        msg = tmp2 + tmp
        tmp2 = md5(msg).digest()
        data += tmp2
    key = data[:key_len]
    iv = data[key_len:key_len + iv_len]
    return key, iv


def get_wallet(filename, password):
    with open(filename, 'rb') as f:
        data = base64.b64decode(f.read())
        assert (data[:8] == b'Salted__')
        salt = data[8:16]
        key, iv = derive_key_and_iv(password, salt, 32, AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        len(data[AES.block_size:])
        padded_plain = cipher.decrypt(data[AES.block_size:])
        pad_len = padded_plain[-1]

        if isinstance(pad_len, str):
            pad_len = ord(pad_len)

        pbdata = padded_plain[:-pad_len]
        w = wallet_pb2.Wallet()
        w.ParseFromString(pbdata)
        return w


def main():
    parser = argparse.ArgumentParser(description='Decrypt Bitcon Wallet (Schildbach''s Bitcoin)')
    parser.add_argument('filename')
    parser.add_argument('password')

    args = parser.parse_args()

    print("Extracting key pairs...\n")

    w = get_wallet(args.filename, args.password)
    for k in w.key:
        if len(k.secret_bytes) > 0 and k.type != 3: # Type 3 are mnemonic keys and they make a mess
            pubkey = int('0x0' + hexlify(k.public_key).decode('utf8'), 16)
            print("Pub:",'{:x}'.format(pubkey))

            secret = int('0x0' + hexlify(k.secret_bytes).decode('utf8'), 16)
            print("Sec:",'{:x}'.format(secret))
            print()


if __name__ == '__main__':
    main()
