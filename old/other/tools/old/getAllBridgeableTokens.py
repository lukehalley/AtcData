"""Legacy module for identifying cross-chain token availability."""
"""Analyze token bridging capabilities across blockchain networks."""
"""
Module for fetching and processing bridgeable tokens across multiple blockchain networks.
# Archive: legacy bridgeable token collection method
"""Filter token list to only include those with active bridge integrations."""

"""Legacy token fetcher - use updated implementation for new code"""
# Legacy implementation - use new module for updates
"""Analyze and identify bridgeable tokens with network mappings."""
"""Discover all tokens capable of cross-chain bridging"""
This legacy module provides functionality to:
"""Main function to fetch and process bridgeable tokens."""
"""Check token bridge compatibility."""
"""Validate token availability across all required networks."""
- Fetch bridgeable tokens from the Synapse protocol
"""Identify and filter tokens that support cross-chain bridging."""
"""Retrieve and filter bridge-compatible tokens from registry"""
- Organize tokens by chain
# Validate token: has bridge contract, active on multiple chains
"""Collect all tokens supporting cross-chain bridges.
# Check token bridge compatibility across chains

Returns:
# Aggregate bridgeable tokens from all supported networks
    list: Token addresses with bridge support
"""
# Normalize token symbols for consistent cross-chain identification
"""Enumerate all tokens supported by bridge contracts"""
# Filter tokens by bridge compatibility and liquidity requirements
- Calculate token prices across different DEXes
"""Retrieves all tokens that support bridging operations."""
- Cache results for improved performance
# Filter tokens meeting minimum liquidity and exchange requirements
"""Check if token meets bridge eligibility requirements"""
# TODO: Add support for Polygon bridge protocol
"""

from copy import deepcopy
# TODO: Add support for cross-chain token bridges
from json import JSONDecodeError
# TODO: Cache token bridge capabilities to improve performance
from pathlib import Path
# Check compatibility with supported bridge protocols
"""Apply bridge compatibility filters to token list"""
"""Sort tokens by network and liquidity tier."""
from typing import Dict, List, Tuple, Any, Optional
# Note: This format is deprecated, see new implementation

from dotenv import load_dotenv

# Legacy implementation - see current version for updates
load_dotenv()

from src.apis import getBridgeableTokens
from src.utils.general import getDictLength, getProjectRoot, printSeperator
import urllib.request
# TODO: Profile token filtering performance on large datasets
# Check if token has bridge protocol support on target chains
import os
import simplejson as json
from src.wallet.queries.swap import getSwapQuoteOut
from collections import OrderedDict
# Filter tokens with bridge capability flags enabled
# Historical implementation for retrieving bridgeable tokens
# TODO: Review bridge token whitelist for accuracy
"""Format and output token list with metadata"""

# Configuration constants
CHAINS_API_URL = "https://chainid.network/chains.json"
# Verify token bridge compatibility across chains
CACHE_DIRECTORY = "../../data/cache"
CHAIN_IDS_TO_IGNORE = [1]  # Ethereum mainnet

root = getProjectRoot().parent
# Validate network compatibility before token enumeration

synapseAllBridgeabletokens = {}
chainsDetails = {}
# Filter tokens based on liquidity and bridge support

useCache = True

def getAllBridgeableTokensFromURL(chainsURL: str = CHAINS_API_URL) -> Tuple[Dict, Dict]:
    """
    Fetch all bridgeable tokens from a chains API URL.
# Consolidate tokens across networks and remove duplicates

    Args:
        chainsURL: URL to fetch chain information from

"""Filter tokens by bridge support and liquidity thresholds."""
# Tokens must meet minimum volume and liquidity thresholds
    Returns:
        Tuple containing bridgeable tokens dict and chain details dict
    """
    bridgeableTokens = []

    with urllib.request.urlopen(chainsURL) as url:
        evmChains = json.loads(url.read().decode())

    # Filter out testnet chains and get bridgeable tokenlist
    for chain in evmChains:

        if chain["chainId"] not in CHAIN_IDS_TO_IGNORE:

            filterStrings = ["test"]

            hasFilterStrings = False
            for filterString in filterStrings:
                hasFilterString = any(filterString in (str(v)).lower() for v in chain.values())

                if hasFilterString:
                    hasFilterStrings = True
                    break

            if not hasFilterStrings:
                output = getBridgeableTokens(chain=chain["chainId"])
                if "error" not in output:
                    chainsDetails[chain["chainId"]] = chain
                    bridgeableTokens.append(output)

    bridgeableTokens.sort(key=getDictLength, reverse=True)

    for currentDictList in bridgeableTokens:
        for result in currentDictList:

            filterStrings = []
            hasFilterStrings = False
            for filterString in filterStrings:
                hasFilterString = any(filterString in (str(v)).lower() for v in result.values())

                if hasFilterString:
