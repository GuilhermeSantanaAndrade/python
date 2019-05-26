import requests as req

class IdInvalida(Exception):
     def __init__(self, message):
         self.message = message

api_key = '72f5c0f2'

def busca_por_id(film_id):
 url = "http://www.omdbapi.com/?apikey={}&i={}".format(api_key, film_id)
 retorno = req.get(url).json()
 return retorno

def busca_por_texto(texto_buscar, page = 1, type_title = ''):
 url = "http://www.omdbapi.com/?apikey={}&s={}&page={}".format(api_key, texto_buscar, str(page))
 if type_title != '':
     url = url + "&type={}".format(type_title)
 retorno = req.get(url).json()
 return retorno


def busca_qtd_total(texto_buscar, type_title = ''):
 print('Processando Aguarde (busca_qtd_total)...')
 page = 0
 totalizador = 0
 while True:
   page += 1
   json = busca_por_texto(texto_buscar, page, type_title)
   if json['Response'] == "True":
       totalizador += len(json['Search'])
   else:
       break
 return totalizador   
 
def busca_qtd_filmes(texto_buscar):
 return busca_qtd_total(texto_buscar, 'movie')


def busca_qtd_jogos(texto_buscar):
 return busca_qtd_total(texto_buscar, 'game')


def nome_do_filme_por_id(id_filme):
 json = busca_por_id(id_filme) 
 if json['Response'] == 'True':
   return json['Title']

 return ''


def ano_do_filme_por_id(id_filme):
 json = busca_por_id(id_filme) 
 if json['Response'] == 'True':
   return json['Year']

 return ''

def dicionario_do_filme_por_id(id_filme):
 new_dicionario = {"ano": 0, "nome": '', "diretor": '', "genero": ''}
 json = busca_por_id(id_filme)
 if json['Response'] == 'True':
    new_dicionario['ano'] = json['Year']
    new_dicionario['nome'] = json['Title']
    new_dicionario['diretor'] = json['Director']
    new_dicionario['genero'] = json['Genre']
    new_dicionario['poster'] = json['Poster']
    new_dicionario['nota_rotten_tomatoes'] = int(json['Ratings'][1]['Value'].replace('%','')) / 100
    new_dicionario['nota_metacritic'] = int(json['Metascore']) / 100
    new_dicionario['nota_imdbRating'] = float(json['imdbRating']) / 10
    new_dicionario['nota_media'] = (new_dicionario['nota_rotten_tomatoes'] + new_dicionario['nota_metacritic'] + new_dicionario['nota_imdbRating']) / 3
    
 else:
     raise IdInvalida('')

 return new_dicionario
 

def busca_filmes(texto_buscar):
 resposta = []
 json = busca_por_texto(texto_buscar, 1)
 if json['Response'] == 'True':
     for item in json['Search']:
         resposta.append({"nome":item['Title'], "ano":item['Year']})
 return resposta


def busca_filmes_grande(texto_buscar):
 print('Processando Aguarde (busca_filmes_grande)...')
 resposta = []
 page = 0
 while True:
   page += 1
   json = busca_por_texto(texto_buscar, page, 'movie')
   if json['Response'] == 'True':
       for item in json['Search']:
           resposta.append({"nome":item['Title'], "ano":item['Year']})
           if len(resposta) >= 20:
             break;
       if len(resposta) >= 20:
         break;
   else:
       break
 return resposta

def conta_tipos_de_midia_para_busca(texto_buscar):
 new_dicionario = {}
 json = busca_por_texto(texto_buscar)
 if json['Response'] == 'True':
     for item in json['Search']:
         if item['Type'] == 'movie':
             try:
               new_dicionario['movie'] += 1
             except:
               new_dicionario['movie'] = 1  
         elif item['Type'] == 'series':
             try:
               new_dicionario['series'] += 1
             except:
               new_dicionario['series'] = 1
         elif item['Type'] == 'game':
             try:
               new_dicionario['game'] += 1
             except:
               new_dicionario['game'] = 1                 
 return new_dicionario

