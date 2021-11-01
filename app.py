import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from utils.models import CategorizerModel

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

model = CategorizerModel()

@app.get("/model/metric")
def get_metric():
    return {"accuracy": f"{model.metric}"}


@app.post("/model/predict")
async def predict_category(req: Request):
    data = await req.json()
    return {"category": model.predict_category(data['text'])}

@app.post("/model/train")
async def predict_category(req: Request):
    data = await req.json()
    return model.train_model(data['text'],data['label'])

if __name__ == "__main__":
    # Runs the FastAPI application only if the app.py file is being run.
    print('Starting server at port 8000')
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)