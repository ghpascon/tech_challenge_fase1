from fastapi import APIRouter,Depends
from app.auth.dependencies import get_current_user
from app.helpers.embrapa import get_json,get_json2
from app.schemas.embrapa import EmbrapaRequestAno
import requests
from bs4 import BeautifulSoup

router = APIRouter(prefix="/embrapa", tags=["EMBRAPA"])

@router.get(
    "/producao",
    summary="Obtem os dados de produção entre os anos de 1970 e 2023",
)
def embrapa_producao(filtros: EmbrapaRequestAno = Depends(), current_user: dict = Depends(get_current_user)):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_02"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return get_json(soup)

@router.get(
    "/processamento",
    summary="Obtem os dados de processamento entre os anos de 1970 e 2023",
)
def embrapa_processamento(filtros: EmbrapaRequestAno = Depends(), current_user: dict = Depends(get_current_user)):
    soups = []
    for i in range(1,5):
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
    json["total"]=total
    return json    


@router.get(
    "/comercializacao",
    summary="Obtem os dados de comercialização entre os anos de 1970 e 2023",
)
def embrapa_comercializacao(filtros: EmbrapaRequestAno = Depends(), current_user: dict = Depends(get_current_user)):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={filtros.ano}&opcao=opt_04"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return get_json(soup)

@router.get(
    "/importacao",
    summary="Obtem os dados de importação entre os anos de 1970 e 2023",
)
def embrapa_importacao(filtros: EmbrapaRequestAno = Depends(), current_user: dict = Depends(get_current_user)):
    soups = []
    for i in range(1,6):
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
    json["total"]=total
    return json    

@router.get(
    "/exportacao",
    summary="Obtem os dados de exportação entre os anos de 1970 e 2023",
)
def embrapa_exportacao(filtros: EmbrapaRequestAno = Depends(), current_user: dict = Depends(get_current_user)):
    soups = []
    for i in range(1,5):
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
    json["total"]=total
    return json    