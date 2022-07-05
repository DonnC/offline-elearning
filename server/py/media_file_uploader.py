# main media file uploader
from os import path, makedirs, remove
import platform

from fastapi import Request, UploadFile

STATIC_DIR = "static"

async def delete_file(resource_path: str) -> bool:
    '''
        delete resource at given path
    '''
    _resource_path = resource_path.replace('/', '\\')

    res = path.join(STATIC_DIR, _resource_path)
    
    if path.isfile(res):
        try:
            remove(res)
            return True
        
        except:
            return False

    return False

async def save_upload_file(upload_file: UploadFile, resource_path: str, request: Request):
    '''
        save the uploaded course file name to resource_path dir
        upload_file: File obj received
        resource_path | resource_path: [str] - course path to save file to e.g 
                           - form4/biology/images/intro/img.png
                           - form4/biology/videos/intro/vid.mp4
                           - form4/biology/intro/chapter1/images/img.jpg

        return dict 
        {
            'filename': '',
            'filepath': '',
            'url': '',
        }

        TODO: Use mounted drive as file path
              Only save file path without base url

        import shutil
        shutil.copy(src="C:/Test/Original.txt", dst="F:/Original.txt")  
    '''
    print(upload_file.filename)
    print("[UPLOAD] Resource path: ", resource_path)

    _resource_path = resource_path

    # check platform
    if platform.system() == 'Windows':
        _resource_path = resource_path.replace('/', '\\')

    _path_dir = path.join(STATIC_DIR, _resource_path)

    if not path.isdir(_path_dir):
        makedirs(_path_dir)

    print("[UPLOAD] Dir path: ", _path_dir)

    file_path = path.join(_resource_path, upload_file.filename)

    file_location = path.join(_path_dir , upload_file.filename)

    with open(file_location, "wb+") as file_object:
        file_object.write(upload_file.file.read())

    _f_path = file_path.replace('\\', '/')

    file_url = request.url_for(STATIC_DIR, path=_f_path)

    print('File url: ', file_url)

    return {
        'filename': upload_file.filename,
        'filepath': _f_path,
        'url': file_url
    }