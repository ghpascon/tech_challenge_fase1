def get_json(soup):
    """
    Extrai informações de uma página HTML do tipo sopa BeautifulSoup e retorna um dicionário JSON contendo o título,
    ano, total e dados detalhados organizados em itens e subitens de uma tabela.

    A estrutura da tabela HTML é esperada conter linhas com células (`<td>`) com classes 'tb_item' para itens principais
    e 'tb_subitem' para subitens associados. A primeira célula de cada linha indica o tipo (item ou subitem) e as
    colunas subsequentes contêm dados, incluindo uma quantidade.

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup representando o HTML da página.

    Returns:
        dict: Um dicionário JSON com a seguinte estrutura:
            {
                "titulo": str,      # Título extraído do texto centralizado.
                "ano": int,          # Ano extraído do texto centralizado.
                "total": int,        # Valor total extraído da linha de rodapé da tabela.
                "tipo": list[dict]   # Lista de dicionários, onde cada dicionário representa um item principal
                                     # e contém as chaves "item" (nome do item) e "qtd" (uma lista de dicionários).
                                     # Para itens principais, "qtd" contém um dicionário com a chave 'total' e o valor da quantidade.
                                     # Para subitens, "qtd" contém uma lista de dicionários, onde cada dicionário tem o nome
                                     # do subitem como chave e a quantidade como valor.
            }
    """
    if soup is None:
        return {
            "msg": "Falha ao acessar a API e não foram encontrados arquivos de backup."
        }
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
    """
    Extrai informações de uma página HTML do tipo sopa BeautifulSoup e retorna um dicionário JSON contendo o título,
    ano, total e dados detalhados de uma tabela.

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup representando o HTML da página.

    Returns:
        dict: Um dicionário JSON com a seguinte estrutura:
            {
                "titulo": str,      # Título extraído do texto centralizado.
                "ano": int,          # Ano extraído do texto centralizado.
                "total": int,        # Valor total extraído da linha de rodapé da tabela.
                "tipo": list[dict]   # Lista de dicionários, onde cada dicionário representa uma linha da tabela
                                     # (excluindo o cabeçalho) e contém as chaves "pais", "qtd" e "valor".
            }
    """
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