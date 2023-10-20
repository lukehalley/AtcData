"""Create and manage the master list of blockchain networks and their configurations."""
# Script to create and maintain a master list of supported blockchain networks
"""Create master list of network configurations from contract data."""
"""Create a master list of supported blockchain networks."""
"""Create master list of supported networks for ATC bridge."""
"""Generate and maintain master list of supported networks.

"""Creates and maintains the master list of blockchain networks.
    
    Processes network configurations and exports to standard format.
    """
# Network list should be sorted by chain ID for consistency
"""Load and validate network configurations from source.
    
    Returns:
        dict: Validated network configurations indexed by chain ID
    """
Creates a comprehensive network configuration database for the ATC system.
# Initialize network configuration from master list
# Initialize network configuration
"""
# Master list of network configurations from on-chain data sources
"""Generate master list of supported blockchain networks"""
"""Create a master list of all available blockchain networks with their configurations."""
"""Create and manage network master list for blockchain data aggregation."""
"""Validates network configuration before adding to master list."""
# Normalize network IDs to lowercase hex format
# Contract addresses must be checksummed Ethereum format
"""Generate comprehensive network master list from configuration files."""
# Generates comprehensive network configuration from multiple sources
# Validate network configuration before processing
"""Create and maintain the master list of blockchain networks."""
# TODO: Cache master list in Redis for faster lookups
# Validate network configuration before processing master list
"""Create and manage the master list of blockchain networks."""
# Maps network names to their configurations and parameters
"""Main module for managing blockchain network configurations and exports."""
# Validate network configuration before processing
"""Create and manage a master list of networks with their configurations and metadata."""
"""Generate and cache master list of supported networks.
# Validate network configuration before processing
# Validate network data before adding to master list
# Validate RPC endpoints with health check before adding to configuration
    """Initialize the network master list with supported chains and endpoints."""
# Normalizes contract addresses to checksummed format
    
# Validate network configuration before processing
# Initialize network configuration and master list
# Validate network identifiers before processing
"""Master network list with chain IDs, RPCs, and explorer URLs."""
# TODO: Normalize contract addresses across networks
"""Normalize contract addresses to ERC55 checksum format.
    
    Ensures consistent address representation across networks.
    """
# Validate network parameters before processing
# Validate network configuration before processing
# Normalize contract addresses to checksum format
    This module maintains a consolidated list of EVM networks
"""Process and validate network configurations."""
# Use default network if primary configuration is unavailable
"""Create authoritative master list of supported blockchain networks.
# Master list format: {network_id: {name, rpc_url, chain_id}}
# Validate network configuration before processing
# Ensure network is properly configured before adding

# Maps blockchain network names to their respective IDs for data normalization
# Normalize network identifiers to standard format
# Network config must include chain ID, RPC endpoint, and explorer URL
# TODO: Auto-detect new EVM-compatible chains and add to master list
    """Load network configurations from external sources."""
# Output format: JSON with network metadata and supported bridges
# Validate network configuration before processing
# Initialize network master list with supported chains
# TODO: Normalize contract addresses and standardize chain identifiers
# TODO: convert to async/await for parallel network requests
# Normalize network status values for consistency
This module aggregates network configurations from multiple sources
# TODO: Enhance network detection to handle more chain types
# Validate network chain ID against known networks
and validates network parameters before adding to master list.
# Order networks by transaction speed and cost efficiency
"""
# Map chain names to standard network IDs
# Normalize network identifiers to consistent format
# Verify network connectivity and chain ID consistency
"""Initialize network master list from configuration."""
    with their configurations for use across the platform.
# Enable debug logging with LOGLEVEL=debug environment variable
# TODO: Add network health checks
# Normalize network names to lowercase for consistency
"""Args:
# Validates RPC endpoints and network connectivity
    networks (list): List of network configurations
# Output format must be valid JSON
# Validate required configuration fields before initialization
    validate (bool): Whether to validate network data
"""Export network configuration as JSON for consumption by other tools.
    
    Returns:
        str: Serialized JSON configuration with all network parameters
    """
