# Runbook Comparion Utility
These scripts will allow you to automatically check to see if the Public Runbook README.md file is missing any files from the Public Runbook Repository

## Prerequisites

1. Download all of the files to a folder called `RunbookComparisonUtility`

2. To begin you will need to create or update the `RunbookIndex.txt` file. This file is created by copying all of the raw code from [https://github.com/IBM/itz-support-public/blob/main/IBM-Technology-Zone/README.md](https://github.com/IBM/itz-support-public/blob/main/IBM-Technology-Zone/README.md) and pasting into a text editor to save as a `.txt` file:

<img width="1387" alt="raw-readme" src="https://github.com/joshshiman/RunbookComparisonUtility/assets/146133452/7c5a09b5-56d0-465a-b12a-37676c82a055">

3. Secondly you will need to update or create an `AllRunbooks.txt` file. This file is created by selecting and copying all of the runbook names from the `IBM-Technology-Zone/IBM-Technology-Zone-Runbooks` [GitHub repository](https://github.com/IBM/itz-support-public/blob/main/IBM-Technology-Zone/IBM-Technology-Zone-Runbooks).

<img width="1421" alt="select-all" src="https://github.com/joshshiman/RunbookComparisonUtility/assets/146133452/09eaf376-34d8-4858-a46f-4dafce1dddf6">

## How to Use

Ensure you have `Git`, `Pip` and `Python3` installed before continuing.

Clone the repository by running this command `git clone https://github.com/joshshiman/RunbookComparisonUtility.git`

Create a virtual environment in the terminal of your editor by using `python -m venv venv`

Activate the virtual environment by running the following in your terminal `source venv/bin/activate`

Install Dependencies `pip3 install -r requirements.txt`


Run the `main.py` file
