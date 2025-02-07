from fastapi import FastAPI,HTTPException, status
from pydantic import BaseModel

description = "API desenvolvida durante a aula de Construção de APIs para IA2"

app = FastAPI(
 title="Aula",
 description=description,
 summary="API desenvolvida durante a aula de Construção de APIs para IA.",
 version="0.1",
 terms_of_service="http://example.com/terms/",
 contact={
 "name": "Flaeuso  ",
 "url": "http://github.com/rogerior/",
 "email": "a@b.com",
 },
 license_info={
 "name": "Apache 2.0",
 "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
 },
)


@app.get("/teste", tags=["Area de testes"],
         summary="Retorna mensagem de teste",
         description="Retorna uma mensagem de teste para verificar se a API está funcionando corretamente"
         )
def hello_world():
 return {"mensagem": " Hello World"}

#Criando um endpoint para receber dois números e retornar a
# Passando o número 1 e 2 na URL
@app.get(
        path="/soma/{numero1}/{numero2}",
        summary="Retorna a soma de dois numeros",
        description="Recebe dois números e retorna a soma deles os numetos devem ser passados na URL /1/2",
        tags=["Operações Matemáticas"]
    ) 
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    if total < 0:
            raise HTTPException(status_code=400, detail="Resultadonegativo")
    return {"resultado": total}
  

# Passando o número 1 e 2 no corpo da requisição
@app.post(
        path="/soma_formato2",
        summary="Retorna a soma de dois numeros",
        description="Recebe dois números e retorna a soma deles os numetos devem ser passados No Corpo da requisição",
        tags=["Operações Matemáticas"]      
      )
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}

# Passando o número 1 e 2 no corpo da requisição
from pydantic import BaseModel
class Numeros(BaseModel):
    numero1: int
    numero2: int
@app.post(
        path="/soma_formato3",
        summary="Retorna a soma de dois numeros",
        description="Recebe dois números e retorna a soma deles os numetos devem ser passados No Corpo HTML da requisição",
        tags=["Operações Matemáticas"],
        response_model=Numeros,
        status_code=status.HTTP_200_OK
         )
def soma_formato3(numeros: Numeros):
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}
