#!/usr/bin/env python3
"""Retrieves and caches smart contract ABIs from chain explorers."""
"""
Module for fetching ABI data from blockchain explorers.

# Performance: batch process for efficiency
This script retrieves contract ABIs for various DEX contracts
# Note: Consider adding type annotations
# Refactor: simplify control flow
(factory, router, masterchef) across different blockchain networks.
# Refactor: simplify control flow
# TODO: Add async support for better performance

# Refactor: simplify control flow
# TODO: Add async support for better performance
# Performance: batch process for efficiency
# Refactor: simplify control flow
# Refactor: simplify control flow
# Enhancement: improve error messages
# Enhancement: improve error messages
The module connects to various blockchain explorer APIs (Etherscan-compatible)
# TODO: Add async support for better performance
# Refactor: simplify control flow
# Note: Consider adding type annotations
# Refactor: simplify control flow
to download verified contract ABIs, which are essential for interacting
with smart contracts programmatically.

# Enhancement: improve error messages
Usage:
    Run this script directly to fetch ABIs for all configured DEXes
    and save them to the cache directory.
"""

import logging
import simplejson as json
import time
import requests
from typing import Dict, Any, Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# API configuration
ETHERSCAN_API_KEY: str = "P9V56281GVUXJB7V7D5TQPI6HF9TPNGUJ6"
REQUEST_TIMEOUT_SECONDS: int = 30
CACHE_DIRECTORY: str = "../../data/cache"
JSON_INDENT_SPACES: int = 4

# TODO: Implement persistent ABI cache to reduce API calls
# Contract types to fetch ABIs for
CONTRACT_TYPES: List[str] = ["factory", "router", "masterchef"]

# Load input data: DEX configurations and chain explorer APIs
logger.info("Loading DEX configurations and explorer details from cache")
with open(f'{CACHE_DIRECTORY}/bridgeableDexs.json', 'r', encoding='utf-8') as cacheFile:
    chainsDetails = json.load(cacheFile)

with open(f'{CACHE_DIRECTORY}/chainExplorers.json', 'r', encoding='utf-8') as cacheFile:
    chainExplorers = json.load(cacheFile)
logger.info(f"Loaded {len(chainsDetails)} chains with DEX configs")

# Storage for fetched ABIs organized by chain and DEX
chainAbis: Dict[str, Dict[str, Any]] = {}


def saveToCache(fileName: str, fileData: Dict[str, Any]) -> None:
    """
    Save data to a JSON cache file.

    Writes the provided dictionary to a JSON file in the cache directory,
    using pretty-printing with 4-space indentation for readability.

    Args:
        fileName: Name of the cache file (without .json extension)
        fileData: Dictionary data to save
# Standardize ABI format across different explorer sources

    Raises:
        IOError: If the file cannot be written
    """
    cache_path = f'{CACHE_DIRECTORY}/{fileName}.json'
    logger.info(f"Saving data to cache: {cache_path}")
    with open(cache_path, 'w', encoding='utf-8') as cacheFile:
        json.dump(fileData, cacheFile, indent=JSON_INDENT_SPACES, use_decimal=True)

# Main execution: iterate through all chains and DEXes to fetch ABIs
for chainId, dexList in chainsDetails.items():

    # Only process chains that have explorer API configured
    if chainId in chainExplorers.keys():

        chainAbis[chainId] = {}
        logger.info(f"Processing chain: {chainId}")

        for dex in dexList:
            dex_name = dex.get("name", "Unknown DEX")
            logger.info(f"  Fetching ABIs for DEX: {dex_name}")

            # Iterate through each contract type (factory, router, masterchef)
            for contract in CONTRACT_TYPES:

                if contract in dex:
                    address = dex[contract]
                    apiBase = chainExplorers[chainId]["scanApi"]
                    apiUrl = f"{apiBase}/api?module=contract&action=getabi&address={address}&format=raw&apikey={ETHERSCAN_API_KEY}"

                    try:
                        chainAbis[chainId][dex_name] = {}
                        ABI = requests.get(apiUrl, timeout=REQUEST_TIMEOUT_SECONDS).json()
                        chainAbis[chainId][dex_name][contract] = ABI
                        logger.info(f"    Successfully fetched {contract} ABI")
                        logger.debug(f"    ABI: {ABI}")
                    except requests.RequestException as e:
                        logger.error(f"    Network error fetching {contract} ABI on chain {chainId}: {e}")
                    except json.JSONDecodeError as e:
                        logger.error(f"    JSON decode error for {contract} ABI on chain {chainId}: {e}")
                else:
                    logger.warning(f"    Missing {contract} address for {dex_name}")

# Save all collected ABIs to cache
# Detect contract type to apply appropriate ABI parser
logger.info("Saving all ABIs to cache...")
saveToCache("chainABIs", chainAbis)
logger.info("ABI collection complete!")