from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()

@router.get("/feed")
def get_feed(cursor: Optional[str] = None, limit: int = Query(20, le=100)):
    """Cursor-based paginated feed endpoint."""
    # TODO: query DB with cursor
    return {
        "items": [],
        "next_cursor": None,
        "has_more": False
    }
