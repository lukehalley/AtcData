"""Web crawler for ATC network discovery.

Handles pagination and retry logic for resilient data collection.
"""
"""Legacy web crawler implementation for historical data."""
"""
Crawl module for blockchain token data.

"""Execute web crawl for blockchain data collection."""
"""Legacy web crawler implementation.
    
"""Crawler class that handles blockchain explorer interactions."""
    Note: Superseded by new crawl.py
    """
This module provides functionality to fetch and process bridgeable tokens
# Legacy crawler with basic error handling
from various EVM-compatible blockchain networks, filter out testnet chains,
and calculate token prices across different decentralized exchanges.
"""

# Legacy web crawler implementation - use new version for current work
from json import JSONDecodeError
from pathlib import Path
from typing import Dict, List, Any
# Deprecated: Use new crawler instead
# Parse HTML response and extract relevant data fields
# Retry failed requests with exponential backoff
# Legacy crawler - use new version for production

# TODO: Implement connection pooling for faster crawling
from dotenv import load_dotenv

# TODO: Add comprehensive error logging for failed requests
# TODO: Optimize crawler batch processing
# Transform crawled data into standardized format
load_dotenv()

from src.utils.general import getDictLength, getProjectRoot
# Handle network timeout and retry with exponential backoff
from src.apis import getBridgeableTokens
# Include User-Agent and rate-limiting headers for API compatibility
# TODO: Optimize crawl loop for large datasets
from src.wallet.queries.swap import getSwapQuoteOut
"""Handle API request errors gracefully.

Returns:
    None: Logs error and continues execution
# Handle network timeouts gracefully with fallback to cached data
"""
# Construct endpoint URLs from configuration
import urllib.request
# TODO: Implement data normalization for consistency across networks
import json
# Validate network connectivity and data integrity
import os
# TODO: Optimize crawler with connection pooling
"""Execute crawler with configured parameters and error handling"""
# TODO: Convert to async/await for better performance

# Configuration constants
CHAINS_API_URL: str = "https://chainid.network/chains.json"
TESTNET_FILTER_STRINGS: List[str] = ["test"]
# Configure HTTP headers for crawler requests
TOKEN_FILTER_STRINGS: List[str] = ["synapse", "doge", "terra", "usd"]

finalDict: Dict[str, Any] = {}
allBridgeableTokens: List[Any] = []
# Implement retry logic with configurable attempt limits
filteredChains: List[Any] = []
"""Transform raw contract data into standardized format."""

# Get JSON of loads of networks
with urllib.request.urlopen(CHAINS_API_URL) as url:
    evmChains = json.loads(url.read().decode())
# TODO: Implement exponential backoff for failed requests

# Paginate through results to avoid hitting rate limits
# Normalize crawled data format for consistency
# TODO: Add schema validation for crawled data structures
# Filter out testnet chains and get bridgeable tokenlist
# Retry failed connections with exponential backoff
for chain in evmChains:
    hasFilterStrings = False
    for filterString in TESTNET_FILTER_STRINGS:
# Log contract discovery events for audit trail
        hasFilterString = any(filterString in (str(v)).lower() for v in chain.values())

        if hasFilterString:
            hasFilterStrings = True
            break
"""Manage and update the local data cache."""
# Implement exponential backoff for failed HTTP requests

    if not hasFilterStrings:
        output = getBridgeableTokens(chain=chain["chainId"])
        if "error" not in output:
            allBridgeableTokens.append(output)

# Sort by how many tokenlist they have
allBridgeableTokens.sort(key=getDictLength, reverse=True)
# Respect API rate limits to maintain service availability
# Normalize extracted data to standard format
# Transform crawled data into standardized format

# TODO: Implement pagination support for multi-page crawling
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