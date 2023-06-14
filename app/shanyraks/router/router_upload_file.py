from fastapi import Depends, UploadFile, Response
from typing import List

from ..service import Service, get_service
from . import router
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

#@router.post("/file")
#def upload_file(
#    file: UploadFile,
#    svc: Service = Depends(get_service),
#):
#    """
#    file.filename: str - Название файла
#    file.file: BytesIO - Содержимое файла
#    """
#    url = svc.s3_service.upload_file(file.file, file.filename)
#    
#    return {"msg": url}

@router.post("/{id}/media")
def upload_files(
    user_id: str,
    shanyrak_id: str,
    files: List[UploadFile],
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    """
    file.filename: str - Название файла
    file.file: BytesIO - Содержимое файла
    """
    
    if (jwt_data.user_id == user_id):
        result = []
        for file in files:
            url = svc.s3_service.upload_file(shanyrak_id, file.file, file.filename)
            result.append(url)
        
        media = {"media": result}
        svc.repository.push_media_to_shanyrak(shanyrak_id, media)
        return Response(status_code=200, content=str(result))