def id_do_mais_velho(texto_buscar):
 json = busca_por_texto(texto_buscar, 1)
 menorAno = 9999
 id_menor = None
 if json['Response'] == 'True':
   for item in json['Search']:
       if int(item['Year']) < int(menorAno):
           menorAno = item['Year']
           id_menor = item['imdbID']

 return id_menor

def ids_dos_tres_primeiros(texto_buscar):
 json = busca_por_texto(texto_buscar, 1)
 idx  = 1
 resposta = []
 
 if json['Response'] == 'True':
   for item in json['Search']  :
       resposta.append(item['imdbID'])
       idx += 1
       if idx > 3:
           break       

 return resposta
 
def mais_bem_avaliado_dos_3_primeiros(texto_buscar):
 print('Processando Aguarde (mais_bem_avaliado_dos_3_primeiros)...') 
 lista = ids_dos_tres_primeiros(texto_buscar)
 nota = -9999.99
 for item in lista:
     detalhe = busca_por_id(item)
     if float(detalhe['imdbRating']) > nota:
         nota = float(detalhe['imdbRating'])
 
 if nota == -9999.99:
     nota = 0
 return nota

def baixar_poster(id_filme):
 url = "http://img.omdbapi.com/?apikey={0}&i={1}".format(api_key, id_filme)
 retorno = req.get(url)
 arquivo = open("Poster.jpg", "wb")
 arquivo.write(retorno.content)
 arquivo.close()
 
 status = retorno.status_code
 if status != 200:
     return 'id inválida'
 else:
     return 'id válida'
 
