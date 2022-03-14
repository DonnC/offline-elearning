from fastapi import APIRouter, UploadFile, Request
from fastapi.responses import HTMLResponse

import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Callable

#from ..dependencies import get_token_header

router = APIRouter(
    prefix="/files",
    tags=["files"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path

@router.post("/uploadfile/")
def create_upload_file(file: UploadFile, request: Request):
    # return path
    # ! save file and return full file url
    url = request.url_for(file.filename)
    return {"filename": file.filename}

@router.post("/uploadfiles/")
def create_upload_files(files: list[UploadFile]):
    tmp_path = save_upload_file_tmp(files[0])

    try:
        handler(tmp_path)  # Do something with the saved temp file
    finally:
        tmp_path.unlink()  # Delete the temp file
    # return {"filenames": [file.filename for file in files]}

@router.get("/")
async def main():
    content = """
            <body>
                <form action="/files/" enctype="multipart/form-data" method="post">
                    <input name="files" type="file" multiple>
                    <input type="submit">
                </form>
                
                <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                    <input name="files" type="file" multiple>
                    <input type="submit">
                </form>
            </body>
    """
    return HTMLResponse(content=content)

'''
@app.post("/create_file/")
async def image(image: UploadFile = File(...)):
    print(image.file)
    # print('../'+os.path.isdir(os.getcwd()+"images"),"*************")
    try:
        os.mkdir("images")
        print(os.getcwd())
    except Exception as e:
        print(e) 
    file_name = os.getcwd()+"/images/"+image.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(image.file.read())
        f.close()
   file = jsonable_encoder({"imagePath":file_name})
   new_image = await add_image(file)
   return {"filename": new_image}



---------------------------------
import uvicorn
from fastapi import File, UploadFile, FastAPI
from typing import List

app = FastAPI()


def save_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):

    # in case you need the files saved, once they are uploaded
    for file in files:
        contents = await file.read()
        save_file(file.filename, contents)

    return {"Uploaded Filenames": [file.filename for file in files]}
    

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)


-----------------------------

 return JSONResponse({
        #"root_path": request.scope['root_path'],
        #"raw_path": request.scope['raw_path'],
        #"path": request.scope['path'],
        "req_url_for": request.url_for("read_sub"),
        "app_url_for": app.url_path_for("read_sub"),
        "subapp_url_for": subapp.url_path_for("read_sub"),
    })

--------------------------------
@app.post("/upload-file/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"files/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}
'''