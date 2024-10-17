from datetime import datetime
from pydantic import BaseModel, Field  # type: ignore


class BaseSchemaMixin(BaseModel):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(default_factory=datetime.utcnow)


class UserPublic(BaseModel):
    userusername: str
    email: str
