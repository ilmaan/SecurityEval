from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/change_email")
async def change_email(new_email: str = Form(...)):
    # Change email without CSRF protection
    return {"message": f"Email changed to {new_email}"}

@app.get("/", response_class=HTMLResponse)
async def get_form():
    return "