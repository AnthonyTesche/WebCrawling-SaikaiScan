# WebScraping-SaikaiScan
- Author: Anthony Tesche

## Version - 0.1.0
- Some corrections in apresentation

## Description
- Want to read any novel hosted on Saikai Scan? Use this "Software" to download in .txt all the Chapters.

## How to use
- Find the var "my_url" and change for the url of your first chapter novel
- Change for the amount of chapters your novel have "for url in range(x)"
- In case you try to use in another site change this line "my_url = 'https://saikaiscan.com.br' + url"

## Observations
- Use with Python ^3
- If encounter this error "ImportError: No module named bs4 in Windows" use the ""pip install BeautifulSoup4"".

## Bugs (Working in Fix)
- Some chapters dont generate the .txt but the bs4 catch the <p>(Paragraph) and generate a blank archive with no extension.