"""
ABI Fetcher Module.

This module retrieves contract ABIs from blockchain explorer APIs
for various DEX contracts (factory, router, masterchef) across
multiple blockchain networks.
"""

import simplejson as json
import time
import requests
from typing import Dict, Any

# Configuration constants
ETHERSCAN_API_KEY: str = "P9V56281GVUXJB7V7D5TQPI6HF9TPNGUJ6"
REQUEST_TIMEOUT: int = 30
CACHE_BASE_PATH: str = "../../data/cache"

with open(f'{CACHE_BASE_PATH}/bridgeableDexs.json', 'r', encoding='utf-8') as cacheFile:
    chainsDetails: Dict[str, Any] = json.load(cacheFile)

with open(f'{CACHE_BASE_PATH}/chainExplorers.json', 'r', encoding='utf-8') as cacheFile:
    chainExplorers: Dict[str, Any] = json.load(cacheFile)

chainAbis: Dict[str, Dict] = {}


def saveToCache(fileName: str, fileData: Dict[str, Any]) -> None:
    """
    Save data to a JSON cache file.

    Args:
        fileName: Name of the cache file (without extension)
        fileData: Dictionary data to serialize and save
    """
    with open(f'{CACHE_BASE_PATH}/{fileName}.json', 'w', encoding='utf-8') as cacheFile:
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
                    apiUrl = f"{apiBase}/api?module=contract&action=getabi&address={address}&format=raw&apikey={etherscanAPIKey}"
                    try:
                        chainAbis[chainId][dex["name"]] = {}
                        ABI = requests.get(apiUrl).json()
                        chainAbis[chainId][dex["name"]][contract] = ABI
                        print(ABI, "\n")
                    except Exception:
                        pass
                else:
                    print(f"Missing {contract}")

saveToCache("chainABIs", chainAbis)

x = 1