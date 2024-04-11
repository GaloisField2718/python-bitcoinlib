import bitcoin 
from bitcoin.rpc import Proxy
import json
from pprint import pprint
import subprocess

bitcoin.SelectParams('testnet')

amount = 0.0031
nb_outputs = 3
command = ["ord", "-t", "wallet", "receive"]

output = subprocess.check_output(command)
receiver = json.loads(output.decode('utf-8').strip())
receiver = receiver["addresses"][0]

print('receiver1: ', receiver)

output = subprocess.check_output(command)
receiver2 = json.loads(output.decode('utf-8').strip())
receiver2 = receiver2["addresses"][0]


print('receiver2: ', receiver2)
output = subprocess.check_output(command)
receiver3 = json.loads(output.decode('utf-8').strip())
receiver3 = receiver3["addresses"][0]


print('receiver3: ', receiver3)

receivers = [receiver, receiver2, receiver3]

payments = {}

for index in range(nb_outputs):
    payments[f'{receivers[index]}'] = 0.001

print(payments)

rpc = Proxy()

rpc.sendmany("",payments)

