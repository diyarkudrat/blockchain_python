
class Blockchain(object):
    def __init__(self):

        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1,proof=100)

    def new_block(self):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            previous_hash: previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self):
        
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

    @property
    def last_block(self):
        pass
