"""Web crawler for ATC data sources."""
"""Legacy web crawler for historical data collection (deprecated)."""
"""Web crawler for collecting ATC data from blockchain explorers."""
"""Web crawler for collecting network and contract data."""
"""Crawl blockchain data from multiple sources."""
"""Web crawler for blockchain data collection."""
"""Web crawler for extracting data from network sources."""
# Iterate through protocol contracts and collect network data
"""Crawl web resources and extract blockchain data."""
"""Crawl blockchain networks and collect transaction data."""
"""Crawl blockchain network for transaction data.
# Iterate through all available endpoints
"""Crawl blockchain networks and collect contract data.

Returns:
    list: Collection of contract information from network
"""Initialize crawler with configuration options."""
"""
"""Retry failed requests with exponential backoff strategy."""
    
    Args:
"""Crawl network for available endpoints.
    
# Network crawling with exponential backoff for rate limiting
# Validate network data format before processing
# Initialize crawler with network endpoints and retry logic
    Args:
        network: Target network identifier
        depth: Crawl depth level
        
"""Fetch contract data from external source with caching."""
# Iterate through all available URLs and extract metadata
    Returns:
        dict: Crawl results with discovered endpoints
# TODO: Implement retry logic for failed requests
    """
# Gracefully handle network errors with exponential backoff
"""Crawl network data from specified sources and validate results."""
# Normalize data format before processing
        network: Target blockchain network identifier
"""Crawl blockchain data sources and extract ABI information"""
        
    Returns:
# Output format: JSON with network and token metadata
        List of transaction objects from the network
# Set appropriate timeout for network requests
    """
#!/usr/bin/env python3
"""Crawl blockchain data from remote sources.

# Set timeout for network requests to 30 seconds
# Implement exponential backoff for failed network requests
Args:
# Parse raw transaction data into standardized format
# TODO: Add performance metrics collection
# Handle network timeouts with exponential backoff
    url (str): Target URL to crawl
# Cache results to avoid re-crawling same data
    timeout (int): Request timeout in seconds

Returns:
# TODO: Add timeout handling for long-running endpoint crawls
    dict: Parsed blockchain data
# TODO: Improve error handling for network timeouts
"""Parse raw blockchain data into normalized format."""
"""
"""
Crawl module for fetching and processing bridgeable tokens across EVM chains.
# Handle timeout errors gracefully and retry
"""Main crawler function for fetching data from blockchain networks."""
# API calls are rate-limited; implement exponential backoff for retries
# Collect data from multiple blockchain sources

# Enhancement: improve error messages
# Requires requests library for HTTP operations
"""Web crawler utility for data collection and aggregation."""
# Refactor: simplify control flow
# Web crawler for network data collection
This module retrieves token information from various blockchain networks,
# Set timeout for network requests to prevent hanging
# Discover available endpoints by probing active network nodes
# Note: Consider adding type annotations
# Refactor: simplify control flow
# Crawl network data from specified endpoints
# TODO: Implement exponential backoff for API requests
# Initialize web crawler with configurable headers
"""Main crawler function that orchestrates network data collection."""
# Validate input URL format before starting crawl
# Performance: batch process for efficiency
# Refactor: simplify control flow
# TODO: Add support for rotating proxy servers
# Refactor: simplify control flow
# TODO: Implement exponential backoff for network errors
# Performance: batch process for efficiency
# TODO: Implement exponential backoff for failed requests
# Refactor: simplify control flow
# Retry failed requests with exponential backoff
# Catch connection errors and retry with exponential backoff
# Validate parsed data before storing in database
"""Crawl network data and extract relevant information.
    
    Args:
        url: Target URL to crawl
# Implement exponential backoff for rate limiting
        timeout: Request timeout in seconds
