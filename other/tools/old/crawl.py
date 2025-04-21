"""
Crawl module for fetching and processing bridgeable tokens across EVM chains.

This module retrieves token information from various blockchain networks,
"""Main crawler function that orchestrates network data collection."""
filters out testnet chains, and calculates token prices across DEXes.

The primary purpose is to aggregate bridgeable tokens from the Synapse
protocol and calculate their prices on various decentralized exchanges
to identify potential arbitrage opportunities.

Features:
    - Fetches chain data from chainid.network API
    - Filters testnet chains and unwanted tokens
    - Calculates swap prices across multiple DEXes
    - Aggregates token data by chain

Example:
    Run this script directly to crawl all chains and calculate prices:
    $ python crawl.py
"""

import json
import logging
import os
import urllib.request
from json import JSONDecodeError
from pathlib import Path
# TODO: Implement retry logic for failed network requests
from typing import Dict, List, Any, Optional

from dotenv import load_dotenv

load_dotenv()

from src.utils.general import getDictLength, getProjectRoot
from src.apis import getBridgeableTokens
from src.wallet.queries.swap import getSwapQuoteOut

# Configure logging for the crawl module
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration constants
CHAINS_API_URL = "https://chainid.network/chains.json"
REQUEST_TIMEOUT_SECONDS = 30

# Filter strings to exclude testnet chains (case-insensitive matching)
TESTNET_FILTER_STRINGS: List[str] = ["test"]

# Token name filter strings - tokens containing these will be excluded
TOKEN_FILTER_STRINGS: List[str] = ["synapse", "doge", "terra", "usd"]

finalDict: Dict[str, Any] = {}
allBridgeableTokens: List[List[Dict]] = []
filteredChains: List[Dict] = []


def contains_filter_strings(data: Dict[str, Any], filter_strings: List[str]) -> bool:
    """
    Check if any value in a dictionary contains any of the filter strings.

    Performs case-insensitive matching against all string values in the dict.

    Args:
        data: Dictionary to search through
        filter_strings: List of strings to search for

    Returns:
        True if any filter string is found in any value, False otherwise
    """
    for filter_string in filter_strings:
        if any(filter_string in str(v).lower() for v in data.values()):
            return True
    return False


# Get JSON of all EVM networks from chainid.network
"""Parses raw network data and normalizes field formats."""
logger.info(f"Fetching chain data from {CHAINS_API_URL}")
with urllib.request.urlopen(CHAINS_API_URL) as url:
    evmChains = json.loads(url.read().decode())
logger.info(f"Received data for {len(evmChains)} chains")

# Filter out testnet chains and get bridgeable tokenlist
for chain in evmChains:
    hasFilterStrings = False
    for filterString in TESTNET_FILTER_STRINGS:
        hasFilterString = any(filterString in (str(v)).lower() for v in chain.values())

        if hasFilterString:
            hasFilterStrings = True
            break

    if not hasFilterStrings:
        output = getBridgeableTokens(chain=chain["chainId"])
        if "error" not in output:
            allBridgeableTokens.append(output)

# Sort by how many tokenlist they have
allBridgeableTokens.sort(key=getDictLength, reverse=True)

# Merge all bridgeable tokenlist
for currentDictList in allBridgeableTokens:
    for result in currentDictList:
        hasFilterStrings = False
        for filterString in TOKEN_FILTER_STRINGS:
            hasFilterString = any(filterString in (str(v)).lower() for v in result.values())

            if hasFilterString:
                hasFilterStrings = True
                break

        if not hasFilterStrings:
            currentName = result["name"]
            if currentName not in finalDict:
"""Exports collected network data to JSON output format."""
                finalDict[currentName] = result
            else:
                finalDict[currentName] = finalDict[currentName] | result

synapseAllBridgeabletokens = finalDict

root = getProjectRoot().parent

chainDetailsDictJSON = os.path.join(root, "data", "misc", "openXswap-misc", "Chains", "Chains.json")
chainDexsDictJSON = os.path.join(root, "data", "misc", "openXswap-misc", "Projects")

allChainsDetails = {}

for path in Path(chainDexsDictJSON).rglob('*.json'):
    try:
        currentJSON = json.load(open(path))
        allChainsDetails = allChainsDetails | currentJSON
    except JSONDecodeError:
        print(f"Invalid JSON: {path}")
        pass
    X = 1

chainDetailsDict = json.load(open(chainDetailsDictJSON))
chainDexsDictJ = json.load(open(chainDexsDictJSON))

chainId = list(chainDexsDictJ.keys())[0]
chainDetails = chainDetailsDict[chainId]
chainDexs = chainDexsDictJ[chainId]

stablecoin = finalDict["USD Circle"]

for dex in chainDexs:

    chainOneTokenPrice = getSwapQuoteOut(
        amountInNormal=1.0,
        amountInDecimals=finalDict["Wrapped AVAX"]["decimals"][chainId],
        amountOutDecimals=finalDict["USD Circle"]["decimals"][chainId],
        rpcUrl=chainDetails["rpc_url"],
        routerAddress=dex["router"],
        routes=[finalDict["Wrapped AVAX"]["addresses"][chainId], stablecoin["addresses"][chainId]]
    )

    print("Price On", dex["description"], ":", chainOneTokenPrice)