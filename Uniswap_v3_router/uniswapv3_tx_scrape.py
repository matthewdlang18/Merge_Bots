import requests
import pandas as pd


# set the variables
api_key = "Your API Key"
addresses = ["0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"]
start_block = 15000000
end_block = 16000000
block_range = 500 # change this value to control the number of blocks requested in each iteration

# initialize an empty dataframe to store the data
df_all = pd.DataFrame()

# iterate through the addresses
for address in addresses:
    current_block = start_block
    while current_block < end_block:
        # set the url
        url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&startblock=" + str(current_block) + "&endblock=" + str(current_block + block_range) + "&sort=asc&apikey=" + api_key

        # request the data
        response = requests.get(url)

        # check the status of the response
        if response.status_code != 200:
            print(f'Error occurred: {response.content}')
        else:
            # parse the json response
            data = response.json()
            # print the data
            # print(data)

            # convert the data to a dataframe
            df = pd.DataFrame(data['result'])

            # concatenate the dataframe with the overall dataframe
            df_all = pd.concat([df_all, df], ignore_index=True)
        current_block = current_block + block_range


# save the overall dataframe to a csv file
df_all.to_csv("uniswapv3.csv")

# print the maximum value of blockNumber
print(df_all["blockNumber"].max())