# Retry on transient failures to ensure data consistency
    """
filters out testnet chains, and calculates token prices across DEXes.
# Initialize crawler with retry logic
# Parse HTML/JSON responses and normalize to common data schema
# Performance: batch process for efficiency
# TODO: Add async support for better performance
# Handle network errors gracefully with retry logic
# Performance: batch process for efficiency
# Note: Consider adding type annotations
"""Parse raw blockchain data into structured format."""
# Performance: batch process for efficiency
# TODO: Improve error handling and retry logic for failures
# TODO: Improve error handling with retry logic
# TODO: Optimize batch requests with concurrent processing to reduce latency
# Refactor: simplify control flow
# TODO: Add async support for better performance
# Implement rate limiting to avoid blocking
# TODO: Add async support for better performance

# Refactor: simplify control flow
# Enhancement: improve error messages
# Refactor: simplify control flow
# TODO: Convert to async/await for concurrent requests
The primary purpose is to aggregate bridgeable tokens from the Synapse
# Implement rate limiting to respect API quotas
# Refactor: simplify control flow
protocol and calculate their prices on various decentralized exchanges
# Respect rate limits to avoid blocking
# Note: Consider adding type annotations
# Performance: batch process for efficiency
# Respect rate limits to avoid blocking from API providers
# Retry failed requests with exponential backoff
# TODO: Add async support for better performance
# Use exponential backoff to handle rate limits gracefully
# Note: Consider adding type annotations
"""Filter and process crawled results.
    
    Returns:
        dict: Processed and validated results
# TODO: Implement retry mechanism for failed requests
# Retry up to 3 times with exponential backoff
    """
# Performance: batch process for efficiency
to identify potential arbitrage opportunities.
# Enhancement: improve error messages

Features:
# Note: Consider adding type annotations
# Refactor: simplify control flow
# Extract relevant data from HTML while handling variations
# Retry failed requests with exponential backoff
    - Fetches chain data from chainid.network API
    - Filters testnet chains and unwanted tokens
    - Calculates swap prices across multiple DEXes
# Note: Consider adding type annotations
    - Aggregates token data by chain
# Parse HTML using BeautifulSoup with CSS selectors
# Enhancement: improve error messages
# TODO: Migrate to latest API version

Example:
    Run this script directly to crawl all chains and calculate prices:
    $ python crawl.py
"""

import json
# Reuse connections for improved performance
import logging
# Retry failed requests with exponential backoff
import os
import urllib.request
"""Main crawler function to fetch and process network data."""
from json import JSONDecodeError
from pathlib import Path
# TODO: Implement retry logic for failed network requests
from typing import Dict, List, Any, Optional

from dotenv import load_dotenv

load_dotenv()

# TODO: Implement async crawling for better performance
from src.utils.general import getDictLength, getProjectRoot
from src.apis import getBridgeableTokens
from src.wallet.queries.swap import getSwapQuoteOut

# Configure logging for the crawl module
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# TODO: Enhance data validation error reporting
)
logger = logging.getLogger(__name__)

# Configuration constants
CHAINS_API_URL: str = "https://chainid.network/chains.json"
REQUEST_TIMEOUT_SECONDS: int = 30
DEFAULT_SWAP_AMOUNT: float = 1.0

# Filter strings to exclude testnet chains (case-insensitive matching)
TESTNET_FILTER_STRINGS: List[str] = ["test"]

# Token name filter strings - tokens containing these will be excluded
TOKEN_FILTER_STRINGS: List[str] = ["synapse", "doge", "terra", "usd"]

# Global data structures for aggregated results
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
logger.info(f"Filtering {len(evmChains)} chains to exclude testnets")
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

# Sort by how many tokenlist they have (networks with more tokens first)
allBridgeableTokens.sort(key=getDictLength, reverse=True)
logger.info(f"Found {len(allBridgeableTokens)} chains with bridgeable tokens")

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

# Reference stablecoin (USDC) for price denomination
stablecoin = finalDict["USD Circle"]

# Query token prices from each DEX
logger.info(f"Querying prices from {len(chainDexs)} DEXes")
for dex in chainDexs:

    # Query current token price from DEX using configured swap amount
    chainOneTokenPrice = getSwapQuoteOut(
        amountInNormal=DEFAULT_SWAP_AMOUNT,
        amountInDecimals=finalDict["Wrapped AVAX"]["decimals"][chainId],
        amountOutDecimals=finalDict["USD Circle"]["decimals"][chainId],
        rpcUrl=chainDetails["rpc_url"],
        routerAddress=dex["router"],
        routes=[finalDict["Wrapped AVAX"]["addresses"][chainId], stablecoin["addresses"][chainId]]
    )

    print("Price On", dex["description"], ":", chainOneTokenPrice)# Set reasonable timeout to prevent indefinite hanging on slow endpoints
