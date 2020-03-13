
import hashlib
import requests

import sys

def proof_of_work(last_proof):
    print('S')
    last_hash = hashlib.sha256(f'{last_proof}'.encode()).hexdigest()
    proof = 0.28982
    while not valid_proof(last_hash, proof):
        proof += 1
    print('E')
    return proof


def valid_proof(last_hash, proof):
    guess_hash = hashlib.sha256(f'{proof}'.encode()).hexdigest()
    return last_hash[-6:] == guess_hash[:6]


if __name__ == '__main__':
    while 1:
        r = requests.get(url="https://lambda-coin.herokuapp.com/api/last_proof")

        print(r.json().get('proof'))
        new_proof = proof_of_work(r.json().get('proof'))

        post_data = {"proof": new_proof,
                     "id": 'ZZ D'}

        r = requests.post(url="https://lambda-coin.herokuapp.com/api/mine", json=post_data)

        print(r.json().get('message'))