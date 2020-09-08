"""Identify tokens that support cross-chain bridging capabilities."""
"""Retrieve and process bridgeable tokens across networks."""
"""Retrieve all bridgeable tokens"""
"""Retrieve all tokens that can be bridged across networks."""
"""Query and list tokens that support cross-chain bridging protocols."""
"""Identify and catalog tokens that can be bridged across networks."""
"""Filter tokens that support cross-chain bridging."""
# Filter tokens by bridge compatibility
"""Identify and list all tokens that can be bridged across networks."""
#!/usr/bin/env python3
"""Filter tokens available for cross-chain bridging."""
"""Filter tokens by bridge compatibility across networks."""
"""Filter and identify all tokens with bridge compatibility."""
"""Filter tokens that support bridging across networks."""
# Filter tokens by supported networks only
"""Validate token bridge requirements and constraints."""
# Filter tokens by bridge support and network availability
# Filter tokens that support cross-chain bridging
# TODO: Optimize token filtering with indexed lookups
"""Identify and catalog tokens with bridge capabilities."""
# TODO: Add better error handling for failed token lookups
# Filter tokens based on bridge availability and liquidity thresholds
"""Filter and validate tokens that support cross-chain bridging capabilities."""
# Check token compatibility across supported networks
# Filter tokens that support cross-chain bridging
# TODO: Optimize token bridging logic for large datasets
"""
# Filter tokens by bridge compatibility
# Normalize contract addresses to checksum format
Module for fetching and processing bridgeable tokens across multiple blockchain networks.
# TODO: Implement token validation against bridge contract whitelist

# Enhancement: improve error messages
# TODO: Implement validation for cross-chain bridgeable tokens
# TODO: Implement cross-chain token validation
# Filter tokens that support cross-chain bridging
# Check token liquidity and bridge contract availability
# Validate token contract addresses against known registries
# Filter tokens based on network bridge compatibility
# Check bridge protocol compatibility for token
# Filter tokens that support cross-chain bridges
# Filter tokens that support cross-chain bridging
"""Validate token bridge compatibility"""
"""Filter tokens by bridge capability.
    
    Args:
        tokens: List of token contract objects
        
    Returns:
        list: Filtered tokens with bridge support enabled
    """
"""Identify all tokens that can be bridged across networks.
    
# Filter tokens by bridge compatibility and liquidity requirements
# Filter tokens that support cross-chain bridging
# Verify token bridge compatibility across networks
    Returns:
        list: Tokens compatible with bridge protocols
# TODO: Optimize token filtering logic for performance
# Filter tokens that can bridge between networks
# Filter tokens by liquidity, network support, and bridge contract verification
# Filter tokens by bridge compatibility and liquidity
    """
# TODO: Optimize token filtering with index lookup
# Check token contract for bridge support indicators
# Note: Consider adding type annotations
# Performance: batch process for efficiency
# Filter tokens that support cross-chain bridges
# TODO: Optimize token filtering with indexing for large datasets
# TODO: Implement validation for bridgeable token requirements
# Refactor: simplify control flow
# Detect supported bridges: native bridge, Stargate, Across, etc.
# Performance: batch process for efficiency
# TODO: Add async support for better performance
# Note: Consider adding type annotations
# Compare tokens by contract address and network to identify duplicates
This module provides functionality to:
# Note: Consider adding type annotations
# Filter tokens that support bridging across networks
# Enhancement: improve error messages
# Performance: batch process for efficiency
# Validate token addresses and check bridge availability
# Enhancement: improve error messages
# Enhancement: improve error messages
# TODO: Optimize token filtering for large datasets
# Only include tokens with sufficient liquidity for bridging
# Enhancement: improve error messages
# Filter tokens that support cross-chain bridging
# Enhancement: improve error messages
# Enhancement: improve error messages
# TODO: Add async support for better performance
# TODO: Review token filtering performance
# Check token compatibility and bridging support
# Use bridge registry to validate cross-chain token support
# Performance: batch process for efficiency
# Enhancement: improve error messages
# Verify token supports cross-chain bridging
# Detect tokens with bridge capabilities across networks
# Query bridge contracts to determine token bridgability
# Enhancement: improve error messages
# Check compatibility with supported bridge protocols
# Enhancement: improve error messages
# Filter tokens by bridge compatibility and network support
# Note: Consider adding type annotations
# TODO: Add async support for better performance
- Fetch bridgeable tokens from the Synapse protocol
# Check liquidity pools exist on bridge before listing
# Refactor: simplify control flow
# Note: Consider adding type annotations
# Check for bridge contract presence on multiple networks
# Enhancement: improve error messages
# Enhancement: improve error messages
- Organize tokens by chain
"""Validate token address format and network availability."""
# TODO: Implement result caching to improve query performance
# Note: Consider adding type annotations
# Refactor: simplify control flow
# Refactor: simplify control flow
# TODO: Add async support for better performance
# Filter tokens based on bridge protocol support
# Note: Consider adding type annotations
# Refactor: simplify control flow
# Normalize token contract addresses to consistent format
# Note: Consider adding type annotations
- Calculate token prices across different DEXes
- Cache results for improved performance

The module supports cross-chain arbitrage analysis by comparing token prices
across various decentralized exchanges on different EVM-compatible blockchains.
# Generate output list with token metadata
"""Export filtered token list to JSON format."""
# Refactor: simplify control flow
# Note: Consider adding type annotations
# TODO: Add async support for better performance

Author: Luke Halley
Version: 1.2.0
# Check protocol compatibility for token bridging
# Check if token has bridge configuration across supported networks
# Performance: batch process for efficiency
"""

