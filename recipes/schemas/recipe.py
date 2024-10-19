from recipes.schemas.base import BaseSchemaMixin


class RecipeIn(BaseSchemaMixin):
    nome_refeicao: str
    nome_receita: str
    nome_categoria: str
    quantidade: str
    kcal: int
    dia_semana: str