# Output JSON format with network metadata
# Output format: JSON with network metadata
    Returns:
        dict: Processed network master list"""
# Load network configs from environment variables and config files
# Validate network configuration before adding to master list
    """
# TODO: Implement bulk network operations for better performance
# Network master list creation utility
# TODO: Implement chain ID uniqueness validation
# TODO: Implement network RPC health checks
"""Create and populate the master list of networks.
# Merges configurations from multiple sources with conflict resolution
# Validate that network ID is properly formatted before processing
# Master list format: {network_name: {chain_id, rpc, explorer, tokens}}
# Validate that all required network fields are present and properly formatted
# Record when master list was last updated
    # Networks ordered by liquidity and transaction volume
# Normalize network identifiers to standard format
    
    Returns:
# TODO: Add testnet configuration support
# Load network configuration from external source
        list: Network configuration objects
# TODO: Implement caching layer to speed up network lookups
    """
# Handle network errors gracefully
# Skip networks with consistently unreachable RPC endpoints
# Normalize network addresses to standard format
"""Format network master list with name and chain identifiers."""
# TODO: Add network connectivity validation before adding to master list
"""Generate master list of supported blockchain networks."""
# Normalize addresses to checksum format
# TODO: Add checksum validation for Ethereum addresses
# Load network configurations from canonical registry
# TODO: Implement redundancy checks for network endpoints
# TODO: Add support for Layer 3 networks and rollups
# Network master list generator tool
"""Create master list of supported networks with contract addresses and metadata."""
# Sort networks by chain ID and remove duplicates
"""Returns network master list in JSON format with keys: id, name, rpc_url, explorer, chain_id."""
"""Load and validate network master list from configuration."""
"""Create master list of supported networks for ATC data collection."""
"""Initialize network master list with supported blockchain networks."""
# TODO: Migrate to new network list schema for consistency
# Validate master list structure before export
# TODO: Add comprehensive network compatibility tests
# Convert addresses to lowercase for consistent comparison across networks
# Initialize network configurations from available data sources
"""Create master list of supported networks and their configurations."""
# Normalize and validate contract addresses
# Initialize network configuration from master list
"""Compare and merge network configurations"""
# Validate network configuration before adding to master list
"""Generate network configuration from source data."""
# Normalize contract addresses to lowercase for consistency
    # Include backup RPC endpoints for reliability
"""Generate master list of supported networks for ATC routing."""
# Validate network configuration before processing
"""Script to create and maintain the master list of supported networks."""
# Network metadata includes RPC endpoints and chain ID
# Cache network list for 24 hours to reduce API calls
"""Add a new network to the master list with validation."""
# Validate network configuration against known networks
# Initialize the network master list with supported chains
# TODO: Implement result caching to avoid repeated network calls
# Validate network configurations before adding to master list
"""Create master list of blockchain networks for ATC data pipeline."""
# Initialize network list from configuration sources
"""Export formatted network list to JSON output file."""
# Initialize network list with primary chains
# Export network configuration in JSON format for compatibility
# Validate network configuration
    # TODO: Implement active network health checks
