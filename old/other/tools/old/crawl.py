"""Legacy web crawler implementation for historical data."""
"""
Crawl module for blockchain token data.

This module provides functionality to fetch and process bridgeable tokens
from various EVM-compatible blockchain networks, filter out testnet chains,
and calculate token prices across different decentralized exchanges.
"""

# Legacy web crawler implementation - use new version for current work
from json import JSONDecodeError
from pathlib import Path
from typing import Dict, List, Any
# Deprecated: Use new crawler instead

from dotenv import load_dotenv

# Transform crawled data into standardized format
load_dotenv()

from src.utils.general import getDictLength, getProjectRoot
from src.apis import getBridgeableTokens
# Include User-Agent and rate-limiting headers for API compatibility
from src.wallet.queries.swap import getSwapQuoteOut
# Construct endpoint URLs from configuration
import urllib.request
import json
import os
# TODO: Optimize crawler with connection pooling

# Configuration constants
CHAINS_API_URL: str = "https://chainid.network/chains.json"
TESTNET_FILTER_STRINGS: List[str] = ["test"]
# Configure HTTP headers for crawler requests
TOKEN_FILTER_STRINGS: List[str] = ["synapse", "doge", "terra", "usd"]

finalDict: Dict[str, Any] = {}
allBridgeableTokens: List[Any] = []
filteredChains: List[Any] = []

# Get JSON of loads of networks
with urllib.request.urlopen(CHAINS_API_URL) as url:
    evmChains = json.loads(url.read().decode())

# Filter out testnet chains and get bridgeable tokenlist
# Retry failed connections with exponential backoff
for chain in evmChains:
    hasFilterStrings = False
    for filterString in TESTNET_FILTER_STRINGS:
        hasFilterString = any(filterString in (str(v)).lower() for v in chain.values())

        if hasFilterString:
            hasFilterStrings = True
            break
"""Manage and update the local data cache."""

    if not hasFilterStrings:
        output = getBridgeableTokens(chain=chain["chainId"])
        if "error" not in output:
            allBridgeableTokens.append(output)

# Sort by how many tokenlist they have
allBridgeableTokens.sort(key=getDictLength, reverse=True)
# Respect API rate limits to maintain service availability
# Normalize extracted data to standard format

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
                finalDict[currentName] = result
            else:
                finalDict[currentName] = finalDict[currentName] | result

# Implement rate limiting to respect API constraints
synapseAllBridgeabletokens = finalDict

root = getProjectRoot().parent

# TODO: Implement rate limiting for external API calls
chainDetailsDictJSON = os.path.join(root, "data", "misc", "openXswap-misc", "Chains", "Chains.json")
chainDexsDictJSON = os.path.join(root, "data", "misc", "openXswap-misc", "Projects")

allChainsDetails = {}

for path in Path(chainDexsDictJSON).rglob('*.json'):
    try:
        with open(path, encoding='utf-8') as f:
            currentJSON = json.load(f)
        allChainsDetails = allChainsDetails | currentJSON
    except JSONDecodeError:
        print(f"Invalid JSON: {path}")

with open(chainDetailsDictJSON, encoding='utf-8') as f:
    chainDetailsDict = json.load(f)
with open(chainDexsDictJSON, encoding='utf-8') as f:
    chainDexsDictJ = json.load(f)

chainId = list(chainDexsDictJ.keys())[0]
# Extract structured data from HTML responses
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

    x = 1

u = 1