import unittest
class TestStringMethods(unittest.TestCase):
    def test_000_qdt_total(self):
     self.assertTrue(439 * 0.9 < int(busca_qtd_total('star wars')) < 439 * 1.1)
     self.assertTrue(283 * 0.9 < int(busca_qtd_total('star trek')) < 283 * 1.1)
    
    def test_001_qdt_filmes(self):
     self.assertTrue(305 * 0.9 < int(busca_qtd_filmes('star wars')) < 305 * 1.1)
     self.assertTrue(186 * 0.9 < int(busca_qtd_filmes('star trek')) < 186 * 1.1)
     self.assertTrue(111 * 0.9 < int(busca_qtd_filmes('menace')) < 1.1 * 111)
     self.assertTrue(964 * 0.9 < int(busca_qtd_filmes('future')) < 964 * 1.1)
    
    def test_002_qdt_jogos(self):
     self.assertTrue(96 * 0.9 < int(busca_qtd_jogos('star wars')) < 1.1 * 96)
     self.assertTrue(55 * 0.9 < int(busca_qtd_jogos('star trek')) < 1.1 * 55)
     self.assertTrue( 8 * 0.8 < int(busca_qtd_jogos('menace')) < 1.2 * 8)
     self.assertTrue(34 * 0.9 < int(busca_qtd_jogos('future')) < 1.1 * 34)

    def test_003_nome_do_filme_por_id(self):
     self.assertEqual(nome_do_filme_por_id('tt0796366'), 'Star Trek')
     self.assertEqual(nome_do_filme_por_id('tt0861739'), 'Elite Squad')
    
    def test_004_ano_do_filme_por_id(self):
     self.assertEqual(ano_do_filme_por_id('tt0076759'), '1977')
     self.assertEqual(ano_do_filme_por_id('tt1211837'), '2016')
    
    def test_005_dicionario_filme_por_id(self):
     d1 = dicionario_do_filme_por_id('tt0076759')
     self.assertTrue(type(d1) is dict)
     self.assertEqual(d1['ano'], '1977')
     self.assertEqual(d1['diretor'], 'George Lucas')
     self.assertTrue('Action' in d1['genero'])
     d2 = dicionario_do_filme_por_id('tt1211837')
     self.assertTrue(type(d2) is dict)
     self.assertEqual(d2['ano'], '2016')
     self.assertEqual(d2['nome'], 'Doctor Strange')
     self.assertTrue('Fantasy' in d2['genero'])
    
    def test_006_busca(self):
     resposta = busca_filmes('star wars')
     self.assertEqual(len(resposta),10)
     achei = False
    
     for filme in resposta:
       if int(filme['ano']) == 1977:
         achei = True
       if 'ano' not in filme:
         self.fail('Ano não encontrado')
       if 'nome' not in filme:
         self.fail('Nome não encontrado')
       if not achei:
         self.fail('Filme "A New Hope" não encontrado')
     
    def test_007_busca_grande(self):
     resposta = busca_filmes_grande('star wars')
     self.assertEqual(len(resposta), 20)
     achei = False
     for filme in resposta:
       if int(filme['ano']) == 1977:
         achei = True
       if 'ano' not in filme:
         self.fail('Ano não encontrado.')
       if 'nome' not in filme:
         self.fail('Nome não encontrado.')
       if not achei:
         self.fail('Filme "A New Hope" não encontrado.')
     
    def test_008_dicionario_filme_por_id_tem_poster(self):
     resposta = dicionario_do_filme_por_id('tt0796366')
     self.assertTrue(
     "MV5BMjE5NDQ5OTE4Ml5BMl5BanBnXkFtZTcwOTE3NDIzMw@@._V1_SX300.jpg" in
     resposta['poster'])
     
    def test_009_tenta_montar_dicionario_para_id_invalida(self):
     try:
       dicionario_do_filme_por_id('tt0796366naoao')
     except IdInvalida:
       print('Ok, você levantou a exceção desejada.')
     except:
       self.fail('Você levantou uma exceção diferente.')
     else:
       self.fail('Você não levantou exceção.')
     
    def test_010_dicionario_tem_nota_rotten_tomatoes(self):
     resposta = dicionario_do_filme_por_id('tt0796366')
     self.assertTrue(0.92 < resposta['nota_rotten_tomatoes'] < 0.96)
     resposta = dicionario_do_filme_por_id('tt0861739')
     self.assertTrue(0.51 < resposta['nota_rotten_tomatoes'] < 0.55)
     
    def test_011_dicionario_tem_nota_metacritic(self):
     resposta = dicionario_do_filme_por_id('tt0796366')
     self.assertTrue(0.8 < resposta['nota_metacritic'] < 0.84)
     resposta = dicionario_do_filme_por_id('tt0861739')
     self.assertTrue(0.3 < resposta['nota_metacritic'] < 0.35)

    def test_012_dicionario_tem_nota_media(self):
     resposta = dicionario_do_filme_por_id('tt0796366')
     self.assertTrue(0.81 < resposta['nota_media'] < 0.89)
     resposta = dicionario_do_filme_por_id('tt0861739')
     self.assertTrue(0.51 < resposta['nota_media'] < 0.59)
     
    def test_013_conta_tipos_de_midia_para_busca(self):
     d1 = conta_tipos_de_midia_para_busca('menace')
     self.assertEqual(d1, {'movie': 8, 'series': 2})
     d1 = conta_tipos_de_midia_para_busca('grim fandango')
     self.assertEqual(d1, {'game': 2})     
     
    def test_014_id_do_mais_velho(self):
     self.assertEqual(id_do_mais_velho('star wars'), 'tt0076759')
     self.assertEqual(id_do_mais_velho('grim fandango'), 'tt0177822')
    
    def test_015_ids_dos_tres_primeiros(self):
     lista = ids_dos_tres_primeiros('star wars')
     self.assertTrue('tt0076759' in lista)
     self.assertTrue('tt0080684' in lista)
     self.assertTrue('tt0086190' in lista)
    
    def test_016_mais_bem_avaliado(self):
     self.assertEqual(mais_bem_avaliado_dos_3_primeiros('star wars'), 8.8)
    
    def test_017_poster_invalida(self):
     resposta = baixar_poster('tt0796366naoao')
     self.assertEqual(resposta, 'id inválida')
     resposta = baixar_poster('bonde')
     self.assertEqual(resposta, 'id inválida')
     resposta = baixar_poster('blackkamenrider')
     self.assertEqual(resposta, 'id inválida')
    
    def test_018_poster_valida(self):
     resposta = baixar_poster('tt0796366')
     self.assertEqual(resposta, 'id válida')     
    
def runTests():
     suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
     unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

if __name__ == "__main__":
 runTests()