from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from openai_functions_agent import agent_executor as openai_functions_agent_chain
from langserve import add_routes

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


add_routes(app, openai_functions_agent_chain, path="/openai-functions-agent")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
