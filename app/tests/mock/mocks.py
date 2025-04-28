
def mock_html1():
    html = """<!-- versão 2.00 -->
<!DOCTYPE html>

<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="Na página 'Vitibrasil' são apresentadas informações referentes à quantidade de uvas processadas, produção e comercialização de vinhos, suco e derivados provenientes do Estado do Rio Grande do Sul, que representa mais de 90% da produção nacional. Também são apresentados os dados de importações e exportações dos produtos da vitivinicultura." name="description"/>
<meta content="Vinhos, Espumante, Uva, Uvas passas, Suco de uva, Produção, Processamento, Comercialização, Importação, Exportação, Publicação" lang="pt-BR" name="keywords"/>
<meta content="Embrapa Uva e Vinho" name="author"/>
<link href="./figures/favicon.ico" rel="Shortcut Icon"/>
<link href="vitibrasil.css" rel="stylesheet" type="text/css"/>
<title>Banco de dados de uva, vinho e derivados</title>
<script>
    var x = screen.width;
    window.onload = function() {  
      var meta = document.createElement('meta');
      meta.name = "viewport";
      if(x < 780) {
        var val = x/780;
        meta.content = 'width=device-width, initial-scale=' + val;
      }
      else {
        meta.content = 'width=device-width, initial-scale=1.0';
      }
      document.getElementsByTagName('head')[0].appendChild(meta);
    }
  </script>
<!-- Piwik -->
<script type="text/javascript">
    var _paq = _paq || [];
    _paq.push(['trackPageView']);
    _paq.push(['enableLinkTracking']);
    (function() {
      var u=(("https:" == document.location.protocol) ? "https" : "http") + "://hotsites.cnpuv.embrapa.br/estatisticas/";
      _paq.push(['setTrackerUrl', u+'piwik.php']);
      _paq.push(['setSiteId', 3]);
      var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; g.type='text/javascript';
      g.defer=true; g.async=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
    })();
  </script>
<noscript><p><img alt="" src="http://hotsites.cnpuv.embrapa.br/estatisticas/piwik.php?idsite=3" style="border:0;"/></p></noscript>
<!-- End Piwik Code -->
</head>
<body>
<table class="tb_layout" id="_top">
<tr>
<td> </td>
<td class="col_center" id="td_center">
<table class="tb_base">
<tr>
<td>
<p id="program_title">Dados da Vitivinicultura</p>
</td>
<td>
<p id="program_mail">
<a href="loiva.mello@embrapa.br">Loiva Maria Ribeiro de Mello</a>
<br/>
<a href="carlos.machado@embrapa.br">Carlos Alberto Ely Machado</a>
</p>
</td>
</tr>
</table>
</td>
<td> </td>
</tr>
</table>
<table class="tb_layout">
<tr>
<td id="tb_banner"></td>
</tr>
</table>
<table class="tb_layout no_print">
<tr>
<td> </td>
<td class="col_center" id="row_height">
<form action="index.php" method="get">
<p id="row_btn">
<button class="btn_opt" name="opcao" type="submit" value="opt_01">Apresentação</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_02">Produção</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_03">Processamento</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_04">Comercialização</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_05">Importação</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_06">Exportação</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_07">Publicação</button>
</p>
</form>
<script>
            var btn = 'opt_02';
            var item = document.querySelector('button[value=' + btn + ']');
            item.setAttribute('id','btn_active');
          </script>
</td>
<td> </td>
</tr>
</table>
<table class="tb_base">
<tr>
<td> </td>
<td class="col_center">
<div class="div_content">
<p class="subtitle_1">Banco de dados de uva, vinho e derivados</p>
<p class="subtitle_2">Produção de vinhos, sucos e derivados do Rio Grande do Sul</p>
<table class="tb_base tb_header no_print">
<tr>
<td>
           
        </td>
<td>
<form action="index.php">
<p id="p_navegano">
<button name="ano" type="submit" value="1970">«</button>
<button name="ano" onclick="if(this.value&lt;1970){this.value=1970}" type="submit" value="2022">‹</button>
<button disabled="disabled" id="neutral"> </button>
<button name="ano" onclick="if(this.value&gt;2023){this.value=2023}" type="submit" value="2024">›</button>
<button name="ano" type="submit" value="2023">»</button>
<input name="opcao" type="hidden" value="opt_02"/>
</p>
</form>
</td>
<td>
<form action="index.php">
<p id="p_ano">
<label class="lbl_pesq">Ano: [1970-2023] </label> <br/>
<input autocomplete="off" class="text_pesq" max="2023" min="1970" name="ano" onkeydown="return event.keyCode !== 69" required="" type="number" value=""/> 
              <input class="subm_pesq" type="submit" value="Ok"/>
<input name="opcao" type="hidden" value="opt_02"/>
</p>
</form>
</td>
</tr>
</table>
<div class="content_center">
<p class="text_center"> Produção de vinhos, sucos e derivados  [2023] </p>
<table class="tb_base tb_dados">
<thead>
<tr>
<th>Produto </th>
<th>Quantidade (L.) </th>
</tr>
</thead>
<tbody>
<tr>
<td class="tb_item">
                VINHO DE MESA
              </td>
<td class="tb_item">
                169.762.429
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Tinto
              </td>
<td class="tb_subitem">
                139.320.884
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Branco
              </td>
<td class="tb_subitem">
                27.910.299
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Rosado
              </td>
<td class="tb_subitem">
                2.531.246
              </td>
</tr>
<tr>
<td class="tb_item">
                VINHO FINO DE MESA (VINIFERA)
              </td>
<td class="tb_item">
                46.268.556
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Tinto
              </td>
<td class="tb_subitem">
                23.615.783
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Branco
              </td>
<td class="tb_subitem">
                20.693.437
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Rosado
              </td>
<td class="tb_subitem">
                1.959.336
              </td>
</tr>
<tr>
<td class="tb_item">
                SUCO
              </td>
<td class="tb_item">
                67.045.238
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Suco de uva integral
              </td>
<td class="tb_subitem">
                38.122.173
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Suco de uva concentrado
              </td>
<td class="tb_subitem">
                28.216.760
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Suco de uva adoçado
              </td>
<td class="tb_subitem">
                94.587
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Suco de uva orgânico
              </td>
<td class="tb_subitem">
                611.718
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Suco de uva reconstituído
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_item">
                DERIVADOS
              </td>
<td class="tb_item">
                174.716.647
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Espumante
              </td>
<td class="tb_subitem">
                65.525
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Espumante moscatel
              </td>
<td class="tb_subitem">
                14.744
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Base espumante
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Base espumante moscatel
              </td>
<td class="tb_subitem">
                6.734.590
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Base Champenoise champanha
              </td>
<td class="tb_subitem">
                1.552.243
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Base Charmat champanha
              </td>
<td class="tb_subitem">
                5.418.118
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Bebida de uva
              </td>
<td class="tb_subitem">
                1.627
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Polpa de uva
              </td>
<td class="tb_subitem">
                1.388.251
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Mosto simples
              </td>
<td class="tb_subitem">
                157.848.983
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Mosto concentrado
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Mosto de uva com bagaço
              </td>
<td class="tb_subitem">
                7.784
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Mosto dessulfitado
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Mistelas
              </td>
<td class="tb_subitem">
                600
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Néctar de uva
              </td>
<td class="tb_subitem">
                70.976
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Licorosos
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Compostos
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Jeropiga
              </td>
<td class="tb_subitem">
                4.500
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Filtrado
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Frisante
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Vinho leve
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Vinho licoroso
              </td>
<td class="tb_subitem">
                73.600
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Brandy
              </td>
<td class="tb_subitem">
                450
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Destilado
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Bagaceira
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Licor de bagaceira
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Vinagre
              </td>
<td class="tb_subitem">
                9.000
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Borra líquida
              </td>
<td class="tb_subitem">
                758.140
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Borra seca
              </td>
<td class="tb_subitem">
                17.200
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Vinho Composto
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Pisco
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Vinho orgânico
              </td>
<td class="tb_subitem">
                94.150
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Espumante orgânico
              </td>
<td class="tb_subitem">
                1.365
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Destilado alcoólico simples de bagaceira
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Vinho acidificado
              </td>
<td class="tb_subitem">
                2.500
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Mosto parcialmente fermentado
              </td>
<td class="tb_subitem">
                -
              </td>
</tr>
<tr>
<td class="tb_subitem">
                Outros derivados
              </td>
<td class="tb_subitem">
                652.301
              </td>
</tr>
</tbody>
<tfoot class="tb_total">
<tr>
<td>
            Total
          </td>
<td>
            457.792.870
          </td>
</tr>
</tfoot>
</table>
<div class="tb_font">
      Fonte: União Brasileira de Vitivinicultura - UVIBRA <br/> Elaboração: EMBRAPA/CNPUV <br/>
</div>
<table class="tb_base tb_link no_print">
<tr>
<td>
<a class="footer_content" href="download/Producao.csv" target="_blank">
<img alt="" height="16" src="figures/download.png" width="16"/>
<span class="spn_small">DOWNLOAD</span>
</a>
</td>
<td class="footer_right">
<a class="footer_content" href="#_top">
<img alt="" height="16" src="figures/topo.png" width="16"/>
<span class="spn_small">TOPO</span>
</a>
</td>
</tr>
</table>
</div>
</div>
</td>
<td> </td>
</tr>
</table>
<table class="tb_base">
<tr>
<td> </td>
<td class="col_center">
<table class="tb_base tb_footer">
<tr>
<td>
                Copyright © Embrapa Uva e Vinho. Todos os direitos reservados.<br/>
                Mais informações: <a class="footer_sac" href="https://www.embrapa.br/fale-conosco/sac">https://www.embrapa.br/fale-conosco/sac</a><br/>
                Última modificação: 21/12/23       
              </td>
<td class="footer_right">
                Rua Livramento 515, Caixa Postal 130<br/>
                95700-000 Bento Gonçalves, RS - Brasil<br/>
                Fone: (54) 3455-8000 - Fax: (54) 3451-2792
              </td>
</tr>
</table>
</td>
<td> </td>
</tr>
</table>
</body>
</html>"""
    return html


