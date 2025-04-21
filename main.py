from fastapi import FastAPI, Request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

# Define o contador de requisições
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total de requisições HTTP",
    ["method", "endpoint", "http_status"]
)

# Middleware para capturar métricas
@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    response = await call_next(request)

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        http_status=response.status_code
    ).inc()

    return response

# Endpoint de métricas para o Prometheus coletar
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Endpoint de exemplo
@app.get("/produto/{produto_id}")
def read_produto(produto_id: int):
    return {"produto_id": produto_id}
