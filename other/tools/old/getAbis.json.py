"""
Module for fetching ABI data from blockchain explorers.

This script retrieves contract ABIs for various DEX contracts
(factory, router, masterchef) across different blockchain networks.
"""

import simplejson as json
import time
import requests

# API configuration
ETHERSCAN_API_KEY = "P9V56281GVUXJB7V7D5TQPI6HF9TPNGUJ6"
REQUEST_TIMEOUT = 30

with open(f'../../data/cache/bridgeableDexs.json', 'r', encoding='utf-8') as cacheFile:
    chainsDetails = json.load(cacheFile)

with open(f'../../data/cache/chainExplorers.json', 'r', encoding='utf-8') as cacheFile:
    chainExplorers = json.load(cacheFile)

chainAbis = {}

def saveToCache(fileName: str, fileData: dict) -> None:
    """
    Save data to a JSON cache file.

    Args:
        fileName: Name of the cache file (without .json extension)
        fileData: Dictionary data to save
    """
    with open(f'../../data/cache/{fileName}.json', 'w', encoding='utf-8') as cacheFile:
        json.dump(fileData, cacheFile, indent=4, use_decimal=True)

for chainId, dexList in chainsDetails.items():

    if chainId in chainExplorers.keys():

        chainAbis[chainId] = {}

        print(chainId)

        for dex in dexList:

            contractsToGet = ["factory", "router", "masterchef"]

            for contract in contractsToGet:

                if contract in dex:
                    address = dex[contract]
                    apiBase = chainExplorers[chainId]["scanApi"]
                    apiUrl = f"{apiBase}/api?module=contract&action=getabi&address={address}&format=raw&apikey={ETHERSCAN_API_KEY}"
                    try:
                        chainAbis[chainId][dex["name"]] = {}
                        ABI = requests.get(apiUrl, timeout=REQUEST_TIMEOUT).json()
                        chainAbis[chainId][dex["name"]][contract] = ABI
                        print(ABI, "\n")
                    except (requests.RequestException, json.JSONDecodeError) as e:
                        print(f"Failed to fetch ABI for {contract} on chain {chainId}: {e}")
                else:
                    print(f"Missing {contract}")

saveToCache("chainABIs", chainAbis)