def expected_html1():
    return {'titulo': 'Produção de vinhos, sucos e derivados', 'ano': 2023, 'total': 457792870, 'tipo': [{'item': 'VINHO DE MESA', 'qtd': [{'total': 169762429}, {'Tinto': 139320884}, {'Branco': 27910299}, {'Rosado': 2531246}]}, {'item': 'VINHO FINO DE MESA (VINIFERA)', 'qtd': [{'total': 46268556}, {'Tinto': 23615783}, {'Branco': 20693437}, {'Rosado': 1959336}]}, {'item': 'SUCO', 'qtd': [{'total': 67045238}, {'Suco de uva integral': 38122173}, {'Suco de uva concentrado': 28216760}, {'Suco de uva adoçado': 94587}, {'Suco de uva orgânico': 611718}, {'Suco de uva reconstituído': 0}]}, {'item': 'DERIVADOS', 'qtd': [{'total': 174716647}, {'Espumante': 65525}, {'Espumante moscatel': 14744}, {'Base espumante': 0}, {'Base espumante moscatel': 6734590}, {'Base Champenoise champanha': 1552243}, {'Base Charmat champanha': 5418118}, {'Bebida de uva': 1627}, {'Polpa de uva': 1388251}, {'Mosto simples': 157848983}, {'Mosto concentrado': 0}, {'Mosto de uva com bagaço': 7784}, {'Mosto dessulfitado': 0}, {'Mistelas': 600}, {'Néctar de uva': 70976}, {'Licorosos': 0}, {'Compostos': 0}, {'Jeropiga': 4500}, {'Filtrado': 0}, {'Frisante': 0}, {'Vinho leve': 0}, {'Vinho licoroso': 73600}, {'Brandy': 450}, {'Destilado': 0}, {'Bagaceira': 0}, {'Licor de bagaceira': 0}, {'Vinagre': 9000}, {'Borra líquida': 758140}, {'Borra seca': 17200}, {'Vinho Composto': 0}, {'Pisco': 0}, {'Vinho orgânico': 94150}, {'Espumante orgânico': 1365}, {'Destilado alcoólico simples de bagaceira': 0}, {'Vinho acidificado': 2500}, {'Mosto parcialmente fermentado': 0}, {'Outros derivados': 652301}]}]}


