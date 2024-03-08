from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post("/webhook")
def check_payload(payload: dict):
    if "after" in payload:
        print(payload)
        return {"data": "there was a push event"}


    raise HTTPException(status_code=400, detail="unable to get payload")


@app.get("/test")
def test():
    return {"data": "hello!"}
