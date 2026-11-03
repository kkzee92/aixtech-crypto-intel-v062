# Asset-class strategies (v0.62 research)

Paper-only multi-factor adaptive rules. Not investment advice.

## Major (BTC/ETH)

- Adaptive EMA/ATR/Supertrend/Ichimoku/BB/Keltner/VWAP/MACD/Heikin-Ashi/SAR/Donchian crossover with GARCH/EWMA/realized/term-structure/vol-of-vol forecast scaling.
- Fib/Elliott/options skew/gamma/vanna confirmation.
- On-chain: funding, basis, OI, order-flow, liquidity, MVRV, SOPR, reserve, NVTS, Puell, CDD, supply distribution.
- Correlation/beta/factor/covariance-adjusted outside stress. Risk cap 8%.

## Large-cap alt

- Volume-profile/POC/VAH/VAL breakout + VWAP + MACD + multi-TF + relative strength z-score.
- Correlation/beta/factor/covariance filter + regime cluster + volume delta + netflow + OI + order-flow + Fib + DEX LP + CCI + residual + hierarchical.
- Risk cap 4%.

## Stablecoin

- Adaptive peg deviation (15-50 bps) with volume confirmation + netflow + liquidity depth + SOPR + residual + CDD + dormancy.
- Risk cap 0%.

## DeFi

- Calm multi-scale + low anomaly + Supertrend + ADX + on-chain activity/smart-money + isolation + risk-parity + CVaR + LP depth/IL/fee/concentrated + Williams %R + residual + HODL + supply.
- Risk cap 2%.

## Meme

- Qualified burst + StochRSI + consistency + hard horizon + volume-flow decay + anomaly filter + residual + liq heat + order-flow + social synthetic + Fib + CCI + beta + narrative + attention.
- Risk cap 0.5%.

## L2

- Relative strength + MACD vs benchmark + adaptive MTF + correlation confirmation + cluster + vol forecast + transition + Elliott proxy + residual + factor + hierarchical.
- Risk cap 3%.

## RWA

- Slow multi-scale + gap/anomaly halt + volume filter + isolation + forecast + CVaR + realized-cap + NVTS + residual + age-weighted + dormancy.
- Risk cap 2%.

## Perpetual

- Negative funding carry + contained drift + low anomaly + funding flip alert + correlation + residual + OI + order-flow + gamma/vanna/charm/vanna-volga + reserve change + basis + basis momentum + carry.
- Risk cap 2%.

## AI-token

- Hybrid burst + activity proxy + divergence + low isolation; strict horizon + smart-money + OI + transition + options vanna + social + residual + narrative + factor + attention.
- Risk cap 1%.

All classes apply multi-gate risk (confidence floor, anomaly, isolation, drawdown, kill switch, vol scaling). Synthetic data only.
