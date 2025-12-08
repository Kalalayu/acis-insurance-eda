# acis-insurance-eda
End-to-end insurance risk analytics &amp; predictive modeling for AlphaCare
Task 3 – A/B Hypothesis Testing: Insurance Risk Drivers
Overview

This task focuses on statistically validating or rejecting key hypotheses about risk drivers in the insurance portfolio. The analysis uses Claim Frequency, Claim Severity, and Margin to quantify risk and inform segmentation strategy.

Hypotheses Tested

H₀: No risk differences across provinces

H₀: No risk differences between zip codes

H₀: No significant margin (profit) difference between zip codes

H₀: No significant risk difference between Female and Male clients

Methodology

Data Preparation: Cleaned Gender column to include only 'Male' and 'Female'.

Group Segmentation: Control (Group A) and Test (Group B) defined per feature.

Statistical Tests:

t-tests for numerical KPIs (Claim Severity, Margin)

z-test for proportion (Claim Frequency by Gender)

Significance Level: p-value < 0.05 indicates rejection of H₀
