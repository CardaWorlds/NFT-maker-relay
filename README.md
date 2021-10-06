# NFT-maker-relay
Flask app for use with NFT-maker

To use for local testing, open a terminal and enter SET API_KEY="<YOUR NFT MAKER KEY>"

To run this locally, simply create a virtual environment and run *pip install -r requirements.txt* to install the requirements.

You can easily [deploy this app to Heroku](https://devcenter.heroku.com/articles/git). You then simply have to add your configure your API key as a config variable for heroku by entering:
heroku config:set API_KEY="<YOUR NFT MAKER KEY>"


## Main things to modify
You can change the nft_price variable to the price at which you wish to sell your NFTs.

You should also modify CORS to only allow requests from your website.

## To use the API from your front end
You can use the same endpoints as the [NFT-maker pro API](https://api.nft-maker.io/swagger/index.html), but omitting the API key.

rodrigo@cardaworlds.io
