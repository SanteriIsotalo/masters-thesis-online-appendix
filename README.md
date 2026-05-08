# masters-thesis-online-appendix
This repository contains all the data and code used for the master's thesis "Economic Paradigms in CEO Communication Analysis of Stakeholder Relations in Finnish Listed Companies' CEO Statements".

The thesis can be found here: (link will be added after the thesis gets published)

## Repository structure
- /data/ — CEO reviews (157 PDF files and 157 TXT files) for all sampled Finnish listed companies
- analysis.ipynb — Jupyter Notebook containing all statistical tests and visualizations reported in the thesis
- final_data.xlsx — Combines the manually implemented CDP data, sectors, segments and sentiment data
- Loughran-McDonald_MasterDictionary_1993-2025.csv — free for use in academic research, can be downloaded from https://sraf.nd.edu/loughranmcdonald-master-dictionary/
- sentiment_analysis.py — Python script for sentiment analysis using the Loughran-McDonald Master Dictionary. Expects input files in /data/ and the dictionary CSV in the root folder, as specified in the script.

## Requirements
- Python 3.12.9
- Path
- pandas
- seaborn
- matplotlib
- scipy
- scikit-posthocs
- statsmodels
