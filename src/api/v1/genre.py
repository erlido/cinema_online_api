from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4, BaseModel

from src.services.genre import GenreService, get_genre

router = APIRouter()


class Genre(BaseModel):
    id: str
    name: str


@router.get('/', response_model=list[Genre])
async def get_genres(
        genre_service: GenreService = Depends(get_genre)
) -> list[Optional[Genre]]:
    genres = await genre_service.get_list()
    if not genres:
        return []
    genres = [Genre(uuid=genre.id, name=genre.name) for genre in genres]
    return genres


@router.get('/{genre_id}', response_model=Genre)
async def get_genre_by_id(
        genre_id: str,
        genre_service: GenreService = Depends(get_genre)
):
    genre = await genre_service.get_by_id(genre_id)
    if not genre:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='genre not found')
    genre = Genre(id=genre.id, name=genre.name)
    return genre
