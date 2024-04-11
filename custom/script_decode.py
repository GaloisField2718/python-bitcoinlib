import bitcoin
from bitcoin.rpc import RawProxy
from bitcoin.core import script
import json
from pprint import pprint 

bitcoin.SelectParams("testnet")

rpc = RawProxy()

def decodetx(tx):
    tx_hex = rpc.getrawtransaction(tx)
    return rpc._call("decoderawtransaction", tx_hex)

def is_op_return(tx):
    raw_tx = decodetx(tx)
    return 'OP_RETURN 13' in raw_tx['vout'][0]['scriptPubKey']['asm']

def scriptPub(tx):
    raw_tx = decodetx(tx)
    scriptPubKey = raw_tx['vout'][0]['scriptPubKey']['asm']
    return scriptPubKey

bitcoin.SelectParams("testnet")
rpc = RawProxy()


mempool = rpc.getrawmempool()



runes_tx = []

for tx in mempool:
    if is_op_return(tx):
        runes_tx.append(tx)

print("There are: ",len(runes_tx), " runes txs in mempool")

print("There are: ", len(mempool), " txs in the mempool")


tx_0 = runes_tx[0]

script_0 = scriptPub(tx_0)



#pprint(mempool)


