from flask import Flask, json, jsonify
from flask import abort, request
import requests
from flask_cors import CORS

import base64

app = Flask(__name__)

#Enable CORS for local testing
CORS(app, origins= ["http://localhost:3000","http://localhost:5000", "http://localhost:5500","http://127.0.0.1:5500","http://127.0.0.1:3000","https://cardaworlds.io","https://viewer.cardaworlds.io","https://www.cardaworlds.io","https://cardaworlds.github.io"])

#Enable CORS for production website. Replace this with your website URL from where the requests will be made
#CORS(app, origins= ["https://yourwebsite.io","https://www.yourwebsite.io"])

import os 
API_KEY = os.environ.get('API_KEY')
API_KEY=str(API_KEY)    

#NFT price in lovelaces
nft_price=12000000 

@app.route('/GetNfts/<string:projectID>', methods=['GET'])
def get_nfts(projectID):
    api_url = "https://api.nft-maker.io/GetNfts/" + API_KEY + "/"+projectID+"/all"
    print(api_url)
    response = requests.get(api_url)
    return jsonify(response.json())

@app.route('/GetNftDetails/<string:projectID>/<string:name>', methods=['GET'])
def get_nft_details(projectID, name):
    price=nft_price
    api_url = "https://api.nft-maker.io/GetNftDetails/" + API_KEY + "/" + projectID + "/" + name
    response = requests.get(api_url)
    new_json = response.json()
    new_json["price"]=price
    return jsonify(new_json)

@app.route('/GetNftDetailsById/<string:projectID>/<string:nft_id>', methods=['GET'])
def get_nft_details_by_id(projectID, nft_id):
    price=nft_price
    api_url = "https://api.nft-maker.io/GetNftDetailsById/" + API_KEY + "/" + projectID + "/" + nft_id
    response = requests.get(api_url)
    new_json = response.json()
    new_json["price"]=price
    return jsonify(new_json)

@app.route('/GetAddressForSpecificNftSale/<string:projectID>/<string:nft_id>', methods=['GET'])
def get_address_for_specific_nft_sale(projectID, nft_id):
    price=nft_price
    api_url = "https://api.nft-maker.io/GetAddressForSpecificNftSale/" + API_KEY + "/" + projectID + "/" + nft_id + "/1/"+price
    print(api_url)
    response = requests.get(api_url)
    return jsonify(response.json())


@app.route('/GetAddressForRandomNftSale/<string:projectID>/<int:amountToBuy>', methods=['GET'])
def get_address_for_random_nft_sale(projectID, amountToBuy):
    if(amountToBuy==1):
        price=str(nft_price)
    elif(amountToBuy==3):
        price=str(nft_price*3)
    elif(amountToBuy==5):
        price=str(nft_price*5)
    else:
        return("Amount not allowed")
    api_url = "https://api.nft-maker.io/GetAddressForRandomNftSale/" + API_KEY + "/" + projectID + "/"+str(amountToBuy)+"/"+price
    print(api_url)
    response = requests.get(api_url)
    print(response)

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

### API endpoint used to upload NFTs in batch

# @app.route('/UploadNft', methods=['POST'])
# def UploadNft():
    
#     comma=", "
#     print(request)
#     if request.is_json:
#         data = request.get_json()
#         print(data)
#         projectID = data['projectID']
#         api_url = "https://api.nft-maker.io/UploadNft/" + API_KEY + "/" + projectID
#         print(api_url)
#         assetName = data["assetName"]
#         planetName = data["planetName"]
#         imageURL = data["imageURL"]
#         heightmap=data["heightmap"]
#         background=data["background"]
#         galaxyType=data["galaxyType"]
#         #rarities=comma.join(data["rarities"])
#         rarities=data["rarities"]
        
#         with open(imageURL, 'rb') as binary_file:
#             binary_file_data = binary_file.read()
#             base64_encoded_data = base64.b64encode(binary_file_data)
#             imageURL_base64 = base64_encoded_data.decode('utf-8')
#         with open(heightmap, 'rb') as binary_file:
#             binary_file_data = binary_file.read()
#             base64_encoded_data = base64.b64encode(binary_file_data)
#             heightmap_base64 = base64_encoded_data.decode('utf-8')
#         with open(background, 'rb') as binary_file:
#             binary_file_data = binary_file.read()
#             base64_encoded_data = base64.b64encode(binary_file_data)
#             background_base64 = base64_encoded_data.decode('utf-8')
        

#         metadata={
#             "assetName": assetName,
#             "previewImageNft": {
#                 "mimetype": "image/png",
#                 "fileFromBase64": imageURL_base64,
#                 "description": planetName,
#                 "metadataPlaceholder": [
#                 {
#                     "name": "rarities",
#                     "value": rarities
#                 },
#                 {
#                     "name": "planetName",
#                     "value": planetName
#                 },
#                 {
#                     "name": "galaxyType",
#                     "value": galaxyType
#                 }
#                 ]
                
#             },
#             "subfiles": [
#                 {
#                 "name":"heightmap",
#                 "mimetype": "image/png",
#                 "fileFromBase64": heightmap_base64,
#                 "description": "Heightmap for "+assetName
#                 },
#                 {
#                 "mimetype": "image/png",
#                 "name":"space",
#                 "fileFromBase64": background_base64,
#                 "description": "Cosmic background for "+assetName,
#                 },
#                 {
#                 "mimetype": "image/png",
#                 "name":"map",
#                 "fileFromBase64": imageURL_base64,
#                 "description": "Map for "+assetName,
#                 }
#             ],
#         }

#         #print(metadata)
#         response = requests.post(api_url, json=metadata)
#         #print(response)
#         return jsonify(response.json())
#         #return jsonify(data)
#     else:
#         return jsonify(status="Request was not JSON")
    

if __name__ == '__main__':
    app.run(debug=True)