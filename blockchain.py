import hashlib
import json
import time



class Blockchain(object):
    def __init__(self):

        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1,proof=100)


    def new_block(self, proof, previous_hash=None):
        """ Creates new block and adds it to the exising chain """

        # create python object that contains the info inside a block
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            previous_hash: previous_hash or self.hash(self.chain[-1])
        }

        # set current transaction list to empty
        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self,sender, receiver, amount):
        """ create new transaction that will be sent to the next block """
        
        self.current_transactions.append(
            {
                'sender': sender,
                'receiver': receiver,
                'amount': amount,
            }
        )

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """ creates a SHA-256 block hash. Ensures that the dict is in order """

        # convert block into a json object and then into bytes so it can be hashed
        block_string = json.dumps(block, sort_keys=True).encode()

        # return encoded data in hexadecimat format
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_proof(last_proof, proof):

        guess = "{} {}".format(last_proof, proof).encode()
        guess_hash = hashlib.sha256(guess).hexidigest()

        return guess_hash[:4] == "0000"