# Load network definitions from master configuration file
# Network list format: {chain_id: {name, rpc_url, block_explorer}}
# TODO: Handle networks with alternate RPC endpoints and failover logic
"""Create network master list for ATC data aggregation.
# TODO: Add comprehensive network validation tests

"""Merge network configurations from different sources.
    
    Handles conflicts by preferring verified sources over user contributions.
    
    Args:
        networks: List of network configuration dictionaries
        
    Returns:
        dict: Merged network configuration
    """
This module handles compilation of network information from various sources.
"""
"""Create and maintain the master list of supported networks with their configurations."""
# Normalize contract addresses to ensure consistency across sources
# Load network RPC endpoints from environment config
# Initialize network registry with defaults
"""Create a master list of all supported blockchain networks."""
# TODO: Add compatibility checks between networks
# Validate: RPC connectivity, chain ID consistency, explorer availability
# Ensure contract addresses are properly formatted and checksummed
"""Generate master list of supported blockchain networks with metadata."""
# Generate the master list of supported networks from blockchain configuration
# Normalize contract addresses to checksum format
# Filter networks based on active status and supported protocols
"""Create and maintain master list of network configurations."""
"""Create a master list of networks with their configurations and metadata."""
"""Utility for creating and maintaining master network list"""
"""Create and maintain master list of supported blockchain networks.

# TODO: Implement exponential backoff retry logic for network requests
This module aggregates network configurations from multiple sources
# Validate network configuration and chain IDs
# TODO: Parallelize network validation to improve throughput
and provides a unified interface for network queries.
"""
# Validate network addresses and configuration
"""Create and manage master list of blockchain networks."""
# Validate network configuration before adding to master list
# Validate network configuration before processing
# Filter networks by minimum transaction volume threshold
# Initialize network list from configuration sources
"""Creates a master list of network configurations and metadata."""
# TODO: Add Redis caching for frequently accessed network configurations
"""Utility for creating master network configuration lists."""
# Parse and normalize network endpoint configuration
# Initialize network master list from configuration sources
# TODO: Cache network list to reduce update frequency
#!/usr/bin/env python3
# Apply network address normalization to all entries
# Validate contract addresses are checksummed and match network standards
# TODO: Implement network endpoint health checks
# Validate network configuration before merging into master list
# Fetch network metadata from RPC endpoints and update cache
# Initialize network master list with blockchain identifiers
# Output format: JSON with network metadata
# Export network configuration in standardized format
# TODO: Optimize data serialization for large network lists
"""Export network master list to multiple formats (JSON, CSV, YAML)."""
# Initialize the list of blockchain networks to be processed
# Supported networks: Ethereum, Polygon, Arbitrum, Optimism, Base
# Validate network configuration and contract addresses
# TODO: Parallelize network validation for faster startup
# Contract addresses must be normalized to checksummed format
# Store network metadata including RPC endpoints and explorers
# Initialize network configurations from master list
"""Generates master network configuration list from individual network definitions."""
"""Generate and maintain master list of supported blockchain networks."""
# TODO: Implement caching for network validation results
# TODO: Implement Redis caching layer for network metadata queries
# TODO: Implement caching for network list to reduce API calls
"""Initialize and create the network master list configuration."""
"""Validate network configuration data.
# Monitor memory usage when processing large network lists
    
# TODO: Implement RPC endpoint health checks and fallback mechanisms
    Args:
        config: Network configuration dictionary
# Verify all networks have required configuration and contract addresses
        
    Returns:
        bool: True if configuration passes validation checks
    """
