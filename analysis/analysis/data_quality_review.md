# Data Quality Review and Recommendations  
**Client:** Sprocket Central Pty Ltd

## Introduction
Thank you for sharing the datasets from Sprocket Central Pty Ltd.  
This document summarises the data quality issues identified and provides recommendations to improve data reliability.

## Summary of Data Quality Issues

| Dataset | Issues Identified |
|------|----------------|
| Transactions | Completeness, Relevancy |
| New Customer List | Completeness, Consistency |
| Customer Demographic | Completeness, Consistency, Relevancy |

---

## Transactions Dataset
**Issues Identified**
- Missing values in `online_order` and `brand`
- `product_first_sold_date` stored in non-readable numeric format

**Actions Taken**
- Identified and flagged missing values
- Converted `product_first_sold_date` into date/time format

**Recommendation**
- Enforce validation rules during data ingestion
- Standardise date formats during data import

---

## New Customer List Dataset
**Issues Identified**
- Missing values in `job_title` and `industry`
- Inconsistent values in `gender`
- Blank values in `second_name`

**Actions Taken**
- Standardised gender values to `M` and `F`
- Removed irrelevant category `U`
- Retained `second_name` as optional

**Recommendation**
- Apply controlled vocabularies for categorical variables
- Validate mandatory fields at data entry stage

---

## Customer Demographic Dataset
**Issues Identified**
- Missing and inconsistent gender values
- Null values in `job_title` and `job_industry`
- Irrelevant column `default`

**Actions Taken**
- Standardised gender values
- Removed irrelevant column
- Flagged missing occupational data

---

## Conclusion
Addressing these data quality issues will improve analytical accuracy and ensure reliable insights for customer targeting and predictive modelling.

**Prepared by:**  
Sumi Sukumari Vikraman  
Junior Analyst, ISM Dortmund