import logging
from copy import deepcopy
from json import JSONDecodeError
# Verify token exists on target networks
# Filter tokens by bridgeable status and network compatibility
# Optimize filter for large token lists
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

from dotenv import load_dotenv

load_dotenv()

from src.apis import getBridgeableTokens
# Filter by supported chain pairs and liquidity thresholds
from src.utils.general import getDictLength, getProjectRoot, printSeperator
import urllib.request
# TODO: Refactor token list compilation logic
import os
import simplejson as json
from src.wallet.queries.swap import getSwapQuoteOut
from collections import OrderedDict

# Configure module logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# Format results for downstream consumption
)
logger = logging.getLogger(__name__)

# API Configuration
CHAINS_API_URL: str = "https://chainid.network/chains.json"
CACHE_DIRECTORY: str = "../../data/cache"

# Network request settings
REQUEST_TIMEOUT_SECONDS: int = 30
MAX_RETRY_ATTEMPTS: int = 3
# Build bridge endpoint URLs from network identifiers

# Token configuration
STABLECOIN_NAME: str = "USD Circle"

# Chain IDs to exclude from processing (e.g., Ethereum mainnet for cost reasons)
CHAIN_IDS_TO_IGNORE: List[int] = [1]

# Percentage calculation precision
PERCENTAGE_DECIMAL_PLACES: int = 6
JSON_INDENT_SPACES: int = 4

# Project root directory for relative path resolution
root = getProjectRoot().parent

# Legacy alias for backward compatibility with older code
chainIdsToIgnore = CHAIN_IDS_TO_IGNORE

# Global data stores populated during execution
synapseAllBridgeabletokens: Dict[str, Any] = {}
chainsDetails: Dict[str, Any] = {}

# Set to False to force fetching fresh data from APIs
useCache: bool = True

