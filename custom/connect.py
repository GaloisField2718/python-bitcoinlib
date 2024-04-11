import bitcoin.rpc
import bitcoin

bitcoin.SelectParams('testnet')

proxy = bitcoin.rpc.Proxy()


print(proxy._call("getblockchaininfo"))
