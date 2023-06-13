from fastapi import Depends, Response, status

from ..service import Service, get_service
from . import router

@router.delete("/{id}", status_code = 200)
def delete_shanyrak(
    user_id: str,
    shanyrak_id: str,
    svc: Service = Depends(get_service)
) -> dict[str, str]:
    svc.repository.delete_shanyrak(user_id, shanyrak_id)
    return Response(status_code = 200)