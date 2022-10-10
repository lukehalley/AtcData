SELECT
  pair_results.pair_id,
  pair_results.name AS pair_name,
  primary_tokens.symbol AS primary_token_symbol,
  secondary_tokens.symbol AS secondary_token_symbol,
  networks.name AS network_name,
  dexs.name AS dex_name,
  networks.chain_rpc AS network_rpc,
  networks.explorer_tx_url AS network_explorer,
  dexs.factory AS dex_factory_address,
  dexs.factory_s3_path AS dex_factory_abi,
  dexs.router AS dex_router_address,
  dexs.router_s3_path AS dex_router_abi,
  pair_results.address as pair_address
FROM
  pairs AS pair_results
  JOIN (
    SELECT
      pairs.network_id,
      pairs.primary_token_id,
      pairs.secondary_token_id
    FROM
      pairs
    GROUP BY
      network_id,
      primary_token_id,
      secondary_token_id
    HAVING
      COUNT(*) > 1
    ORDER BY
      network_id,
      primary_token_id,
      secondary_token_id,
      COUNT(*) DESC
  ) AS matching_pairs ON pair_results.network_id = matching_pairs.network_id
  AND pair_results.primary_token_id = matching_pairs.primary_token_id
  AND pair_results.secondary_token_id = matching_pairs.secondary_token_id
  JOIN networks ON pair_results.network_id = networks.network_id
  JOIN dexs ON pair_results.dex_id = dexs.dex_id
  JOIN tokens AS primary_tokens ON pair_results.primary_token_id = primary_tokens.token_id
  JOIN tokens AS secondary_tokens ON pair_results.secondary_token_id = secondary_tokens.token_id 
  JOIN pair_market_data ON pair_results.pair_id = pair_market_data.pair_id
WHERE
  dexs.factory IS NOT NULL
  AND dexs.factory_s3_path IS NOT NULL
  AND dexs.router IS NOT NULL
  AND dexs.router_s3_path IS NOT NULL
  AND primary_tokens.address IS NOT NULL
  AND secondary_tokens.address IS NOT NULL