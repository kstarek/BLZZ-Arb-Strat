import socket
import os
import itertools
import time
import json
import web3

w3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))

block_number = w3.eth.block_number


ipc_path = '~/.ethereum/geth.ipc'
ipc_path = os.path.expanduser(ipc_path)

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect(ipc_path)
sock.settimeout(0.1)


def receive_response(sock, total):
    raw_response = b''
    end_chr = ord('\n')
    while total > 0:
        chunk = sock.recv(1 * 4096)
        raw_response += chunk
        total -= chunk.count(b'\n')
    return raw_response


start_time = time.time()

request_counter = itertools.count()
responses = b''
for chunk in range(total_blocks // blocks_per_chunk):
    for i in range(blocks_per_chunk):
        count = next(request_counter)
        request = f'{{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["{hex(block_number)}",false],"id":{count}}}'
        request = request.encode('ascii')
        sock.sendall(request)
        block_number += 1
    responses += receive_response(sock, blocks_per_chunk)

data = [json.loads(e) for e in responses.split(b'\n')[:-1]]

end_time = time.time()
print(end_time - start_time)

