from flask import Flask, jsonify
from flask import abort
import requests

import config

app = Flask(__name__)
import os 
API_KEY = os.environ.get('API_KEY')
API_KEY=str(API_KEY)

@app.route('/GetNfts/<string:projectID>', methods=['GET'])
def get_nfts(projectID):
    api_url = "https://api.nft-maker.io/GetNfts/" + API_KEY + "/"+projectID+"/all"
    print(api_url)
    response = requests.get(api_url)
    return jsonify(response.json())

@app.route('/GetNftDetails/<string:projectID>/<string:name>', methods=['GET'])
def get_nft_details(projectID, name):
    price=config.prices_and_rarity[projectID]["price"]
    toMint=config.prices_and_rarity[projectID]["toMint"]
    api_url = "https://api.nft-maker.io/GetNftDetails/" + API_KEY + "/" + projectID + "/" + name
    response = requests.get(api_url)
    new_json = response.json()
    new_json["price"]=price
    new_json["toMint"]=toMint
    return jsonify(new_json)
@app.route('/GetNftDetailsById/<string:projectID>/<string:nft_id>', methods=['GET'])
def get_nft_details_by_id(projectID, nft_id):
    price=config.prices_and_rarity[projectID]["price"]
    toMint=config.prices_and_rarity[projectID]["toMint"]
    api_url = "https://api.nft-maker.io/GetNftDetailsById/" + API_KEY + "/" + projectID + "/" + nft_id
    response = requests.get(api_url)
    new_json = response.json()
    new_json["price"]=price
    new_json["toMint"]=toMint
    return jsonify(new_json)

@app.route('/GetAddressForSpecificNftSale/<string:projectID>/<string:nft_id>', methods=['GET'])
def get_address_for_specific_nft_sale(projectID, nft_id):
    price=config.prices_and_rarity[str(projectID)]["price"]
    api_url = "https://api.nft-maker.io/GetAddressForSpecificNftSale/" + API_KEY + "/" + projectID + "/" + nft_id + "/1/"+price
    print(api_url)
    response = requests.get(api_url)
    return jsonify(response.json())

@app.route('/CheckAddress/<string:projectID>/<string:paymentAddress>', methods=['GET'])
def CheckAddress(projectID, paymentAddress):
    api_url = "https://api.nft-maker.io/CheckAddress/" + API_KEY + "/" + projectID + "/" + paymentAddress
    print(api_url)
    response = requests.get(api_url)
    return jsonify(response.json())

@app.route('/GetProjectPriceAndRarity/<string:projectID>', methods=['GET']) #get the amount of mintable nfts for each project, and the price of the nfts
def get_project_price_and_rarity(projectID):
    price=config.prices_and_rarity[projectID]["price"]
    toMint=config.prices_and_rarity[projectID]["toMint"]
    
    return jsonify({"price":price, "toMint":toMint})

if __name__ == '__main__':
    app.run(debug=True)