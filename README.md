# demo-py-portfoliorisk

## Finding Risk in Financial Portfolios using Python

This small data-pipeline uses Yahoo Finance and Numpy to collect live price data and calculate a rolling **Value at Risk (VaR)**. It provides insights on the potential loss in value of a portfolio over a defined period for a given confidence interval.

## What is Value at Risk (VaR)?

What we're looking to do here is quantify exposure over a specific time horizon. To do that we need a risk metric that tells us the maximum expected loss for a portfolio of assets over a time period with a specific confidence level. 

The variance-covariance method: **Parametric Value at Risk (VaR)**. 

The formula for daily VaR at a 95% confidence level is:

$$\text{VaR}_{95\\%} = \text{Portfolio Value} \times (1.645\sigma_p - \mu_p)$$

*Where $\mu_p$ is the expected return and $\sigma_p$ is the standard deviation.*

For reference, other methods are Monte Carlo VaR and Historic VaR.

## Demo Output

Below is a sample output of the demo which simulates a $100,000 investment in Nvidia stock (NVDA) for the last month:

```log
--- Starting Pipeline for NVDA ---
Process Complete at 2026-06-21 15:47:08.026475
Current Value at Risk (95%): $4676.71
```

A layman's reading of the above output is that if you invested $100,000 in Nvidia stock, there is a 5% chance that you could lose more than $4676.71 over the next month.

## Reality Check 

Parametric VaR is a simplified model that assumes normal distribution of returns and does not account for market shocks, liquidity issues, or other real-world factors. It relies on historical data and assumptions that may not hold true in the future. In reality, stocks like NVDA are notorious for "fat tails" (unexpected price jumps or drops). In a real market crash, this formula will drastically underestimate your actual risk—which is exactly why people pivot to the Historic or Monte Carlo methods.

## ⚠️ Disclaimer

**This is a financial analysis demo for educational purposes only. I am not a financial advisor, and this code should not be used as the basis for making investment decisions. The contents of this repository is not financial advice. Always consult with a financial advisor before making investment decisions.**

