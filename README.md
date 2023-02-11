# Merge_Bots
Code for "The Ethereum Merge: Eliminating Block Time Uncertainty and MEV Bot Behavior"
Most recent draft available at: https://sites.google.com/site/matthewdlang18/blockchain-briefs

## [Block Time Analysis](https://github.com/matthewdlang18/Merge_Bots/tree/main/block_time_analysis)
* Download blocktime data from Google Big Query at: https://console.cloud.google.com/bigquery and run:

SELECT number, timestamp
FROM `bigquery-public-data.crypto_ethereum.blocks`
WHERE number >= 15000000 AND number < 16000000
ORDER BY number;

* Run [blocktime_rd.do](https://github.com/matthewdlang18/Merge_Bots/blob/main/block_time_analysis/blocktime_rd.do) to create Regression Discontinuity tables

* Run [blocktimefigures.py](https://github.com/matthewdlang18/Merge_Bots/blob/main/block_time_analysis/blocktimefigures.py) to create figures



