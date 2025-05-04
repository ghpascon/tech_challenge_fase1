from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user
from app.helpers.embrapa import get_json, get_json2
from app.schemas.embrapa import EmbrapaRequestAno
import requests
from bs4 import BeautifulSoup

router = APIRouter(prefix="/embrapa", tags=["EMBRAPA"])

@router.get(
    "/producao",
    summary="Obtem os dados de produção entre os anos de 1970 e 2023",
)
def embrapa_producao(
    filtros: EmbrapaRequestAno = Depends(), 
    current_user: dict = Depends(get_current_user)
):
    """
    Consulta os dados de produção de uvas da EMBRAPA para o ano especificado.

    Args:
        filtros (EmbrapaRequestAno): Objeto contendo o ano desejado.
        current_user (dict): Usuário autenticado (validação via dependência).

    Returns:
        dict: Dados extraídos da tabela de produção.
    """
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_02"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return get_json(soup)

@router.get(
    "/processamento",
    summary="Obtem os dados de processamento entre os anos de 1970 e 2023",
)
def embrapa_processamento(
    filtros: EmbrapaRequestAno = Depends(), 
    current_user: dict = Depends(get_current_user)
):
    """
    Consulta os dados de processamento de uvas da EMBRAPA para o ano especificado.

    O processamento está dividido em 4 subcategorias, cada uma representada por uma subopção.

    Returns:
        dict: Dados consolidados de todas as subcategorias, incluindo total geral.
    """
    soups = []
    for i in range(1, 5):
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_03&subopcao=subopt_0{i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        soups.append(soup)
    soups[2]
    
    json = {}
    total = 0
    for soup in soups:
        current_json = get_json(soup)
        total += current_json["total"]
        json[current_json["titulo"]] = current_json
    json["total"] = total
    return json

@router.get(
    "/comercializacao",
    summary="Obtem os dados de comercialização entre os anos de 1970 e 2023",
)
def embrapa_comercializacao(
    filtros: EmbrapaRequestAno = Depends(), 
    current_user: dict = Depends(get_current_user)
):
    """
    Consulta os dados de comercialização de vinhos da EMBRAPA para o ano especificado.

    Returns:
        dict: Dados extraídos da tabela de comercialização.
    """
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_04"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return get_json(soup)

@router.get(
    "/importacao",
    summary="Obtem os dados de importação entre os anos de 1970 e 2023",
)
def embrapa_importacao(
    filtros: EmbrapaRequestAno = Depends(), 
    current_user: dict = Depends(get_current_user)
):
    """
    Consulta os dados de importação de vinhos da EMBRAPA para o ano especificado.

    A importação está dividida em 5 subcategorias.

    Returns:
        dict: Dados consolidados das subcategorias, com total geral.
    """
    soups = []
    for i in range(1, 6):
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_05&subopcao=subopt_0{i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        soups.append(soup)

    json = {}
    total = 0
    for soup in soups:
        current_json = get_json2(soup)
        total += current_json["total"]
        json[current_json["titulo"]] = current_json
    json["total"] = total
    return json

@router.get(
    "/exportacao",
    summary="Obtem os dados de exportação entre os anos de 1970 e 2023",
)
def embrapa_exportacao(
    filtros: EmbrapaRequestAno = Depends(), 
    current_user: dict = Depends(get_current_user)
):
    """
    Consulta os dados de exportação de vinhos da EMBRAPA para o ano especificado.

    A exportação está dividida em 4 subcategorias, semelhantes às da importação.

    Returns:
        dict: Dados consolidados das subcategorias, com total geral.
    """
    soups = []
    for i in range(1, 5):
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_05&subopcao=subopt_0{i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        soups.append(soup)

    json = {}
    total = 0
    for soup in soups:
        current_json = get_json2(soup)
        total += current_json["total"]
        json[current_json["titulo"]] = current_json
    json["total"] = total
    return json