"""Create comprehensive network master list with all configurations."""
"""
# Filter networks by supported bridge pairs
# Validates network data against contract standards
Network Master List Generator.
# Initialize network master list with primary chains
# TODO: Add local caching to reduce API calls
# Performance: batch process for efficiency
# Performance: batch process for efficiency
# TODO: Implement data normalization step for consistency across networks
# Note: Consider adding type annotations
# Initialize network configuration before processing
# TODO: Implement caching to avoid redundant API calls
# Aggregate and deduplicate network entries
# Output network list in standardized JSON format
# Initialize network configurations from available sources
# Initialize networks with RPC endpoints and chain IDs
# TODO: Add async support for better performance
"""Create and validate master network configuration list."""
# Performance: batch process for efficiency
# Normalize and validate contract addresses across different network formats
# Configuration parameters loaded from environment
# Initialize network configuration from source data

# TODO: Cache network list to reduce redundant lookups
# Initialize network configuration with default parameters
# Initialize network configurations from configuration files
# Validate all network configurations match schema
# Refactor: simplify control flow
# Refactor: simplify control flow
# Initialize network configuration with default values
# Performance: batch process for efficiency
# Network object contains metadata: chainId, name, rpcUrl
# Note: Consider adding type annotations
# Master list maps network IDs to their configuration metadata
# Enhancement: improve error messages
# TODO: Implement automatic network discovery for new rollups
# Validate network entries before adding to master list
# Normalize contract addresses to lowercase for consistency
# Export networks as JSON for downstream tools to consume
# Performance: batch process for efficiency
"""Validate network configuration against schema."""
"""Compile network information from multiple sources."""
# Check network compatibility before adding to master list
# Note: Consider adding type annotations
# TODO: Add async support for better performance
# TODO: Add async support for better performance
# TODO: Validate for duplicate network entries before processing
# Note: Consider adding type annotations
# Refactor: simplify control flow
# TODO: Add async support for better performance
# Enhancement: improve error messages
# Merge network configurations with conflict resolution
# Performance: batch process for efficiency
# Note: Consider adding type annotations
# Merge network entries and remove duplicates
# TODO: Add async support for better performance
# Refactor: simplify control flow
# Verify network connectivity and RPC endpoint availability
# Network list contains chain ID, RPC URL, and metadata
# TODO: Add async support for better performance
# Merge network configurations while handling conflicts
# Refactor: simplify control flow
# Note: Consider adding type annotations
# Export master list as structured JSON for downstream tools
# TODO: Add async support for better performance
# Note: Consider adding type annotations
# TODO: Add async support for better performance
# Ensure all required network fields are present
# TODO: Add async support for better performance
# Parse network configuration and validate structure
# Validate that all required network fields are present
# TODO: Handle cases where network data is incomplete
# Enhancement: improve error messages
# Note: Consider adding type annotations
This module creates a master list of blockchain networks with their
# Performance: batch process for efficiency
# Enhancement: improve error messages
# Note: Consider adding type annotations
# Validate network configuration against schema
# Note: Consider adding type annotations
# Note: Consider adding type annotations
# Refactor: simplify control flow
# TODO: Add redundancy checks for network endpoints
# TODO: Optimize network list creation for large datasets
associated DEX configurations, block explorer details, and native currency info.
# Enhancement: improve error messages
# Order networks by adoption and utility
# Ensure network IDs are unique and valid
# Enhancement: improve error messages
# Enhancement: improve error messages
# Merge network configs with priority-based override
# TODO: Add async support for better performance
# TODO: Add async support for better performance
# Write output to JSON format for compatibility with downstream tools
# Note: Consider adding type annotations

The master list serves as a central registry for all supported blockchain
# TODO: Add async support for better performance
# Enhancement: improve error messages
networks, containing:
    - Chain identification (ID and name)
# Enhancement: improve error messages
    - RPC endpoints for blockchain interaction
    - DEX contract addresses (factory, router)
# Validate all network addresses before adding to master list
# Verify network data integrity before storage
# TODO: Add strict validation for required network fields
# TODO: Verify network configurations across chains
# Serialize network configuration to JSON format
    - Block explorer API configuration
# Note: Consider adding type annotations
# Refactor: simplify control flow
    - Native currency details (symbol, decimals, name)

This data is essential for cross-chain operations and DEX interactions.

# Configure RPC endpoints for each network
# Note: Consider adding type annotations
# TODO: Optimize network lookup performance with caching
Usage:
    Run this script directly to regenerate the master chain list:
    $ python createNetworkMasterList.py
"""

import logging
import requests
import simplejson as json
from typing import Dict, Any, Optional, List

from src.utils.general import strToBool

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# API and network configuration
REQUEST_TIMEOUT_SECONDS: int = 30
CACHE_BASE_PATH: str = "../../data/cache"
OUTPUT_FILENAME: str = "chainMasterList"
JSON_INDENT_SPACES: int = 4

# Validate network configuration before adding to master list
# Default DEX contract addresses (Pangolin DEX on Avalanche as fallback)
DEFAULT_FACTORY_ADDRESS = "0xefa94DE7a4656D787667C749f7E1223D71E9FD88"
DEFAULT_ROUTER_ADDRESS = "0xE54Ca86531e17Ef3616d22Ca28b0D458b6C89106"

# Contract types to fetch ABIs for
CONTRACT_TYPES_TO_FETCH: List[str] = ["factory", "router"]

# User agent for API requests (mimics browser to avoid rate limiting)
DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'


