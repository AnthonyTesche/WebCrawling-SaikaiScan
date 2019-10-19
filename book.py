from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# Imports and Var creations

#url for reference
my_url = 'https://saikaiscan.com.br/novels/ascensao-de-um-deus-aud/post/capitulo-247-ervas-de-ranks-mutaveis/4899'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
print("Download, Read & Close - Start")

page_soup = soup(page_html, "html.parser")
url = 0 #Just Creating the var
count = 0 # Knowing the amounts of run

def again(url, page_soup, count):
    for url in range(950):
        print("Contador: ")
        print(count)
        count = count + 1

        # locates the next page and create the url
        url = page_soup.find("a", {"class":"next"})["href"]
        my_url = 'https://saikaiscan.com.br' + url

        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        print("Download, Read & Close - Mid")

        page_soup = soup(page_html, "html.parser")
        Cap = page_soup.body.h2.text.strip().replace("?", "") # Get the Chapter and clear the special chars(win archives restrictions)
        print("Leitura do " + Cap)

        #gets all the <p> whit 
        textPar = page_soup.findAll("p")

        out_filename = Cap + ".txt"
        f = open(out_filename, "w", encoding='utf-8')
        f.write(Cap + "\n")
        print("Arquivo " + Cap + "criado")

        # Creating the vars to use in while
        a = len(textPar)
        i = 0 #Vector position

        # While for write all the <p>
        while (i <= a):
            if (i == len(textPar)): #if textPar reaches hes maximum vector go next page
                again(url, page_soup, count)

            textCorrect = textPar[i].text.replace(".", ". ") #correction for the text
            f.write(textCorrect + "\n")#every <p> need a \n
            i = i + 1 #Vector position

    f.close()
    print("Fecha Arquivo")
again(url, page_soup, count)