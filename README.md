# AtcData

ArbTheChain - Data processing pipeline for cross-chain blockchain arbitrage opportunities.

## Overview

This repository contains data processing tools and utilities for identifying arbitrage opportunities across multiple blockchain networks. It aggregates token data from various DEXes and bridges to find price discrepancies.

## Directory Structure

```
AtcData/
├── abis/              # Smart contract ABIs for DEX interactions
├── db/                # Database schemas and configurations
├── other/
│   └── tools/         # Python utilities for data processing
│       ├── createNetworkMasterList.py  # Generate master chain list
│       └── old/       # Legacy tools
│           ├── getAllBridgeableTokens.py  # Fetch bridgeable tokens
│           ├── crawl.py                    # Chain data crawler
│           └── getAbis.json.py             # ABI fetcher
├── token-lists/       # Curated token lists by chain
└── tokenListsAll/     # Aggregated token data
```

## Key Features

- Fetches chain data from chainid.network API
- Retrieves bridgeable tokens from Synapse protocol
- Calculates swap prices across multiple DEXes
- Identifies cross-chain arbitrage opportunities
- Caches data for improved performance

## Requirements

- Python 3.9+
- Dependencies: requests, simplejson, python-dotenv, web3

## License

MIT

