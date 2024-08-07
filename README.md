# NonProfitsLNK

This repository contains code used to extract information from nonprofit 990 filings, using raw IRS data, and the ProPublica nonprofit search API.

IRS990GetAndParse.py creates an object with functions that allow for the bulk download of specified years of 990 filing data, unzipping them, removing .xml files that have undesirable cities/states in them, then converting the resulting .xml files into a single .csv.

The Propublica tools allow for bulk querying the Propublica Non-Profit Search API using EINs obtained using the IRS990GetAndParse build in "get EIDs" Function.

IRS 990 sources:
https://www.irs.gov/charities-non-profits/form-990-series-downloads
For entities making under $50,000: https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-bulk-data-downloads#990-n

Propublica Non-Profit Search API documentation
https://projects.propublica.org/nonprofits/api
