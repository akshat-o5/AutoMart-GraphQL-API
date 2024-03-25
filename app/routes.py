from fastapi import APIRouter, Request
from strawberry.asgi import GraphQL
from .schema import schema

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to the Second Hand Automobiles GraphQL API"}

@router.post("/graphql")
async def graphql(request: Request):
    # Create a GraphQL ASGI application
    graphql_app = GraphQL(schema, debug=True)

    # Pass the receive and send events from the request
    response = await graphql_app(request.scope, request.receive, request._send)
    return response
