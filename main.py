from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
temp = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def calcu(request: Request):
    return temp.TemplateResponse("index.html", {"request": request, "title": "My Calculator"})

@app.post("/", response_class=HTMLResponse)
async def result(req: Request, fnum: int = Form(...), math: str = Form(...), snum: int = Form(...)):
    if math == "+":
        ans = fnum + snum
    elif math == "-":
        ans = fnum - snum
    elif math == "/":
        ans = fnum / snum
    elif math == "*":
        ans = fnum * snum
    else:
        ans = "Invalid Operation"

    return temp.TemplateResponse("index.html", {"request": req, "answer": ans, "title": "My Calculator"})