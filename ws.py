from selenium import webdriver
import neural

driver = webdriver.Chrome(executable_path="chromedriver.exe")

profissoes = ('engenheiro de dados', 'analista de bi', 'cientista de dados')
for cargo in profissoes:
    csv = str(cargo) + '.csv'
    first = cargo.replace(' ', '-')
    second = cargo.replace(' ', '%20')

    driver.get("https://www.catho.com.br/vagas/" + first + "/?q=" + second + "&page=1")

    #get pages
    ul = driver.find_elements_by_id("search-result")
    for list in ul:
        xpath = list.find_elements_by_tag_name("span")
        for xp in xpath:
            if xp.get_attribute("class") == 'Mobile__Info-sc-1h7l4jx-0 glochE':
                total = str(xp.get_attribute("innerHTML")).split(" de ")
                paginas = total[1]

    with open('scrap/' + csv, 'w', encoding='utf-8') as f:
        #Escreve header Titulo, url, regiao, descricao
        f.writelines("titulo;url;regiao;descricao")
        f.write('\n')
        page = 1
        while page <= int(paginas):
            http = "https://www.catho.com.br/vagas/" + first + "/?q=" + second + "&page=" + str(page)
            driver.get(http)
            
            print(str(page) + " of " + str(paginas) + " for " + cargo )

            #loop through pages
            ul = driver.find_elements_by_id("search-result")
            for list in ul:
                li = list.find_elements_by_tag_name("li")
                for i in li:
                    article = i.find_elements_by_tag_name("article")

                    pg = 1
                    linha = [] #Titulo, url, regiao, descricao
                    for x in article:
                        header = x.find_elements_by_tag_name("header")
                        for i in header:
                            aTag = i.find_elements_by_tag_name("a")
                            for a in aTag: #titulo e url
                                href = a.get_attribute('href')
                                if "entrada_apply" in href:
                                    title = str(a.text).replace(";","")
                                    url = str(href).replace(";", "")
                                    #linha.append(a.text)
                                    #linha.append(href)
                                    #print(a.text, ' - ', href)
                                elif not "entrada_apply" in href:
                                    region = str(a.text).replace(";", "")
                                    #linha.append(a.text)
                                    #print("Região:", a.text)  

                        btn = x.find_elements_by_tag_name("button")
                        for button in btn:
                            if "continuar lendo" in button.text:
                                button.click()
                                aria_label = button.get_attribute("aria-label")
                                description = str(aria_label.strip()).replace(";", "")
                                description = str(description).replace("\n", " ").replace("\r", " ")

                        f.write(title + ";" + url + ";" + region + ";" + description )
                        f.write('\n')
                        break
            
            page += 1
            
    neural.generate_nltk(str(cargo))