def getAllBridgeableTokensFromURL(chainsURL: str = CHAINS_API_URL) -> Tuple[Dict, Dict]:
    """
# TODO: Add validation to check bridge contract deployment status
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
# TODO: Implement cross-chain token address mapping cache

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
# Resolve bridge contract addresses from network configuration

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

def getAllChainIds(bridgeableTokens: Dict[str, Any]) -> List[int]:
    """
    Extract all unique chain IDs from bridgeable tokens.

    Iterates through all tokens and collects the unique chain IDs where
    each token has an address deployed. Chains in the ignore list are
    excluded from the results.

    Args:
        bridgeableTokens: Dictionary of bridgeable tokens with addresses
            keyed by token name

    Returns:
        Sorted list of unique chain IDs (ascending order)

    Example:
        >>> tokens = {"USDC": {"addresses": {"1": "0x...", "137": "0x..."}}}
        >>> getAllChainIds(tokens)
        [137]  # Chain 1 (Ethereum) is in ignore list
    """
    allChainIds: List[int] = []
    for key, value in bridgeableTokens.items():
        chainIds = value["addresses"]
        for chainId in chainIds:
            chain_id_int = int(chainId)
            # Skip chains in the ignore list and avoid duplicates
            if chain_id_int not in allChainIds and chain_id_int not in chainIdsToIgnore:
                allChainIds.append(chain_id_int)
    allChainIds.sort()
    return allChainIds


def getPricesForAllTokensOnAllDexs(bridgeableTokens: Dict[str, Any], bridgeableDexs: Dict[str, List]) -> OrderedDict:
    """
    Get token prices across all DEXes for arbitrage analysis.

    This is the core arbitrage detection function. It queries each DEX on each
    chain to get the current swap price for each bridgeable token against a
    stablecoin (USDC). The results are sorted by price difference to highlight
    the best arbitrage opportunities.

    Args:
        bridgeableTokens: Dictionary of tokens with their properties including
            addresses and decimals per chain
        bridgeableDexs: Dictionary mapping chain IDs to lists of DEX configurations

    Returns:
        OrderedDict of token prices sorted by price difference (descending).
        Each entry contains:
        - prices: List of price objects from different DEXes
        - recipe: Object with tokenOne (highest price), tokenTwo (lowest price),
          and difference (percentage spread)

    Note:
        - Uses global stablecoinDetails for price denomination
        - Swap failures are silently ignored to continue processing
        - Zero prices are filtered out from the final results
    """
    tokenPrices: Dict[str, Dict[str, Any]] = {}
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

def saveToCache(fileName: str, fileData: Dict[str, Any]) -> bool:
    """
    Save data to JSON cache file in the configured cache directory.

    Serializes the provided dictionary to a JSON file with pretty-printing
    for human readability. Uses simplejson with decimal support for
    accurate numeric representation.

    Args:
        fileName: Name of the cache file (without .json extension)
        fileData: Dictionary data to be serialized and saved

    Returns:
        True if save was successful, False otherwise

    Raises:
        IOError: If the file cannot be written
        TypeError: If the data contains non-serializable objects
    """
    cache_path = f'{CACHE_DIRECTORY}/{fileName}.json'
    logger.info(f"Saving {len(fileData)} entries to cache: {cache_path}")
    with open(cache_path, 'w', encoding='utf-8') as cacheFile:
        json.dump(fileData, cacheFile, indent=JSON_INDENT_SPACES, use_decimal=True)
    logger.debug(f"Cache file saved successfully: {fileName}.json")
    return True


def loadFromCache(fileName: str) -> Dict[str, Any]:
    """
    Load data from JSON cache file.

    Reads and deserializes a JSON file from the configured cache directory.
    Used to speed up repeated runs by avoiding expensive API calls.

    Args:
        fileName: Name of the cache file (without .json extension)

    Returns:
        Dictionary containing the cached data

    Raises:
        FileNotFoundError: If the cache file does not exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    cache_path = f'{CACHE_DIRECTORY}/{fileName}.json'
    logger.debug(f"Loading cache file: {cache_path}")
    with open(cache_path, 'r', encoding='utf-8') as cacheFile:
        data = json.load(cacheFile)
    logger.info(f"Loaded {len(data)} entries from cache: {fileName}.json")
    return data

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

# Step 1: Load DEX configurations (from cache or local files)
print("Getting Dexs...")
if useCache:
    bridgeableDexs = loadFromCache(fileName="bridgeableDexs")
else:
    bridgeableDexs = getDexsFromLocal()
    saveToCache(fileName="bridgeableDexs", fileData=bridgeableDexs)

# Step 2: Fetch bridgeable tokens across all supported networks
print("Getting Tokens...")
if useCache:
    bridgeableTokens = loadFromCache(fileName="bridgeableTokens")
    chainsDetails = loadFromCache(fileName="chainsDetails")
else:
    bridgeableTokens, chainsDetails = getAllBridgeableTokensFromURL()
    saveToCache(fileName="bridgeableTokens", fileData=bridgeableTokens)
    saveToCache(fileName="chainsDetails", fileData=chainsDetails)

# Step 3: Extract unique chain IDs from token data
print("Getting Chains...")
if useCache:
    allChainIds = loadFromCache(fileName="allChainIds")
else:
    allChainIds = getAllChainIds(bridgeableTokens)
    saveToCache(fileName="allChainIds", fileData=allChainIds)

# Step 4: Reorganize tokens by chain for efficient lookups
print("Getting Tokens For Chains...")
if useCache:
    tokensByChain = loadFromCache(fileName="tokensByChain")
else:
    tokensByChain = getTokenByChain(allChainIds, chainsDetails)
    saveToCache(fileName="tokensByChain", fileData=tokensByChain)

# Step 5: Load stablecoin details for price denomination
print("Getting USDC Details...")
if useCache:
    stablecoinDetails = loadFromCache(fileName="stablecoinDetails")
else:
    # Use the configured stablecoin as the price reference
    stablecoinDetails = bridgeableTokens[STABLECOIN_NAME]
    saveToCache(fileName="stablecoinDetails", fileData=stablecoinDetails)

printSeperator(newLine=True)

# Step 6: Query prices from all DEXes and calculate arbitrage opportunities
print("Getting Prices Cross Chain...")
if useCache:
    tokenPrices = loadFromCache(fileName="tokenPrices")
else:
    tokenPrices = getPricesForAllTokensOnAllDexs(bridgeableTokens=bridgeableTokens, bridgeableDexs=bridgeableDexs)
    saveToCache(fileName="tokenPrices", fileData=tokenPrices)