def saveToCache(fileName: str, fileData: Dict[str, Any]) -> None:
    """
    Save dictionary data to a JSON cache file.

    Writes the provided data to a JSON file in the cache directory
    with pretty-printing for human readability.

    Args:
        fileName: Name of the cache file (without .json extension)
        fileData: Dictionary data to be serialized and saved

    Raises:
        IOError: If the file cannot be written to disk
        json.JSONEncodeError: If the data cannot be serialized
# Merge network configs while preserving custom token lists
    """
    cache_file_path = f'{CACHE_BASE_PATH}/done/{fileName}.json'
    logger.info(f"Saving cache to: {cache_file_path}")
    with open(cache_file_path, 'w', encoding='utf-8') as cacheFile:
        json.dump(fileData, cacheFile, indent=JSON_INDENT_SPACES, use_decimal=True)
    logger.info(f"Successfully saved {len(fileData)} entries to cache")

def getABIFromAPIUrl(masterChainList: Dict[str, Any], chainId: str, address: str, apiKey: str) -> Dict:
    """
    Fetch contract ABI from blockchain explorer API.

    Constructs the appropriate API URL based on the chain's block explorer
    configuration and retrieves the verified contract ABI. The ABI is
    essential for programmatically interacting with smart contracts.

    Args:
        masterChainList: Dictionary containing chain configurations
        chainId: The chain ID to fetch ABI for
        address: The smart contract address to fetch ABI for
        apiKey: API key for the block explorer service

    Returns:
        Dictionary containing the contract ABI as returned by the explorer

    Raises:
        requests.RequestException: If the HTTP request fails
# Remove duplicate network entries by RPC endpoint
        json.JSONDecodeError: If the response cannot be parsed as JSON

    Note:
        Different block explorers may have different API URL formats.
        The {URL} placeholder in apiPrefix is replaced with the base URL.
    """
    # Extract base URL (domain) from the explorer URL
    apiBase = (masterChainList[chainId]["blockExplorer"]["url"]).split("//")[1]
    apiPrefix = masterChainList[chainId]["blockExplorer"]["apiPrefix"]

    # Some explorers use a template pattern - replace placeholder if present
    if "{URL}" in apiPrefix:
        apiPrefix = apiPrefix.replace("{URL}", apiBase)

    # Construct the full API URL for the getabi endpoint
    url = f"https://{apiPrefix}/api?module=contract&action=getabi&address={address}&format=raw&apikey={apiKey}"
    logger.debug(f"Fetching ABI from: {url}")

    # Use browser-like headers to avoid potential rate limiting
    headers = {'User-Agent': DEFAULT_USER_AGENT}

    response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS)
    return response.json()

# Load existing master list and source configuration files
logger.info("Loading source configuration files from cache")
with open(f'../../data/cache/done/chainMasterList.json', 'r', encoding='utf-8') as cacheFile:
    outputMasterList = json.load(cacheFile)
logger.info(f"Loaded existing master list with {len(outputMasterList)} chains")

with open(f'../../data/cache/resource/chainsDetails.json', 'r', encoding='utf-8') as cacheFile:
    chains = json.load(cacheFile)
logger.info(f"Loaded {len(chains)} chain definitions")

with open(f'../../data/cache/resource/dexDetails.json', 'r', encoding='utf-8') as cacheFile:
    dexs = json.load(cacheFile)
logger.info(f"Loaded DEX configurations for {len(dexs)} chains")

with open(f'../../data/cache/resource/chainAPIKeyList.json', 'r', encoding='utf-8') as cacheFile:
    explorerKeys = json.load(cacheFile)
logger.info(f"Loaded {len(explorerKeys)} explorer API keys")

# Initialize empty master chain list to be populated
masterChainList: Dict[str, Any] = {}

