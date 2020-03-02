from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pathlib import Path
import re
# Imports

#url for reference
my_url = 'https://saikaiscan.com.br/novels/ascensao-de-um-deus-aud/post/capitulo-82-preparacao-para-o-torneio/4721'

print("BS4 Working!!!")
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
url = 0 #Just Creating the var
count = 0
def again(url, page_soup, count):

    for url in range(950): #Amount of chapters
        count = count + 1
        # locates the next page and create the url
        url = page_soup.find("a", {"class":"next"})["href"]
        my_url = 'https://saikaiscan.com.br' + url

        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        print("Download, Read & Close")

        page_soup = soup(page_html, "html.parser")
        Cap = page_soup.body.h2.text.strip().replace("?", "") # Get the Chapter and clear the special chars(win archives restrictions)
        Cap = Cap.replace("!", "")
        print("Leitura do " + Cap)

        #gets all the <p> whit 
        textPar = page_soup.findAll("p")
        archiveName = Cap.split()
        archiveName = archiveName[0] + " " + archiveName[1]
        out_filename = archiveName + ".txt"
        f = open(out_filename, "w", encoding='utf-8')
        f.write(Cap + "\n")
        print("Arquivo do " + Cap + " criado")

        # Creating the vars to use in while
        a = len(textPar)
        i = 0 #Vector position

        # While for write all the <p>
        while (i <= a):
            if (i == len(textPar)): #if textPar reaches hes maximum vector go next page
                again(url, page_soup, count)

            textCorrect = textPar[i].text.replace(".", ". ") #correction for the text
            if textCorrect == "":
                f.write("\n")
            else:
                f.write(textCorrect + "\n")#every <p> need a \n
                print(textCorrect)
            i = i + 1 #Vector position
    path = Path('Pasta')
    for out_filename in path.glob('*'):
        correct = out_filename.suffix
    if correct != ".txt":
        print("Erro no arquivo do " + Cap)
        exit()

    else:
        f.close()
        print("Fecha Arquivo")
again(url, page_soup, count)
