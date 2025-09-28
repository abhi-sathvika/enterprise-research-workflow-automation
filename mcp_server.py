from fastapi import FastAPI

app = FastAPI()


@app.get("/tools")
def list_tools():
    '''
    Handles GET requests to the /tools endpoint.
    '''
    
    return {
        "tools": [
            {"name": "get_emails", "description": "Fetches emails"}, 
            {"name": "create_ticket", "description": "Creates a ServiceNow Ticket"}
        ]
    }
    
    
@app.get("/run_tool/{name}")
def run_tool(name: str):
    if name == "get_emails":
        return {"emails": ["Email-1", "Email-2"]}
    elif name == "create_ticket":
        return {"status": "Ticket Created"}
    else:
        return {"error": "Tool Not Found"}

