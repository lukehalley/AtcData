SELECT
  networks.name AS network_name,
  dexs.name AS dex_name,
  pairs.name AS pair_name,
  primary_tokens.symbol AS primary_token_symbol,
  primary_tokens.address AS primary_token_address,
  secondary_tokens.symbol AS secondary_token_symbol,
  secondary_tokens.address AS secondary_token_address,
  dexs.factory AS dex_factory_address,
  dexs.factory_s3_path AS dex_factory_abi,
  dexs.router AS dex_router_address,
  dexs.router_s3_path AS dex_router_abi,
  networks.chain_rpc AS network_rpc,
  networks.explorer_tx_url AS network_explorer,
  pairs.pair_id,
  primary_tokens.token_id,
  secondary_tokens.token_id,
  pairs.address as pair_address
FROM
  pairs
  INNER JOIN pair_market_data ON pairs.pair_id = pair_market_data.pair_id
  INNER JOIN networks ON pairs.network_id = networks.network_id
  INNER JOIN dexs ON pairs.network_id = dexs.network_id
  INNER JOIN tokens AS primary_tokens ON pairs.primary_token_id = primary_tokens.token_id
  INNER JOIN tokens AS secondary_tokens ON pairs.secondary_token_id = secondary_tokens.token_id
WHERE
  primary_tokens.address IS NOT NULL
  AND secondary_tokens.address IS NOT NULL
  AND dexs.factory IS NOT NULL
  AND dexs.factory_s3_path IS NOT NULL
  AND dexs.router IS NOT NULL
  AND dexs.router_s3_path IS NOT NULL
  AND pairs.pair_id IN (
    SELECT
      join_pairs.pair_id
    FROM
      pairs AS join_pairs
    GROUP BY
      join_pairs.network_id,
      join_pairs.primary_token_id,
      join_pairs.secondary_token_id
    HAVING
      COUNT(*) > 1
  )
  AND pairs.pair_id IN (
    SELECT
      p.pair_id
    FROM
      pairs p
      INNER JOIN pair_market_data pm ON pm.pair_id = p.pair_id
    WHERE
      pm.liquidity = (
        SELECT
          MAX(liquidity)
        FROM
          pair_market_data
        WHERE
          pair_id = p.pair_id
      )
  );