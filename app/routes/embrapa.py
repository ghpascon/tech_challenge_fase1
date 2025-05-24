from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user
from app.helpers.embrapa import get_json, get_json2
from app.schemas.embrapa import EmbrapaRequestAno
import requests
import os
from bs4 import BeautifulSoup

router = APIRouter(prefix="/embrapa", tags=["EMBRAPA"])

def create_backup_file(file_name, content):
    # Garante que a pasta existe
    folder = os.path.dirname(file_name)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    
    with open(file_name, "w") as arquivo:
        arquivo.write(content.prettify())
        print(f"Arquivo HTML de backup criado com sucesso em {file_name}.")

def get_backup_file(file_name):
    try:
        html = open(file_name).read()
        return BeautifulSoup(html, "html.parser")
    except:
        return None

def validate_filepath(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    return  filepath

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
    backup_file = f'app/data/embrapa_producao/backup_file_embrapa_producao_{filtros.ano}.html'
    try:
        url = f"http://vitibrasil.cnpuv.embapa.br/index.php?ano={filtros.ano}&opcao=opt_02"
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        create_backup_file(backup_file, soup)
        return get_json(soup)
    except:
        print("Rota fora do ar")
        soup = get_backup_file(backup_file)
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
    validate_filepath(f"app/data/embrapa_processamento/{filtros.ano}/")
    try:
        for i in range(1,5):
            backup_file = f'app/data/embrapa_processamento/{filtros.ano}/backup_file_embrapa_processamento_{filtros.ano}_subopt_0{i}.html'
            url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_03&subopcao=subopt_0{i}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            create_backup_file(backup_file, soup)
            soups.append(soup)
        soups[2]
    except:
        for i in range(1,5):
            backup_file = f'app/data/embrapa_processamento/{filtros.ano}/backup_file_embrapa_processamento_{filtros.ano}_subopt_0{i}.html'
            soup =get_backup_file(backup_file)
            soups.append(soup)

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
def embrapa_comercializacao(filtros: EmbrapaRequestAno = Depends(), current_user: dict = Depends(get_current_user)):
    """
    Consulta os dados de comercialização de vinhos da EMBRAPA para o ano especificado.

    Returns:
        dict: Dados extraídos da tabela de comercialização.
    """
    backup_file = f'app/data/embrapa_comercializacao/backup_file_embrapa_comercializacaoo_{filtros.ano}.html'
    try:
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_04"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        create_backup_file(backup_file, soup)
        return get_json(soup)
    except:
        soup = get_backup_file(backup_file)
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
    validate_filepath(f"app/data/embrapa_importacao/{filtros.ano}/")
    try:
        for i in range(1,6):
            backup_file = f'app/data/embrapa_importacao/{filtros.ano}/backup_file_embrapa_importacao_{filtros.ano}_subopt_0{i}.html'
            url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_05&subopcao=subopt_0{i}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            create_backup_file(backup_file, soup)
            soups.append(soup)
    except:
        for i in range(1,5):
            backup_file = f'app/data/embrapa_importacao/{filtros.ano}/backup_file_embrapa_importacao_{filtros.ano}_subopt_0{i}.html'
            soup = get_backup_file(backup_file)
            soups.append(soup)

    json = {}
    total = 0
    for soup in soups:
        current_json = get_json2(soup)
        total += current_json["total"]
        json[current_json["titulo"]] = current_json
    json["total"]=total
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
    validate_filepath(f"app/data/embrapa_exportacao/{filtros.ano}/")
    try:
        for i in range(1,5):
            backup_file = f'app/data/embrapa_exportacao/{filtros.ano}/backup_file_embrapa_exportacao_{filtros.ano}_subopt_0{i}.html'
            url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_05&subopcao=subopt_0{i}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            create_backup_file(backup_file, soup)
            soups.append(soup)
    except:
        for i in range(1, 5):
            backup_file = f'app/data/embrapa_exportacao/{filtros.ano}/backup_file_embrapa_exportacao_{filtros.ano}_subopt_0{i}.html'
            soup = get_backup_file(backup_file)
            soups.append(soup)

    json = {}
    total = 0
    for soup in soups:
        current_json = get_json2(soup)
        total += current_json["total"]
        json[current_json["titulo"]] = current_json
    json["total"] = total
    return json
