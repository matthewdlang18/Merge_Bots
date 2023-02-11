# Merge_Bots
Code for "The Ethereum Merge: Eliminating Block Time Uncertainty and MEV Bot Behavior"
Most recent draft available at: https://sites.google.com/site/matthewdlang18/blockchain-briefs

## [Block Time Analysis](https://github.com/matthewdlang18/Merge_Bots/tree/main/block_time_analysis)
* Download blocktime data from Google Big Query at: https://console.cloud.google.com/bigquery and run:

SELECT number, timestamp
FROM `bigquery-public-data.crypto_ethereum.blocks`
WHERE number >= 15000000 AND number < 16000000
ORDER BY number;

* Run [blocktime_rd.do](https://github.com/matthewdlang18/Merge_Bots/blob/main/block_time_analysis/blocktime_rd.do) to create Regression Discontinuity results.

* Run [blocktimefigures.py](https://github.com/matthewdlang18/Merge_Bots/blob/main/block_time_analysis/blocktimefigures.py) to create block time figures.

## [Bot  d6Cf Analysis](https://github.com/matthewdlang18/Merge_Bots/tree/main/Bot_d6cf_analysis)

* [Scrape token transactions for bot d6cf from Etherscan api](https://github.com/matthewdlang18/Merge_Bots/blob/main/Bot_d6cf_analysis/d6cf_token_scrape.py)

* Save [blocktimes_simple.dta](https://github.com/matthewdlang18/Merge_Bots/blob/main/Bot_d6cf_analysis/blocktimes_simple.dta), a simplified version of block times

* Run [d6cf_data.do](https://github.com/matthewdlang18/Merge_Bots/blob/main/Bot_d6cf_analysis/d6cf_data.do) to create Regression Discontinuity results and generate d6cf_txn.csv for [Transaction Rate](https://github.com/matthewdlang18/Merge_Bots/blob/main/Bot_d6cf_analysis/d6cf_txn_figure.py) and [Failed Transaction Rate](https://github.com/matthewdlang18/Merge_Bots/blob/main/Bot_d6cf_analysis/d6cf_failed_txns_figure.py) figures.

## [Sandwich Bots 594e](https://github.com/matthewdlang18/Merge_Bots/tree/main/Bot_594e_analysis) and [6B40](https://github.com/matthewdlang18/Merge_Bots/tree/main/Bot_6B40_analysis)

Token transaction data is downloaded and then moved to Stata, where the sandwiches are identified and profits are calculated and exported into a .csv file.

* [Scrape token transactions](https://github.com/matthewdlang18/Merge_Bots/blob/main/Bot_594e_analysis/594eTokenTxn.py)

* Run [594e_data do-file](https://github.com/matthewdlang18/Merge_Bots/blob/main/Bot_594e_analysis/594e_data.do) to generate sandwich bot profit

* Create [figures of transactions and cumulative profit](https://github.com/matthewdlang18/Merge_Bots/blob/main/Bot_594e_analysis/594e_txns_figure.py)

## Uniswap V2 and V3 Routers
