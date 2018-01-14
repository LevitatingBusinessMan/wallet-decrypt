# Dogecoin + Bitcoin (or any related backup in protobuf format) Wallet Decrypt (BackupFile -> Hex keys)

This is a small modification to wallet-decrypt that instead of providing a mnemonic key, dumps all public and private keys from the wallet in base16 hex format.

**WARNING: You will be decrypting your wallet so the private key might be compromised.**

## Instructions

### In your mobile:

- Go to `Safety` and remove the spending PIN.
- Backup your wallet. Remember the password you use.
- Connect your phone with a usb cable and copy the backup file to your computer.

### In your computer

Install dependencies
```
pip install pycrypto protobuf
```
Download an offline copy of the tool at walletgenerator.net to manipulate the key pairs.

## You may now wish to take your computer offline to ensure the security of your keys in case any of these tools have been compromised

Run the script (replace with the appropriate FILENAME(backup file) and PASSWORD(your backup password))
```
wallet-decrypt.py FILENAME PASSWORD
```

You will get a list of public and private keypairs. Likely the first will be the main key for this wallet to which your coins were originally sent. The others may be change addresses for transactions, don't ask me, I don't know. You should check them all to see if they contain any lost coins.

Start up your copy of walletgenerator, click skip and then go to the "Wallet Details" tab. 
**Don't forget to change your currency to Dogecoin in the "Choose Currency" box!**

Copy and paste your private key into the provided text box and click "View Details".

A bunch of keys will be generated from your private key. If everything is working properly, the public key generated on this page will match the public key that you extracted from the wallet. It should be the "Public Key (compressed)".

If your public key matches the compressed public key, then the compressed address should be the one that contains your coins. Copy the "Public Address Compressed" into a blockchain explorer like dogechain.info and confirm that this address contains the coins.

An important thing to note is that the compressed and uncompressed addresses are in fact two separate addresses, with separate keys. 

On the right, the "Private Key WIF Compressed" is the key to access the funds in the "Public Address Compressed". This private key starts with a Q.
On the left, the "Private Key WIF" is the key to access the funds in the "Public Address". This private key starts with a 6.
Whichever public address contains the coins, use the corresponding private key in the dogechain.io "Redeem Paper Wallet" tool (or your own client) to sweep them into a new wallet. 

Congratulations and remember, always keep your Dogecoin safe by knowing your private key and keeping it safe. If you don't have the private key, you don't have the coins.

**This software is provided under the Apache License Version 2.0 - Use at your own risk**
