import bitcoin
from bitcoin.rpc import RawProxy, Proxy
import json
from pprint import pprint
import subprocess

###########################################

bitcoin.SelectParams("testnet")

rpc = Proxy()

print("-----------------  SOME BLOCKCHAIN INFORMATION  -----------------------")

print(rpc._call("getblockchaininfo"))


raw_proxy = RawProxy()

print("------------------  SOME WALLET INFO  -------------------")

print(raw_proxy.getwalletinfo())

print("---------------- LIST UNSPENT TX OF THE WALLET  --------------------")

utxos =raw_proxy.listunspent()
pprint(utxos)


# Compute total amount into unspent
amounts = []
for utxo in utxos:
    amounts.append(utxo['amount'])

print('Sum unspent: ', int(sum(amounts)*10**8))


# Compare with ord wallet

command = ["ord", "-t", "wallet", "balance"]
output = subprocess.check_output(command)
balances = output.decode('utf-8').strip()
balances = json.loads(balances)

print('Total balance with `ord`: ', balances['total'])

print('Non-runes balance: ', balances['cardinal'])



print("----------------  ONE ETCH RUNE TRANSACTION ----------------")

raw_tx_hex = raw_proxy.getrawtransaction("bcd74252afdd63d42ea60e524d4bea1794626d30bcf82a42aa6fae23cab2eeb2")

print(raw_tx_hex)

print("Version: ", raw_tx_hex[:8])
print("Rest of the tx: ", raw_tx_hex[8:])
decoded_tx = rpc._call("decoderawtransaction", raw_tx_hex)
pprint(decoded_tx)

print("----------------  ONE MINT RUNE TRANSACTION ----------------")

raw_tx_hex = raw_proxy.getrawtransaction("9e74eec578a56a870fc792a3cc017b0b0e3410016d45c5fbba0dcdbf379de38b")

decode_tx = rpc._call("decoderawtransaction", raw_tx_hex)
pprint(decode_tx)

# 36543a98f9ecd1ecb65fc31a14d70a309d1931dbf8759e5ec97d44ff0e2cd83a

def decodetx(tx_id, type_):
    print(f"------------------  ONE {type_} RUNE TRANSACTION  --------------------")
    raw_tx_hex = raw_proxy.getrawtransaction(tx_id)
    decode_tx = rpc._call("decoderawtransaction", raw_tx_hex)
    pprint(decoded_tx)

decodetx("bcd74252afdd63d42ea60e524d4bea1794626d30bcf82a42aa6fae23cab2eeb2", "TRANSFER")
mempool = rpc.getrawmempool()

print("Début de recherche")

for tx in mempool: 
    if tx == 'd8568eb89116394daddb40f48b6ada8710f1b7289f9083d7a84f993bb208edc0':
        print("Good elle existe!")

print("Fin de la recherche...")

