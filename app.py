import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/info/{query}")
def info(query: str):
    return {"detail": f"Look at this {query}"}


@app.post("/info/add")
async def add_info(req: Request):
    data = await req.json()
    return {"detail": f"Look at that {data['resource']}", "msg":"added resource"}

if __name__ == "__main__":
    # Runs the FastAPI application only if the app.py file is being run.
    print('Starting server at port 8000')
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)