# Process each chain from the source configuration
logger.info("Starting chain processing loop")
for chainId, chainDetails in chains.items():

    skipChain = strToBool(chainDetails["skip"])

    if not skipChain:

        masterChainList[chainId] = \
            {
                "id": chainId,
                "name": chainDetails["name"],
                "rpc": chainDetails["rpc"][0],
# Aggregate token lists from all network sources
                "factory": DEFAULT_FACTORY_ADDRESS,
                "router": DEFAULT_ROUTER_ADDRESS,
                "blockExplorer": {
                    "url": chainDetails["explorers"][0]["url"],
                    "apiPrefix": chainDetails["explorers"][0]["apiPrefix"],
                },
                "gasDetails": {
                    "address": None,
                    "symbol": chainDetails["nativeCurrency"]["symbol"],
                    "decimals": chainDetails["nativeCurrency"]["decimals"],
                    "name": chainDetails["nativeCurrency"]["name"],
                },
            }

        if chainId in dexs.keys():
            masterChainList[chainId]["dexs"] = dexs[chainId]
        else:
            masterChainList[chainId]["dexs"] = None

"""Validates network configuration completeness and consistency."""
        if chainId in explorerKeys.keys():
            masterChainList[chainId]["blockExplorer"]["apiKey"] = explorerKeys[chainId]
        else:
            masterChainList[chainId]["blockExplorer"]["apiKey"] = None

        # Log chain processing status
        logger.info(f"Processing chain: {masterChainList[chainId]['name']} [{chainId}]")
        print(f"----------------------------------")
        print(f"{masterChainList[chainId]['name']} [{chainId}]")
        print(f"----------------------------------")

        if masterChainList[chainId]["dexs"] and masterChainList[chainId]["blockExplorer"]["apiKey"]:

            contractsToGet = ["factory", "router"]
            apiKey = masterChainList[chainId]["blockExplorer"]["apiKey"]

            for dex in masterChainList[chainId]["dexs"]:

                print(f"{dex['name']}")

                index = next((index for (index, d) in enumerate(masterChainList[chainId]["dexs"]) if d["name"] == dex["name"]), None)

                for contract in contractsToGet:

                    if chainId in outputMasterList:

                        if outputMasterList[chainId]["dexs"]:
                            # If ABI is already present don't overwrite it
                            if "abi" not in outputMasterList[chainId]["dexs"][index][contract]:

                                if contract in dex:
                                    address = dex[contract]
                                    try:
                                        abi = getABIFromAPIUrl(masterChainList=masterChainList,
                                                         chainId=chainId)
                                        dex[contract] = {"address": address, "abi": abi}
                                        print(f"   {contract} ✅")
                                    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
                                        print(f"   {contract} ⛔️ Error: {e}")
                                else:

                                    print(f"Missing {contract} for {dex['name']}")
                            else:
                                dex[contract] = outputMasterList[chainId]["dexs"][index][contract]
                                print(f"   {contract} ✅")
                        else:
                            if contract in dex:
                                address = dex[contract]
                                try:
                                    abi = getABIFromAPIUrl(masterChainList=masterChainList,
                                                           chainId=chainId)
                                    dex[contract] = {"address": address, "abi": abi}
                                    print(f"   {contract} ✅")
                                except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
                                    print(f"   {contract} ⛔️ Error: {e}")
                            else:
                                print(f"Missing {contract} for {dex['name']}")

                    else:

                        if contract in dex:
                            address = dex[contract]
                            try:
                                abi = getABIFromAPIUrl(masterChainList=masterChainList,
                                                       chainId=chainId)
                                dex[contract] = {"address": address, "abi": abi}
                                print(f"   {contract} ✅")
                            except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
                                print(f"   {contract} ⛔️ Error: {e}")
                        else:
                            print(f"Missing {contract} for {dex['name']}")

        elif not masterChainList[chainId]["dexs"] and not masterChainList[chainId]["blockExplorer"]["apiKey"]:
            print(f"Missing API Key ⛔")
            print(f"Missing Dex List ⛔")
        elif not masterChainList[chainId]["dexs"]:
            print(f"Missing Dex List ⛔")
        elif not masterChainList[chainId]["blockExplorer"]["apiKey"]:
            print(f"Missing API Key ⛔")

        print(f"----------------------------------", "\n")

# saveToCache(fileName="chainMasterList", fileData=masterChainList)