def mock_html2():
    html = """<!-- versão 2.00 -->
<!DOCTYPE html>

<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="Na página 'Vitibrasil' são apresentadas informações referentes à quantidade de uvas processadas, produção e comercialização de vinhos, suco e derivados provenientes do Estado do Rio Grande do Sul, que representa mais de 90% da produção nacional. Também são apresentados os dados de importações e exportações dos produtos da vitivinicultura." name="description"/>
<meta content="Vinhos, Espumante, Uva, Uvas passas, Suco de uva, Produção, Processamento, Comercialização, Importação, Exportação, Publicação" lang="pt-BR" name="keywords"/>
<meta content="Embrapa Uva e Vinho" name="author"/>
<link href="./figures/favicon.ico" rel="Shortcut Icon"/>
<link href="vitibrasil.css" rel="stylesheet" type="text/css"/>
<title>Banco de dados de uva, vinho e derivados</title>
<script>
    var x = screen.width;
    window.onload = function() {  
      var meta = document.createElement('meta');
      meta.name = "viewport";
      if(x < 780) {
        var val = x/780;
        meta.content = 'width=device-width, initial-scale=' + val;
      }
      else {
        meta.content = 'width=device-width, initial-scale=1.0';
      }
      document.getElementsByTagName('head')[0].appendChild(meta);
    }
  </script>
<!-- Piwik -->
<script type="text/javascript">
    var _paq = _paq || [];
    _paq.push(['trackPageView']);
    _paq.push(['enableLinkTracking']);
    (function() {
      var u=(("https:" == document.location.protocol) ? "https" : "http") + "://hotsites.cnpuv.embrapa.br/estatisticas/";
      _paq.push(['setTrackerUrl', u+'piwik.php']);
      _paq.push(['setSiteId', 3]);
      var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; g.type='text/javascript';
      g.defer=true; g.async=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
    })();
  </script>
<noscript><p><img alt="" src="http://hotsites.cnpuv.embrapa.br/estatisticas/piwik.php?idsite=3" style="border:0;"/></p></noscript>
<!-- End Piwik Code -->
</head>
<body>
<table class="tb_layout" id="_top">
<tr>
<td> </td>
<td class="col_center" id="td_center">
<table class="tb_base">
<tr>
<td>
<p id="program_title">Dados da Vitivinicultura</p>
</td>
<td>
<p id="program_mail">
<a href="loiva.mello@embrapa.br">Loiva Maria Ribeiro de Mello</a>
<br/>
<a href="carlos.machado@embrapa.br">Carlos Alberto Ely Machado</a>
</p>
</td>
</tr>
</table>
</td>
<td> </td>
</tr>
</table>
<table class="tb_layout">
<tr>
<td id="tb_banner"></td>
</tr>
</table>
<table class="tb_layout no_print">
<tr>
<td> </td>
<td class="col_center" id="row_height">
<form action="index.php" method="get">
<p id="row_btn">
<button class="btn_opt" name="opcao" type="submit" value="opt_01">Apresentação</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_02">Produção</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_03">Processamento</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_04">Comercialização</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_05">Importação</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_06">Exportação</button>
<button class="btn_opt" name="opcao" type="submit" value="opt_07">Publicação</button>
</p>
</form>
<script>
            var btn = 'opt_05';
            var item = document.querySelector('button[value=' + btn + ']');
            item.setAttribute('id','btn_active');
          </script>
</td>
<td> </td>
</tr>
</table>
<table class="tb_base">
<tr>
<td> </td>
<td class="col_center">
<div class="div_content">
<p class="subtitle_1">Banco de dados de uva, vinho e derivados</p>
<p class="subtitle_2">Importação de derivados de uva</p>
<table class="tb_base tb_header no_print">
<tr>
<td>
<form action="index.php" method="get">
<p>
<button class="btn_sopt" name="subopcao" type="submit" value="subopt_01">Vinhos de mesa</button><br/>
<button class="btn_sopt" name="subopcao" type="submit" value="subopt_02">Espumantes</button><br/>
<button class="btn_sopt" name="subopcao" type="submit" value="subopt_03">Uvas frescas</button><br/>
<button class="btn_sopt" name="subopcao" type="submit" value="subopt_04">Uvas passas</button><br/>
<button class="btn_sopt" name="subopcao" type="submit" value="subopt_05">Suco de uva</button>
<input name="opcao" type="hidden" value="opt_05"/>
</p>
</form>
<script>
            var btn1 = 'subopt_01';
            var item1 = document.querySelector('button[value=' + btn1 + ']');
            item1.setAttribute('id','btn1_active');
          </script>
</td>
<td>
<form action="index.php">
<p id="p_navegano">
<button name="ano" type="submit" value="1970">«</button>
<button name="ano" onclick="if(this.value&lt;1970){this.value=1970}" type="submit" value="2022">‹</button>
<button disabled="disabled" id="neutral"> </button>
<button name="ano" onclick="if(this.value&gt;2024){this.value=2024}" type="submit" value="2024">›</button>
<button name="ano" type="submit" value="2024">»</button>
<input name="opcao" type="hidden" value="opt_05"/>
<input name="subopcao" type="hidden" value="subopt_01"/>
</p>
</form>
</td>
<td>
<form action="index.php">
<p id="p_ano">
<label class="lbl_pesq">Ano: [1970-2024] </label> <br/>
<input autocomplete="off" class="text_pesq" max="2024" min="1970" name="ano" onkeydown="return event.keyCode !== 69" required="" type="number" value=""/> 
              <input class="subm_pesq" type="submit" value="Ok"/>
<input name="opcao" type="hidden" value="opt_05"/>
<input name="subopcao" type="hidden" value="subopt_01"/>
</p>
</form>
</td>
</tr>
</table>
<div class="content_center">
<p class="text_center">Importação de vinhos de mesa [2023] </p>
<table class="tb_base tb_dados">
<thead>
<tr>
<th>Países</th>
<th>Quantidade (Kg)</th>
<th>Valor (US$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>
            Africa do Sul
          </td>
<td> 
                    522.733  
                  </td>
<td> 
                    1.732.850  
                  </td>
</tr>
<tr>
<td>
            Alemanha
          </td>
<td> 
                    102.456  
                  </td>
<td> 
                    557.947  
                  </td>
</tr>
<tr>
<td>
            Argélia
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Arábia Saudita
          </td>
<td> 
                    8  
                  </td>
<td> 
                    161  
                  </td>
</tr>
<tr>
<td>
            Argentina
          </td>
<td> 
                    25.276.991  
                  </td>
<td> 
                    83.918.138  
                  </td>
</tr>
<tr>
<td>
            Armênia
          </td>
<td> 
                    3.542  
                  </td>
<td> 
                    24.336  
                  </td>
</tr>
<tr>
<td>
            Austrália
          </td>
<td> 
                    432.829  
                  </td>
<td> 
                    1.568.550  
                  </td>
</tr>
<tr>
<td>
            Áustria
          </td>
<td> 
                    16.832  
                  </td>
<td> 
                    145.475  
                  </td>
</tr>
<tr>
<td>
            Bermudas
          </td>
<td> 
                    6  
                  </td>
<td> 
                    879  
                  </td>
</tr>
<tr>
<td>
            Bélgica
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Bolívia
          </td>
<td> 
                    1.170  
                  </td>
<td> 
                    10.920  
                  </td>
</tr>
<tr>
<td>
            Bósnia-Herzegovina
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Brasil
          </td>
<td> 
                    6.229  
                  </td>
<td> 
                    76.894  
                  </td>
</tr>
<tr>
<td>
            Bulgária
          </td>
<td> 
                    40.281  
                  </td>
<td> 
                    95.232  
                  </td>
</tr>
<tr>
<td>
            Canada
          </td>
<td> 
                    14  
                  </td>
<td> 
                    1.062  
                  </td>
</tr>
<tr>
<td>
            Chile
          </td>
<td> 
                    62.358.765  
                  </td>
<td> 
                    170.146.247  
                  </td>
</tr>
<tr>
<td>
            China
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Coreia do Sul, República
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Croácia
          </td>
<td> 
                    1.107  
                  </td>
<td> 
                    9.160  
                  </td>
</tr>
<tr>
<td>
            Cuba
          </td>
<td> 
                    8  
                  </td>
<td> 
                    261  
                  </td>
</tr>
<tr>
<td>
            Emirados Árabes Unidos
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Eslovênia
          </td>
<td> 
                    28.806  
                  </td>
<td> 
                    124.283  
                  </td>
</tr>
<tr>
<td>
            Eslováquia
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Espanha
          </td>
<td> 
                    6.591.628  
                  </td>
<td> 
                    20.097.228  
                  </td>
</tr>
<tr>
<td>
            Estados Unidos
          </td>
<td> 
                    244.276  
                  </td>
<td> 
                    1.775.713  
                  </td>
</tr>
<tr>
<td>
            França
          </td>
<td> 
                    4.899.631  
                  </td>
<td> 
                    30.421.272  
                  </td>
</tr>
<tr>
<td>
            Geórgia
          </td>
<td> 
                    17.173  
                  </td>
<td> 
                    29.084  
                  </td>
</tr>
<tr>
<td>
            Geórgia do Sul e Sandwich do Sul, Ilhas
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Grécia
          </td>
<td> 
                    45.889  
                  </td>
<td> 
                    147.724  
                  </td>
</tr>
<tr>
<td>
            Hong Kong
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Hungria
          </td>
<td> 
                    41.905  
                  </td>
<td> 
                    316.481  
                  </td>
</tr>
<tr>
<td>
            Indonésia
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Irlanda
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Israel
          </td>
<td> 
                    48.772  
                  </td>
<td> 
                    259.405  
                  </td>
</tr>
<tr>
<td>
            Itália
          </td>
<td> 
                    8.868.133  
                  </td>
<td> 
                    34.760.596  
                  </td>
</tr>
<tr>
<td>
            Japão
          </td>
<td> 
                    86  
                  </td>
<td> 
                    3.427  
                  </td>
</tr>
<tr>
<td>
            Iugoslávia
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Líbano
          </td>
<td> 
                    14.328  
                  </td>
<td> 
                    106.610  
                  </td>
</tr>
<tr>
<td>
            Luxemburgo
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Macedônia
          </td>
<td> 
                    8.522  
                  </td>
<td> 
                    17.172  
                  </td>
</tr>
<tr>
<td>
            Marrocos
          </td>
<td> 
                    603  
                  </td>
<td> 
                    2.349  
                  </td>
</tr>
<tr>
<td>
            México
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Moldávia
          </td>
<td> 
                    51.189  
                  </td>
<td> 
                    138.741  
                  </td>
</tr>
<tr>
<td>
            Montenegro
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Noruega
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Nova Zelândia
          </td>
<td> 
                    28.665  
                  </td>
<td> 
                    254.138  
                  </td>
</tr>
<tr>
<td>
            Países Baixos (Holanda)
          </td>
<td> 
                    9  
                  </td>
<td> 
                    354  
                  </td>
</tr>
<tr>
<td>
            Panamá
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Paraguai
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Peru
          </td>
<td> 
                    12.276  
                  </td>
<td> 
                    58.862  
                  </td>
</tr>
<tr>
<td>
            Porto Rico
          </td>
<td> 
                    2.021  
                  </td>
<td> 
                    4.481  
                  </td>
</tr>
<tr>
<td>
            Portugal
          </td>
<td> 
                    25.099.409  
                  </td>
<td> 
                    71.970.948  
                  </td>
</tr>
<tr>
<td>
            Reino Unido
          </td>
<td> 
                    1.808  
                  </td>
<td> 
                    32.757  
                  </td>
</tr>
<tr>
<td>
            Republica Dominicana
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Romênia
          </td>
<td> 
                    36.775  
                  </td>
<td> 
                    98.835  
                  </td>
</tr>
<tr>
<td>
            Rússia
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            San Marino
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Sérvia
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Síria
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Suazilândia
          </td>
<td> 
                    320  
                  </td>
<td> 
                    6.968  
                  </td>
</tr>
<tr>
<td>
            Suíça
          </td>
<td> 
                    2.109  
                  </td>
<td> 
                    101.111  
                  </td>
</tr>
<tr>
<td>
            Tcheca, República
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Tunísia
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Turquia
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Ucrânia
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Uruguai
          </td>
<td> 
                    2.905.567  
                  </td>
<td> 
                    9.276.001  
                  </td>
</tr>
<tr>
<td>
            Não consta na tabela
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Não declarados
          </td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>
            Outros
          </td>
<td>-</td>
<td>-</td>
</tr>
</tbody>
<tfoot class="tb_total">
<tr>
<td>
            Total
          </td>
<td>
            137.712.871
          </td>
<td>
            428.292.652
          </td>
</tr>
</tfoot>
</table>
<div class="tb_font">
      Fonte: C.I.E.F.  M.F. <br/> Elaboração: Loiva Maria Ribeiro de Mello  EMBRAPA/CNPUV <br/>
</div>
<table class="tb_base tb_link no_print">
<tr>
<td>
<a class="footer_content" href="download/ImpVinhos.csv" target="_blank">
<img alt="" height="16" src="figures/download.png" width="16"/>
<span class="spn_small">DOWNLOAD</span>
</a>
</td>
<td class="footer_right">
<a class="footer_content" href="#_top">
<img alt="" height="16" src="figures/topo.png" width="16"/>
<span class="spn_small">TOPO</span>
</a>
</td>
</tr>
</table>
</div>
</div>
</td>
<td> </td>
</tr>
</table>
<table class="tb_base">
<tr>
<td> </td>
<td class="col_center">
<table class="tb_base tb_footer">
<tr>
<td>
                Copyright © Embrapa Uva e Vinho. Todos os direitos reservados.<br/>
                Mais informações: <a class="footer_sac" href="https://www.embrapa.br/fale-conosco/sac">https://www.embrapa.br/fale-conosco/sac</a><br/>
                Última modificação: 21/12/23       
              </td>
<td class="footer_right">
                Rua Livramento 515, Caixa Postal 130<br/>
                95700-000 Bento Gonçalves, RS - Brasil<br/>
                Fone: (54) 3455-8000 - Fax: (54) 3451-2792
              </td>
</tr>
</table>
</td>
<td> </td>
</tr>
</table>
</body>
</html>"""
    return html


