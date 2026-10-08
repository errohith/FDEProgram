# Postman collections

Import the JSON files under `collections/` into Postman with **Import → File**.
Each collection is independent and has a `baseUrl` variable where applicable.

## Local APIs

Run each service from its indicated directory in a separate terminal:

| Collection | Command | Base URL |
| --- | --- | --- |
| Invoice Manager API | `cd invoicecrudOperation && uvicorn main:app --reload` | `http://127.0.0.1:8000` |
| Employee API | `cd fastApi && uvicorn main:app --reload --port 8001` | `http://127.0.0.1:8001` |
| FDE Week 1 Health API | `cd src && uvicorn app:app --reload --port 8002` | `http://127.0.0.1:8002` |

The Invoice Manager collection contains its health check and all five invoice
CRUD requests. The Employee collection contains all routes registered by
`fastApi/main.py`. The health collection targets the separate app in `src`.

## External API

The JSONPlaceholder Users collection calls
`https://jsonplaceholder.typicode.com/users` directly; no local service is
needed.
