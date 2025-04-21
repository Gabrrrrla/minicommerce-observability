# MiniCommerce with Observability

This is an educational project for a simplified e-commerce application called **MiniCommerce**, created to demonstrate in practice the three pillars of observability in a microservices architecture: Logging, Tracing, and Monitoring.

## Objective

To explore observability concepts in a modern architecture using microservices. The project currently contains only a product catalog microservice, but it's structured to easily include future services like shopping cart, payment, and authentication.

## Technologies and Tools

| Pillar        | Tool                            | Description                                     |
|---------------|---------------------------------|-------------------------------------------------|
| Logging       | Python logging                  | Outputs structured logs to the terminal         |
| Tracing       | OpenTelemetry + Jaeger          | Traces HTTP requests between services           |
| Monitoring    | Prometheus + Grafana            | Collects and visualizes service metrics         |
| Web Framework | FastAPI                         | Async web framework for building APIs           |
| Runtime       | Uvicorn                         | High-performance ASGI server                    |
| Containers    | Docker + Docker Compose         | Manages observability tools and services        |

## 1. Getting started
Clone the repository
cd mini-observability

cd catalog_service
pip install -r requirements.txt

docker-compose up

cd catalog_service
uvicorn main:app --host 0.0.0.0 --port 8000
