from flask import Flask, json, jsonify
from flask import abort, request
import requests
from flask_cors import CORS
import config

import base64

app = Flask(__name__)
#CORS(app, origins= ["http://localhost:3000", "http://localhost:5500","https://cardaworlds.io","https://viewer.cardaworlds.io","https://www.cardaworlds.io","https://cardaworlds.github.io"])
CORS(app, origins= ["https://cardaworlds.io","https://viewer.cardaworlds.io","https://www.cardaworlds.io","https://cardaworlds.github.io"])

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

@app.route('/GetAddressForRandomNftSale/<string:projectID>', methods=['GET'])
def get_address_for_random_nft_sale(projectID):
    #price=config.prices_and_rarity[str(projectID)]["price"]
    price=str(35000000)
    api_url = "https://api.nft-maker.io/GetAddressForRandomNftSale/" + API_KEY + "/" + projectID + "/1/"+price
    print(api_url)
    response = requests.get(api_url)
    return jsonify(response.json())

@app.route('/CheckAddress/<string:projectID>/<string:paymentAddress>', methods=['GET'])
def CheckAddress(projectID, paymentAddress):
    api_url = "https://api.nft-maker.io/CheckAddress/" + API_KEY + "/" + projectID + "/" + paymentAddress
    print(api_url)
    response = requests.get(api_url)
    return jsonify(response.json())

@app.route('/GetCounts/<string:projectID>/', methods=['GET'])
def GetCounts(projectID):
    api_url = "https://api.nft-maker.io/GetCounts/" + API_KEY + "/" + projectID
    print(api_url)
    response = requests.get(api_url)
    return jsonify(response.json())
""" 
@app.route('/UploadNft', methods=['POST'])
def UploadNft():
    
    comma=", "
    print(request)
    if request.is_json:
        data = request.get_json()
        print(data)
        projectID = data['projectID']
        api_url = "https://api.nft-maker.io/UploadNft/" + "71a28c2e9b1d4f9b9f96b0f914aa0ecf" + "/" + projectID
        print(api_url)
        assetName = data["assetName"]
        planetName = data["planetName"]
        imageURL = data["imageURL"]
        heightmap=data["heightmap"]
        background=data["background"]
        rarities=comma.join(data["rarities"])
        
        with open(imageURL, 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            imageURL_base64 = base64_encoded_data.decode('utf-8')
        with open(heightmap, 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            heightmap_base64 = base64_encoded_data.decode('utf-8')
        with open(background, 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            background_base64 = base64_encoded_data.decode('utf-8')
        

        metadata={
            "assetName": assetName,
            "previewImageNft": {
                "mimetype": "image/png",
                "fileFromBase64": imageURL_base64,
                "description": "test description",
                "metadataPlaceholder": [
                {
                    "name": "rarities",
                    "value": rarities
                },
                {
                    "name": "planetName",
                    "value": planetName
                }
                ]
                
            },
            "subfiles": [
                {
                "mimetype": "image/png",
                "name":"space",
                "fileFromBase64": background_base64,
                "description": "Cosmic background for "+assetName,
                "totalAmount":"test"
                },
                {
                "name":"heightmap",
                "mimetype": "image/png",
                "fileFromBase64": heightmap_base64,
                "description": "Heightmap for "+assetName
                }
            ],
        }

        #print(metadata)
        response = requests.post(api_url, json=metadata)
        #print(response)
        return jsonify(response.json())
        #return jsonify(data)
    else:
        return jsonify(status="Request was not JSON")
     """

    

@app.route('/GetProjectPriceAndRarity/<string:projectID>', methods=['GET']) #get the amount of mintable nfts for each project, and the price of the nfts
def get_project_price_and_rarity(projectID):
    price=config.prices_and_rarity[projectID]["price"]
    toMint=config.prices_and_rarity[projectID]["toMint"]
    
    return jsonify({"price":price, "toMint":toMint})

@app.route('/CheckCardanoAddress/<string:address>', methods=['GET'])
def CheckCardanoAddress(address):
    api_url = "https://cardano-mainnet.blockfrost.io/api/v0/addresses/"+str(address)+"/total"
    print(api_url)
    headers={'project_id':'cAiR6OBMC8HcwEc8kf9BVPR05eqW1Cx0'}
    response = requests.get(api_url, headers=headers)
    
    return jsonify(response.json())

@app.route('/CheckAsset/<string:asset>', methods=['GET'])
def CheckAsset(asset):
    api_url = "https://cardano-mainnet.blockfrost.io/api/v0/assets/"+str(asset)
    print(api_url)
    headers={'project_id':'cAiR6OBMC8HcwEc8kf9BVPR05eqW1Cx0'}
    response = requests.get(api_url, headers=headers)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)