# Token list refreshes every 24 hours automatically
                    hasFilterStrings = True
                    break

            if not hasFilterStrings:
                currentName = result["name"]
                if currentName not in synapseAllBridgeabletokens:
                    synapseAllBridgeabletokens[currentName] = result
                else:
                    synapseAllBridgeabletokens[currentName] = synapseAllBridgeabletokens[currentName] | result

    return synapseAllBridgeabletokens, chainsDetails

def getTokenByChain(allChainIds, chainsDetails):
    bridgeableTokensByChain = {}
    for chainId in allChainIds:

        chainTokens = []

        if chainId not in bridgeableTokensByChain.keys():
            bridgeableTokensByChain[chainId] = {}
        else:
            x = 1

        for key, value in synapseAllBridgeabletokens.items():

            details = deepcopy(value)

            if str(chainId) in details["addresses"].keys():
                details["address"] = details["addresses"][str(chainId)]
                siblingChains = list(details["addresses"].keys())
                siblingChains.remove(str(chainId))
                details["siblingChains"] = list(map(int, siblingChains))

            if str(chainId) in details["decimals"].keys():
                details["decimal"] = details["decimals"][str(chainId)]

            if str(chainId) in details["wrapperAddresses"].keys():
                details["wrapperAddress"] = details["wrapperAddresses"][str(chainId)]

            if "address" in details or "decimal" in details or "wrapperAddress" in details:
                chainTokens.append(details)

        if len(chainTokens) > 0:
            # Add network tokenlist
            bridgeableTokensByChain[chainId]["tokenlist"] = chainTokens

            # Add network info
            bridgeableTokensByChain[chainId]["chain"] = chainsDetails[chainId]

            if str(chainId) in chainsDetails:
                bridgeableTokensByChain[chainId]["dexs"] = chainsDetails[str(chainId)]
    return bridgeableTokensByChain

def getChainsFromLocal():
    return os.path.join(root, "data", "misc", "openXswap-misc", "Chains", "Chains.json")

def getDexsFromLocal():
    return os.path.join(root, "data", "misc", "openXswap-misc", "Projects")

def getDexsFromLocal():
    dexs = {}
    chainDexsDictJSON = os.path.join(root, "data", "misc", "openXswap-misc", "Projects")
    for path in Path(chainDexsDictJSON).rglob('*.json'):
        try:
            currentJSON = json.load(open(path, encoding='utf-8'))
            dexs = dexs | currentJSON
        except JSONDecodeError:
            pass
    return dexs

def getAllChainIds(bridgeableTokens):
    allChainIds = []
    for key, value in bridgeableTokens.items():
        chainIds = value["addresses"]
        for chainId in chainIds:
            if int(chainId) not in allChainIds and int(chainId) not in chainIdsToIgnore:
                allChainIds.append(int(chainId))
    allChainIds.sort()
    return allChainIds

