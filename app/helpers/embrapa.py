def get_json(soup):
    # Pegando título e ano
    p_tag = soup.find("p", class_="text_center")
    text = p_tag.get_text(strip=True)
    titulo = text[:text.index('[')].strip()
    ano = int(text[text.index('[')+1:text.index(']')])
    
    #pegando dados da tabela
    table = soup.find("table", class_="tb_base tb_dados")
    dados = []
    item = {}
    for row in table.find_all("tr")[1:]:  # pula o header
        cols = row.find_all("td")
        classe = cols[0].get('class')
        qtd = cols[1].text.strip().replace('.','').replace('-','0')
        qtd = int(qtd)
        if classe is not None and classe[0] == 'tb_item':
            if not item == {}:
                dados.append(item)
                item = {}
            item["item"] = cols[0].text.strip()
            item["qtd"] = [{'total':qtd}]
        if classe is not None and classe[0] == 'tb_subitem':
            item["qtd"].append({
                cols[0].text.strip(): qtd,
            })
    if not item == {}:
        dados.append(item)        
    dados
    tfoot = table.find("tfoot", class_="tb_total")
    tds = tfoot.find_all("td")
    total = int(tds[1].text.strip().replace('.','').replace('-','0'))

    json = {
        "titulo":titulo,
        "ano":ano,
        "total":total,
        "tipo":dados
    }
    return json
def get_json2(soup):
    # Pegando título e ano
    p_tag = soup.find("p", class_="text_center")
    text = p_tag.get_text(strip=True)
    titulo = text[:text.index('[')].strip()
    ano = int(text[text.index('[')+1:text.index(']')])
    
    #pegando dados da tabela
    table = soup.find("table", class_="tb_base tb_dados")
    dados = []
    item = {}
    for row in table.find_all("tr")[1:]:  # pula o header
        cols = row.find_all("td")
        item["pais"]=cols[0].text.strip()
        item["qtd"]=int(cols[1].text.strip().replace('.','').replace('-','0'))
        item["valor"]=int(cols[2].text.strip().replace('.','').replace('-','0'))
        dados.append(item)
        item = {}
    
    tfoot = table.find("tfoot", class_="tb_total")
    tds = tfoot.find_all("td")
    total = int(tds[1].text.strip().replace('.','').replace('-','0'))

    json = {
        "titulo":titulo,
        "ano":ano,
        "total":total,
        "tipo":dados
    }
    return json