from recipes.schemas.recipe import RecipeIn
from tests.factories import recipe_data


def test_schemas_return_success():
    data = recipe_data()
    recipe = RecipeIn.model_validate(data)

    # Verifica se o nome é "Estela"
    assert recipe.nome_refeicao == "Almoco"
