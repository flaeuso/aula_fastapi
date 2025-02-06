from fastapi import FastAPI
app = FastAPI()

@app.get("/teste")
def hello_world():
 return {"mensagem": " Hello World"}
