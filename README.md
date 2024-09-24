# Leo Chen Individual 1

[![Install](https://github.com/nogibjj/Leo_Chen_Individual_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Leo_Chen_Individual_1/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/Leo_Chen_Individual_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Leo_Chen_Individual_1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/Leo_Chen_Individual_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Leo_Chen_Individual_1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/Leo_Chen_Individual_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Leo_Chen_Individual_1/actions/workflows/test.yml)

[Click here to download and view the demo video](https://github.com/nogibjj/Leo_Chen_Individual_1/raw/refs/heads/main/demo.mp4)

Reads a dataset (CSV)

Generates summary statistics (mean, median, standard deviation)

Repository Contents:

* `mylib/lib.py`

* `test_lib.py`

* `main.py`

* `test_main.py`

* `main.ipynb`

* `.devcontainer`

* `install.yml`

* `format.yml`

* `lint.yml`

* `test.yml`

* `Makefile`

* `requirements.txt`

* `README.md`

* `bed_hist.png`

## Data Source

**covid-geography**

This file contains the data behind the story [How One High-Risk Community In Rural South Carolina Is Bracing For COVID-19](https://fivethirtyeight.com/features/how-one-high-risk-community-in-rural-south-carolina-is-bracing-for-covid-19/).

`mmsa-icu-beds.csv` combines data from the Centers for Disease Control and Prevention’s [Behavioral Risk Factor Surveillance System (BRFSS)](https://www.cdc.gov/brfss/smart/smart_2017.html), a collection of health-related surveys conducted each year of more than 400,000 Americans, and the [Kaiser Family Foundation](https://khn.org/news/as-coronavirus-spreads-widely-millions-of-older-americans-live-in-counties-with-no-icu-beds/#lookup) to show the number of people who are at high risk of becoming seriously ill from COVID-19 per ICU bed in each metropolitan area, micropolitan area or metropolitan division for which we have data.

Column | Description
-------|-------------
`MMSA` | The name of the metropolitan area, micropolitan area or metropolitan division available in the CDC’s BRFSS
`total_percent_at_risk` | The percent of individuals in that area that are at high risk of becoming seriously ill from COVID-19, per CDC’s BRFSS
`high_risk_per_icu_bed` | The number of high risk individuals per ICU bed in that area
`high_risk_per_hospital` |  The number of high risk individuals per hospital in that area
`icu_beds` | The number of ICU beds in the area, based on the Kaiser Family Foundation’s data
`hospitals` | The number of hospitals in the area, based on the Kaiser Family Foundation’s data
`total_at_risk` | The total number of high risk individuals in the area, per CDC’s BRFSS

*This project focuses on one column - `icu_beds`.*

[Link to data](https://github.com/fivethirtyeight/data/tree/master/covid-geography)

## Setup Instructions

1. Open codespaces

2. Load the repository into codespaces

3. Run the Makefile command: `make all`

## Result

Mean = 360.185, Median = 221, Standard Deviation = 450.581

Attaching the histogram below for quick reference.

![histogram](bed_hist.png)
