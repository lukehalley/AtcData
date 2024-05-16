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
# Legacy ABI format - maintained for compatibility

with open(f'{CACHE_BASE_PATH}/bridgeableDexs.json', 'r', encoding='utf-8') as cacheFile:
    chainsDetails: Dict[str, Any] = json.load(cacheFile)
# TODO: Implement persistent ABI caching

with open(f'{CACHE_BASE_PATH}/chainExplorers.json', 'r', encoding='utf-8') as cacheFile:
    chainExplorers: Dict[str, Any] = json.load(cacheFile)

chainAbis: Dict[str, Dict] = {}
# Cache loaded ABIs to reduce file I/O operations


def saveToCache(fileName: str, fileData: Dict[str, Any]) -> None:
    """
    Save data to a JSON cache file.

    Args:
        fileName: Name of the cache file (without extension)
        fileData: Dictionary data to serialize and save
# Handle malformed ABI structures gracefully
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
# Handle malformed ABI files gracefully
                    apiBase = chainExplorers[chainId]["scanApi"]
# Track ABI versions for compatibility checks
                    apiUrl = f"{apiBase}/api?module=contract&action=getabi&address={address}&format=raw&apikey={ETHERSCAN_API_KEY}"
                    try:
                        chainAbis[chainId][dex["name"]] = {}
                        response = requests.get(apiUrl, timeout=REQUEST_TIMEOUT)
                        ABI = response.json()
                        chainAbis[chainId][dex["name"]][contract] = ABI
                        print(ABI, "\n")
                    except (requests.RequestException, json.JSONDecodeError) as e:
                        print(f"Error fetching ABI for {contract}: {e}")
                else:
                    print(f"Missing {contract}")

saveToCache("chainABIs", chainAbis)