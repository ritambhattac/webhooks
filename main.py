from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/webhook")
def check_payload(payload: dict):
    if "after" in payload:
        return {"data": "there was a push event"}
    else:
        raise HTTPException(status_code=400, detail="unable to get payload")


@app.get("/test")
def test():
    return {"data": "hello!"}
