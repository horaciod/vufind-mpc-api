from mcp.server.fastmcp import FastMCP
# desarrollo para Bibliotecas UNCuyo
import requests
# create the mcp server
mcp = FastMCP("Vufind-api2")

@mcp.tool()

def get_recordsuncuyo(query, filter=None):
    """Buscar libros en el explorador de registros de Bibliotecas Uncuyo y muestra los enlaces al registro y el autor . Identificar si query tiene más de una palabra y si es así, buscar en el campo de título. Si no hay resultados, devolver None. Si hay resultados, devolver una lista de diccionarios con el título, la url y el autor.
    el filtro es opcional y se puede usar para filtrar los resultados por autor, tema, etc. Si no se proporciona un filtro, se buscará en todos los campos.
        
    """
    
    search_url ="https://bibliotecas.uncuyo.edu.ar/explorador3/api/v1/search" 

    search_params = {
        # "action": "query",
        # "list": "search",
        "type": "AllFields",
        "sort": "relevance",
        "page": 1,
        "prettyPrint": "false",
        "lng": "es",
        "facet[]": ["author_facet", "genre_facet", "topic_facet", "publishDate", "format"],
        "field[]": ["id", "authors", "formats", "series", "subjects", "title", "urls", "languages", "publishDate"],
        "lookfor": query,
        "limit":10  # Get multiple results in case the first is a disambiguation page
    }
    # pasar el agent en el request 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    # make the request
    response = requests.get(search_url, params=search_params, headers=headers)
   
    #get the url of response 
    # print the url of the response
    #print(response.url)
    if response.status_code != 200:
     #   print(f"Error: {response.status_code}")
        return None
    # dump the response.json() to console
   # print(response.json())

    data = response.json()
    
    if "records" not in data:
        return None

   
    if not data["status"]:
      #  print('no hay status')
        return None  # No results found
    results = []
    # Get the first non-disambiguation result
    for result in data["records"]:
        #if "may refer to" not in result["snippet"]:  # Avoid disambiguation pages
            results.append({"title": result["title"] ,"url":"https://bibliotecas.uncuyo.edu.ar/explorador3/Record/" + result["id"], "authors": result["authors"]})
 
    return results

@mcp.tool()
def get_recordssrnd(query):
    """Buscar libros en el explorador de registros del Sistema nacional de Repostorios digitales de la Argentina que contiene registros de todos los repositorios digitales  muestra los enlaces al registro y el autor . Identificar si query tiene más de una palabra y si es así, buscar en el campo de título. Si no hay resultados, devolver None. Si hay resultados, devolver una lista de diccionarios con el título, la url y el autor."""
    # https://vufind.org/advanced_demo/api/v1/search?lookfor=argentina&facet[]=author_facet&facet[]=genre_facet&facet[]=topic_facet&facet[]=publishDate&facet[]=format&field[]=id&field[]=authors&field[]=formats&field[]=series&field[]=subjects&field[]=title&field[]=urls&field[]=languages&field[]=fullRecord&field[]=publishDate&type=AllFields&sort=relevance&page=1&limit=20&prettyPrint=false&lng=en
    search_url ="https://repositoriosdigitales.mincyt.gob.ar/vufind/api/v1/search" 
    #"https://vufind.org/advanced_demo/api/v1/search"
    search_params = {
        # "action": "query",
        # "list": "search",
        "type": "AllFields",
        "sort": "relevance",
        "page": 1,
        "prettyPrint": "false",
        "lng": "es",
        "facet[]": ["author_facet", "genre_facet", "topic_facet", "publishDate", "format"],
        "field[]": ["id", "authors", "formats", "series", "subjects", "title", "urls", "languages", "publishDate"],
        "lookfor": query,
        "limit":10  # Get multiple results in case the first is a disambiguation page
    }
    # pasar el agent en el request 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    # make the request
    response = requests.get(search_url, params=search_params, headers=headers)
   
    #get the url of response 
    # print the url of the response
    #print(response.url)
    if response.status_code != 200:
     #   print(f"Error: {response.status_code}")
        return None
    # dump the response.json() to console
   # print(response.json())

    data = response.json()
    
    if "records" not in data:
        return None

   
    if not data["status"]:
      #  print('no hay status')
        return None  # No results found
    results = []
    # Get the first non-disambiguation result
    for result in data["records"]:
        #if "may refer to" not in result["snippet"]:  # Avoid disambiguation pages
        
            results.append({"title": result["title"] ,"url":"https://repositoriosdigitales.mincyt.gob.ar/vufind/Record/" + result["id"], "authors": result["authors"] ,'urls': result["urls"]})
 
    return results


@mcp.tool()
def function(input):
   """prompt"""
   
   call_external_apis()
   connect_to_external_datasource()
   other_features()
  
   return output
if __name__ == "__main__":
    print( 'buscando...')
    resultados = get_recordsuncuyo("olivo")
    print(resultados)
    # Run the server
    # mcp.run() 