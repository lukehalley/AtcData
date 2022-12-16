SELECT
  pairs.pair_id,
  pairs.name,
  pairs.network_id,
  pairs.dex_id,
  pairs.primary_token_id,
  pairs.secondary_token_id
FROM
  (
    pairs
    JOIN (
      SELECT
        GROUP_CONCAT(DISTINCT pairs_matches.pair_id) AS idsgroup,
        pairs_matches.pair_id,
        pairs_matches.name,
        pairs_matches.network_id,
        pairs_matches.dex_id,
        pairs_matches.primary_token_id,
        pairs_matches.secondary_token_id
      FROM
        pairs AS pairs_matches
        INNER JOIN (
          SELECT
            pairs_max_liquidity.pair_id,
            pairs_max_liquidity.name,
            pairs_max_liquidity.network_id,
            pairs_max_liquidity.dex_id,
            pairs_max_liquidity.primary_token_id,
            pairs_max_liquidity.secondary_token_id,
            MAX(pair_market_data_max_liquidity.liquidity) AS pair_liquidity
          FROM
            pairs AS pairs_max_liquidity
            INNER JOIN pair_market_data AS pair_market_data_max_liquidity ON pairs_max_liquidity.pair_id = pair_market_data_max_liquidity.pair_id
          GROUP BY
            pairs_max_liquidity.primary_token_id,
            pairs_max_liquidity.secondary_token_id,
            pairs_max_liquidity.dex_id,
            pairs_max_liquidity.network_id
          ORDER BY
            pairs_max_liquidity.primary_token_id,
            pairs_max_liquidity.secondary_token_id,
            pairs_max_liquidity.dex_id,
            pairs_max_liquidity.network_id
        ) AS pairs_join_liquidity ON pairs_matches.pair_id = pairs_join_liquidity.pair_id
        AND pairs_matches.primary_token_id = pairs_join_liquidity.primary_token_id
        AND pairs_matches.secondary_token_id = pairs_join_liquidity.secondary_token_id
        AND pairs_matches.dex_id = pairs_join_liquidity.dex_id
        AND pairs_matches.network_id = pairs_join_liquidity.network_id
      GROUP BY
        pairs_matches.primary_token_id,
        pairs_matches.secondary_token_id,
        pairs_matches.network_id
      HAVING
        COUNT(*) > 1
      ORDER BY
        pairs_matches.primary_token_id,
        pairs_matches.secondary_token_id,
        pairs_matches.network_id
    ) AS pairs_multidex ON FIND_IN_SET(pairs.pair_id, pairs_multidex.idsgroup)
  )
ORDER BY
  pairs.primary_token_id,
  pairs.secondary_token_id,
  pairs.dex_id,
  pairs.network_id