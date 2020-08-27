from flask import Flask
from blockchain import Blockchain
from uuid import uuid4
from flask import jsonify

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-','')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "mining new block"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():

    return "adding a new transaction"

@app.route('/chain', methods=["GET"])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)