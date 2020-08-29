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
    values = request.get_json()

    required = ['sender','recipient', 'amount']
    if not all(k in values for k in required):
        return 'missing values!!', 400

    index = blockchain.new_block(values['sender'],values['recipient'],values['amount'])
    response = {'message': "Transaction is scheduled to be added to Block No. {}".format(index)}

    return jsonify(response), 201

@app.route('/chain', methods=["GET"])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)