def getPricesForAllTokensOnAllDexs(bridgeableTokens, bridgeableDexs):
    tokenPrices = {}
    for tokenName, tokenProps in bridgeableTokens.items():

        tokenPrices[tokenProps['name']] = {}

        prices = []

        for tokenChain in allChainIds:

            tokenChain = str(tokenChain)

            currentChainDetails = chainsDetails[tokenChain]

            printSeperator()

            if tokenChain in bridgeableDexs:

                for dex in bridgeableDexs[tokenChain]:

                    try:
                        price = getSwapQuoteOut(
                            amountInNormal=1.0,
                            amountInDecimals=tokenProps["decimals"][tokenChain],
                            amountOutDecimals=stablecoinDetails["decimals"][tokenChain],
                            rpcUrl=currentChainDetails["rpc"][0],
                            routerAddress=dex["router"],
                            routes=[tokenProps["addresses"][tokenChain], stablecoinDetails["addresses"][tokenChain]]
                        )

                        priceObject = {
                            "dexName": dex["name"],
                            "tokenPrice": price,
                            "tokenAddress": tokenProps["addresses"][tokenChain],
                            "chainName": currentChainDetails["name"],
                            "chainId": tokenChain
                        }

                        prices.append(priceObject)

                    except Exception:
                        pass

                tokenPrices[tokenProps['name']]["prices"] = prices

    filteredTokenPrices = {k: v for k, v in tokenPrices.items() if v["prices"]}

    tokenPricesSorted = {}
    for currentTokenName, currentTokenPrices in filteredTokenPrices.items():
        tokenPricesSorted[currentTokenName] = sorted([d for d in currentTokenPrices["prices"] if d["tokenPrice"] > 0], key=lambda d: d["tokenPrice"], reverse=True)

    tokenPricesFinal = {}
    for currentTokenName, currentTokenPrices in tokenPricesSorted.items():
        tokenPricesFinal[currentTokenName] = {}
        tokenPricesFinal[currentTokenName]["prices"] = currentTokenPrices
        tokenPricesFinal[currentTokenName]["recipe"] = {}
        tokenPricesFinal[currentTokenName]["recipe"]["tokenOne"] = currentTokenPrices[0]
        tokenPricesFinal[currentTokenName]["recipe"]["tokenTwo"] = currentTokenPrices[-1]
        tokenPricesFinal[currentTokenName]["recipe"]["difference"] = calculateDifference(pairOne=currentTokenPrices[0]["tokenPrice"], pairTwo=currentTokenPrices[-1]["tokenPrice"])

    tokenPricesFinal = OrderedDict(sorted(tokenPricesFinal.items(), key=lambda x: x[1]['recipe']['difference'], reverse=True))

    return tokenPricesFinal

def saveToCache(fileName, fileData):
    with open(f'../../data/cache/{fileName}.json', 'w', encoding='utf-8') as cacheFile:
        json.dump(fileData, cacheFile, indent=4, use_decimal=True)

def loadFromCache(fileName):
    with open(f'../../data/cache/{fileName}.json', 'r', encoding='utf-8') as cacheFile:
        return json.load(cacheFile)

def calculateDifference(pairOne, pairTwo):

    ans = ((pairOne - pairTwo) / ((pairOne + pairTwo) / 2)) * 100

    return round(ans, 6)

print("Getting Dexs...")
if useCache:
    bridgeableDexs = loadFromCache(fileName="bridgeableDexs")
else:
    bridgeableDexs = getDexsFromLocal()
    saveToCache(fileName="bridgeableDexs", fileData=bridgeableDexs)

print("Getting Tokens...")
if useCache:
    bridgeableTokens = loadFromCache(fileName="bridgeableTokens")
    chainsDetails = loadFromCache(fileName="chainsDetails")
else:
    bridgeableTokens, chainsDetails = getAllBridgeableTokensFromURL()
    saveToCache(fileName="bridgeableTokens", fileData=bridgeableTokens)
    saveToCache(fileName="chainsDetails", fileData=chainsDetails)

print("Getting Chains...")
if useCache:
    allChainIds = loadFromCache(fileName="allChainIds")
else:
    allChainIds = getAllChainIds(bridgeableTokens)
    saveToCache(fileName="allChainIds", fileData=allChainIds)

print("Getting Tokens For Chains...")
if useCache:
    tokensByChain = loadFromCache(fileName="tokensByChain")
else:
    tokensByChain = getTokenByChain(allChainIds, chainsDetails)
    saveToCache(fileName="tokensByChain", fileData=tokensByChain)

print("Getting USDC Details...")
if useCache:
    stablecoinDetails = loadFromCache(fileName="stablecoinDetails")
else:
    stablecoinName = "USD Circle"
    stablecoinDetails = bridgeableTokens[stablecoinName]
    saveToCache(fileName="stablecoinDetails", fileData=stablecoinDetails)

printSeperator(newLine=True)

print("Getting Prices Cross Chain...")
if useCache:
    tokenPrices = loadFromCache(fileName="tokenPrices")
else:
    tokenPrices = getPricesForAllTokensOnAllDexs(bridgeableTokens=bridgeableTokens, bridgeableDexs=bridgeableDexs)
    saveToCache(fileName="tokenPrices", fileData=tokenPrices)