"""
Module for fetching and processing bridgeable tokens across multiple blockchain networks.

This module provides functionality to:
- Fetch bridgeable tokens from the Synapse protocol
- Organize tokens by chain
- Calculate token prices across different DEXes
- Cache results for improved performance
"""

from copy import deepcopy
from json import JSONDecodeError
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

from dotenv import load_dotenv

load_dotenv()

from src.apis import getBridgeableTokens
from src.utils.general import getDictLength, getProjectRoot, printSeperator
import urllib.request
import os
import simplejson as json
from src.wallet.queries.swap import getSwapQuoteOut
from collections import OrderedDict

# Configuration constants
CHAINS_API_URL = "https://chainid.network/chains.json"
CACHE_DIRECTORY = "../../data/cache"
REQUEST_TIMEOUT_SECONDS = 30
MAX_RETRY_ATTEMPTS = 3
STABLECOIN_NAME = "USD Circle"

# Chain IDs to exclude from processing (e.g., Ethereum mainnet for cost reasons)
CHAIN_IDS_TO_IGNORE: List[int] = [1]

# Percentage calculation precision
PERCENTAGE_DECIMAL_PLACES = 6

root = getProjectRoot().parent

chainIdsToIgnore = CHAIN_IDS_TO_IGNORE  # Legacy alias for backward compatibility

synapseAllBridgeabletokens = {}
chainsDetails = {}

useCache = True

def getAllBridgeableTokensFromURL(chainsURL: str = CHAINS_API_URL) -> Tuple[Dict, Dict]:
    """
    Fetch all bridgeable tokens from a chains API URL.

    Args:
        chainsURL: URL to fetch chain information from

    Returns:
        Tuple containing bridgeable tokens dict and chain details dict
    """
    bridgeableTokens = []

    with urllib.request.urlopen(chainsURL) as url:
        evmChains = json.loads(url.read().decode())

    # Filter out testnet chains and get bridgeable tokenlist
    for chain in evmChains:

        if chain["chainId"] not in chainIdsToIgnore:

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
                    hasFilterStrings = True
                    break

            if not hasFilterStrings:
                currentName = result["name"]
                if currentName not in synapseAllBridgeabletokens:
                    synapseAllBridgeabletokens[currentName] = result
                else:
                    synapseAllBridgeabletokens[currentName] = synapseAllBridgeabletokens[currentName] | result

    return synapseAllBridgeabletokens, chainsDetails

def getTokenByChain(allChainIds: List[int], chainsDetails: Dict) -> Dict[int, Dict[str, Any]]:
    """
    Organize tokens by their chain ID for easier chain-specific lookups.

    This function restructures the global bridgeable tokens dictionary to be
    indexed by chain ID rather than token name. For each chain, it extracts:
    - The token's address on that specific chain
    - The token's decimals on that chain
    - Any wrapper addresses (for wrapped tokens)
    - Sibling chains where the token is also available (for bridging)

    Args:
        allChainIds: List of chain IDs to process
        chainsDetails: Dictionary containing chain information (RPC, name, etc.)

    Returns:
        Dictionary mapping chain IDs to objects containing:
        - tokenlist: List of token details for that chain
        - chain: Chain metadata from chainsDetails
        - dexs: Available DEXes on that chain (if any)

    Note:
        Uses deepcopy to avoid mutating the original token data when
        adding chain-specific fields like 'address' and 'siblingChains'.
    """
    bridgeableTokensByChain: Dict[int, Dict[str, Any]] = {}

    for chainId in allChainIds:
        chainTokens: List[Dict[str, Any]] = []

        # Initialize chain entry if not present
        if chainId not in bridgeableTokensByChain:
            bridgeableTokensByChain[chainId] = {}

        # Process each token to extract chain-specific information
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

def getChainsFromLocal() -> str:
    """
    Get the local file path for chain details JSON.

    Returns:
        Absolute path to the Chains.json file containing network metadata
    """
    return os.path.join(root, "data", "misc", "openXswap-misc", "Chains", "Chains.json")


