from fastapi import APIRouter, UploadFile, Request
from typing import List

from media_file_uploader import save_upload_file

# from ..dependencies import get_token_header

router = APIRouter(
    prefix="/files",
    tags=["files"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# ! pass course and section id instead of name
# get name from fetched course | section id
@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile, resource_path: str, request: Request):
    saved_file = await save_upload_file(
        upload_file=file, request=request, resource_path=resource_path
    )

    return {
        "url": saved_file,
        "filename": file.filename,
    }



@router.post("/uploadfiles/")
async def create_upload_files(
    files: List[UploadFile], resource_path: str, request: Request
):

    saved_files = []

    try:
        for file in files:
            saved_file = await save_upload_file(
                upload_file=file, request=request, resource_path=resource_path
            )

            saved_files.append(
                {
                    "url": saved_file,
                    "filename": file.filename,
                }
            )

        return saved_files

    except Exception as err:
        print("[Multiple Upload] Error: ", err)