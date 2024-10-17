from pydantic import Field, EmailStr  # type: ignore
from recipes.schemas.base import BaseSchemaMixin


class UserIn(BaseSchemaMixin):
    username: str = Field(..., description="Nome usuário")
    email: EmailStr
    data_nascimento: str = Field(..., description="Data Nascimento")
    senha: str = Field(..., description="Senha")
    status: bool = Field(..., description="User status")


class UserPublic(BaseSchemaMixin):
    username: str = Field(..., description="Nome usuário")
    email: EmailStr
    data_nascimento: str = Field(..., description="Data Nascimento")
    status: bool = Field(..., description="User status")
