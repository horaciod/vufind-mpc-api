# Vufind-mpc-api
 MCP (Model Context Protocol) para acceder a la api de Vufind. 
tiene dos tools 
- getrecordsuncuyo 
- get_recordssrnd (trae registros desde https://repositoriosdigitales.mincyt.gob.ar/vufind/)

###basado en $ git clone https://github.com/zzaebok/mcp-wikidata.git

###desarrollado en Python

usar npx @modelcontextprotocol/inspector para depurar 

- instalar mcp
 pip install mcp[cli]

###Setting para Claude desktop

```
  "myvuf": {
            "type": "stdio",
            "command": "mcp",
            "args": [
                "run" ,
                "<ruta completa>/vufind-mcp.py"
            ]
        }
    
  }
```