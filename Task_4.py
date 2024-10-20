import pandas as pd
import numpy as np
from sklearn.utils import Bunch
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("/data/Loan_Data.csv")

def create_buckets(fico_scores, num_buckets):
    """
    Creates optimal bucket boundaries for FICO scores using dynamic programming.
    :param fico_scores: Array of FICO scores.
    :param num_buckets: Number of buckets to create.
    :return: List of unique bucket boundaries.
    """
    # Sort the FICO scores
    sorted_scores = np.sort(fico_scores)
    n = len(sorted_scores)

    # Initialize dynamic programming table for MSE minimization
    dp = np.zeros((num_buckets, n))
    boundaries = np.zeros((num_buckets, n), dtype=int)

    # Fill the DP table by incrementally building buckets
    for b in range(num_buckets):
        for i in range(n):
            if b == 0:
                # Initialize the first bucket with cumulative MSE
                dp[b, i] = np.mean((sorted_scores[:i + 1] - np.mean(sorted_scores[:i + 1])) ** 2)
                boundaries[b, i] = 0
            else:
                min_mse = float('inf')
                for j in range(i):
                    mse = dp[b - 1, j] + np.mean((sorted_scores[j + 1:i + 1] - np.mean(sorted_scores[j + 1:i + 1])) ** 2)
                    if mse < min_mse:
                        min_mse = mse
                        boundaries[b, i] = j
                dp[b, i] = min_mse

    # Backtrack to find optimal boundaries
    bucket_boundaries = []
    idx = n - 1
    for b in range(num_buckets - 1, -1, -1):
        bucket_boundaries.append(sorted_scores[boundaries[b, idx]])
        idx = boundaries[b, idx]

    # Ensure unique boundaries by adding a small epsilon if needed
    unique_boundaries = np.unique(bucket_boundaries)
    if len(unique_boundaries) < len(bucket_boundaries):
        unique_boundaries = np.linspace(min(fico_scores), max(fico_scores), num_buckets + 1)

    return list(unique_boundaries)

def calculate_pd_buckets(fico_scores, defaults, bucket_boundaries):
    """
    Calculate the Probability of Default (PD) for each bucket.
    :param fico_scores: Array of FICO scores.
    :param defaults: Array indicating default status (1 = default, 0 = no default).
    :param bucket_boundaries: List of unique bucket boundaries.
    :return: DataFrame with PD for each bucket.
    """
    # Assign each score to a bucket
    buckets = pd.cut(fico_scores, bins=bucket_boundaries, right=False, labels=False)

    # Calculate PD for each bucket
    pd_results = []
    for bucket in range(len(bucket_boundaries) - 1):
        bucket_indices = np.where(buckets == bucket)[0]
        num_defaults = defaults[bucket_indices].sum()
        num_records = len(bucket_indices)
        prob_default = num_defaults / num_records if num_records > 0 else 0
        pd_results.append({"Bucket": bucket, "PD": pd})

    return pd.DataFrame(pd_results)

fico_scores = data["fico_score"]
defaults = data["default"]

# Generate bucket boundaries
num_buckets = 8
bucket_boundaries = create_buckets(fico_scores, num_buckets)

# Calculate PD for each bucket
pd_results = calculate_pd_buckets(fico_scores, defaults, bucket_boundaries)
print("Bucket Boundaries:", bucket_boundaries)
print(pd_results)
