from fastapi import FastAPI

app = FastAPI(title="Task API")

items = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a REST API", "done": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


# TODO: create routes to list items
# TODO: create route to get one item by id
# TODO: create route to add an item
# TODO: create route to update an item
# TODO: create route to delete an item
