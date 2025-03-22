from fastapi import FastAPI 
from fastapi import UploadFile
from fastapi import HTTPException
from app.utils.helper import size_in_mb,create_folder
from app.enums.docconstants import DocConstants
import os 


app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello World"}

@app.post("/api/upload")
async def upload_file(file:UploadFile):
    if file.filename.endswith((".pdf",".txt")) and size_in_mb(file.size)<20:
        create_folder(DocConstants.UPLOAD_DIR.value)
        with open(os.path.join(DocConstants.UPLOAD_DIR.value,file.filename),"wb") as f:
            content = await file.read()
            f.write(content)
        return {"message":f"Succefully Uploaded file {file.filename}"}
    else:
        raise HTTPException(status_code=400,detail="Invalid File Type")


        
        