def expected_html2():
    return {'ano': 2023,
 'tipo': [{'pais': 'Africa do Sul', 'qtd': 522733, 'valor': 1732850},
          {'pais': 'Alemanha', 'qtd': 102456, 'valor': 557947},
          {'pais': 'Argélia', 'qtd': 0, 'valor': 0},
          {'pais': 'Arábia Saudita', 'qtd': 8, 'valor': 161},
          {'pais': 'Argentina', 'qtd': 25276991, 'valor': 83918138},
          {'pais': 'Armênia', 'qtd': 3542, 'valor': 24336},
          {'pais': 'Austrália', 'qtd': 432829, 'valor': 1568550},
          {'pais': 'Áustria', 'qtd': 16832, 'valor': 145475},
          {'pais': 'Bermudas', 'qtd': 6, 'valor': 879},
          {'pais': 'Bélgica', 'qtd': 0, 'valor': 0},
          {'pais': 'Bolívia', 'qtd': 1170, 'valor': 10920},
          {'pais': 'Bósnia-Herzegovina', 'qtd': 0, 'valor': 0},
          {'pais': 'Brasil', 'qtd': 6229, 'valor': 76894},
          {'pais': 'Bulgária', 'qtd': 40281, 'valor': 95232},
          {'pais': 'Canada', 'qtd': 14, 'valor': 1062},
          {'pais': 'Chile', 'qtd': 62358765, 'valor': 170146247},
          {'pais': 'China', 'qtd': 0, 'valor': 0},
          {'pais': 'Coreia do Sul, República', 'qtd': 0, 'valor': 0},
          {'pais': 'Croácia', 'qtd': 1107, 'valor': 9160},
          {'pais': 'Cuba', 'qtd': 8, 'valor': 261},
          {'pais': 'Emirados Árabes Unidos', 'qtd': 0, 'valor': 0},
          {'pais': 'Eslovênia', 'qtd': 28806, 'valor': 124283},
          {'pais': 'Eslováquia', 'qtd': 0, 'valor': 0},
          {'pais': 'Espanha', 'qtd': 6591628, 'valor': 20097228},
          {'pais': 'Estados Unidos', 'qtd': 244276, 'valor': 1775713},
          {'pais': 'França', 'qtd': 4899631, 'valor': 30421272},
          {'pais': 'Geórgia', 'qtd': 17173, 'valor': 29084},
          {'pais': 'Geórgia do Sul e Sandwich do Sul, Ilhas',
           'qtd': 0,
           'valor': 0},
          {'pais': 'Grécia', 'qtd': 45889, 'valor': 147724},
          {'pais': 'Hong Kong', 'qtd': 0, 'valor': 0},
          {'pais': 'Hungria', 'qtd': 41905, 'valor': 316481},
          {'pais': 'Indonésia', 'qtd': 0, 'valor': 0},
          {'pais': 'Irlanda', 'qtd': 0, 'valor': 0},
          {'pais': 'Israel', 'qtd': 48772, 'valor': 259405},
          {'pais': 'Itália', 'qtd': 8868133, 'valor': 34760596},
          {'pais': 'Japão', 'qtd': 86, 'valor': 3427},
          {'pais': 'Iugoslávia', 'qtd': 0, 'valor': 0},
          {'pais': 'Líbano', 'qtd': 14328, 'valor': 106610},
          {'pais': 'Luxemburgo', 'qtd': 0, 'valor': 0},
          {'pais': 'Macedônia', 'qtd': 8522, 'valor': 17172},
          {'pais': 'Marrocos', 'qtd': 603, 'valor': 2349},
          {'pais': 'México', 'qtd': 0, 'valor': 0},
          {'pais': 'Moldávia', 'qtd': 51189, 'valor': 138741},
          {'pais': 'Montenegro', 'qtd': 0, 'valor': 0},
          {'pais': 'Noruega', 'qtd': 0, 'valor': 0},
          {'pais': 'Nova Zelândia', 'qtd': 28665, 'valor': 254138},
          {'pais': 'Países Baixos (Holanda)', 'qtd': 9, 'valor': 354},
          {'pais': 'Panamá', 'qtd': 0, 'valor': 0},
          {'pais': 'Paraguai', 'qtd': 0, 'valor': 0},
          {'pais': 'Peru', 'qtd': 12276, 'valor': 58862},
          {'pais': 'Porto Rico', 'qtd': 2021, 'valor': 4481},
          {'pais': 'Portugal', 'qtd': 25099409, 'valor': 71970948},
          {'pais': 'Reino Unido', 'qtd': 1808, 'valor': 32757},
          {'pais': 'Republica Dominicana', 'qtd': 0, 'valor': 0},
          {'pais': 'Romênia', 'qtd': 36775, 'valor': 98835},
          {'pais': 'Rússia', 'qtd': 0, 'valor': 0},
          {'pais': 'San Marino', 'qtd': 0, 'valor': 0},
          {'pais': 'Sérvia', 'qtd': 0, 'valor': 0},
          {'pais': 'Síria', 'qtd': 0, 'valor': 0},
          {'pais': 'Suazilândia', 'qtd': 320, 'valor': 6968},
          {'pais': 'Suíça', 'qtd': 2109, 'valor': 101111},
          {'pais': 'Tcheca, República', 'qtd': 0, 'valor': 0},
          {'pais': 'Tunísia', 'qtd': 0, 'valor': 0},
          {'pais': 'Turquia', 'qtd': 0, 'valor': 0},
          {'pais': 'Ucrânia', 'qtd': 0, 'valor': 0},
          {'pais': 'Uruguai', 'qtd': 2905567, 'valor': 9276001},
          {'pais': 'Não consta na tabela', 'qtd': 0, 'valor': 0},
          {'pais': 'Não declarados', 'qtd': 0, 'valor': 0},
          {'pais': 'Outros', 'qtd': 0, 'valor': 0},
          {'pais': 'Total', 'qtd': 137712871, 'valor': 428292652}],
 'titulo': 'Importação de vinhos de mesa',
 'total': 137712871}