def getDexsFromLocal() -> Dict[str, List[Dict[str, Any]]]:
    """
    Load DEX information from local JSON files.

    Scans the Projects directory recursively for all JSON files and merges
    them into a single dictionary. Each JSON file typically contains DEX
    configurations for one or more blockchain networks.

    Returns:
        Dictionary mapping chain IDs to lists of DEX configurations.
        Each DEX config includes router address, factory address, and name.

    Note:
        Invalid JSON files are silently skipped to allow partial data loading.
        Uses Python 3.9+ dictionary merge operator (|) for combining data.
    """
    dexs: Dict[str, List[Dict[str, Any]]] = {}
    chainDexsDictJSON = os.path.join(root, "data", "misc", "openXswap-misc", "Projects")

    # Recursively find all JSON files in the Projects directory
    for path in Path(chainDexsDictJSON).rglob('*.json'):
        try:
            with open(path, encoding='utf-8') as f:
                currentJSON = json.load(f)
            # Merge current file's data into the main dictionary
            dexs = dexs | currentJSON
        except JSONDecodeError:
            # Skip invalid JSON files silently
            pass
    return dexs

def getAllChainIds(bridgeableTokens: Dict) -> List[int]:
    """
    Extract all unique chain IDs from bridgeable tokens.

    Args:
        bridgeableTokens: Dictionary of bridgeable tokens with addresses

    Returns:
        Sorted list of unique chain IDs
    """
    allChainIds = []
    for key, value in bridgeableTokens.items():
        chainIds = value["addresses"]
        for chainId in chainIds:
            if int(chainId) not in allChainIds and int(chainId) not in chainIdsToIgnore:
                allChainIds.append(int(chainId))
    allChainIds.sort()
    return allChainIds

def getPricesForAllTokensOnAllDexs(bridgeableTokens: Dict, bridgeableDexs: Dict) -> OrderedDict:
    """
    Get token prices across all DEXes for arbitrage analysis.

    Args:
        bridgeableTokens: Dictionary of tokens with their properties
        bridgeableDexs: Dictionary of DEXes by chain ID

    Returns:
        OrderedDict of token prices sorted by price difference
    """
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

def saveToCache(fileName: str, fileData: Dict) -> None:
    """Save data to JSON cache file."""
    with open(f'{CACHE_DIRECTORY}/{fileName}.json', 'w', encoding='utf-8') as cacheFile:
        json.dump(fileData, cacheFile, indent=4, use_decimal=True)

def loadFromCache(fileName: str) -> Dict:
    """Load data from JSON cache file."""
    with open(f'{CACHE_DIRECTORY}/{fileName}.json', 'r', encoding='utf-8') as cacheFile:
        return json.load(cacheFile)

def calculateDifference(pairOne: float, pairTwo: float) -> float:
    """
    Calculate the percentage difference between two prices.

    Uses the average of both prices as the base for percentage calculation,
    which provides a symmetric measure of the price difference regardless
    of which price is used as the reference point.

    Formula: ((price1 - price2) / average) * 100

    Args:
        pairOne: First price value (typically the higher price)
        pairTwo: Second price value (typically the lower price)

    Returns:
        Percentage difference rounded to configured decimal places

    Example:
        >>> calculateDifference(105.0, 95.0)
        10.0  # 10% difference between 105 and 95
    """
    if pairOne == pairTwo:
        return 0.0

    average = (pairOne + pairTwo) / 2
    difference = ((pairOne - pairTwo) / average) * 100
    return round(difference, PERCENTAGE_DECIMAL_PLACES)

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
    # Use the configured stablecoin as the price reference
    stablecoinDetails = bridgeableTokens[STABLECOIN_NAME]
    saveToCache(fileName="stablecoinDetails", fileData=stablecoinDetails)

printSeperator(newLine=True)

print("Getting Prices Cross Chain...")
if useCache:
    tokenPrices = loadFromCache(fileName="tokenPrices")
else:
    tokenPrices = getPricesForAllTokensOnAllDexs(bridgeableTokens=bridgeableTokens, bridgeableDexs=bridgeableDexs)
    saveToCache(fileName="tokenPrices", fileData=tokenPrices)