from recipes.schemas.user import UserIn
from tests.factories import user_data


def test_schemas_return_success():
    data = user_data()
    user = UserIn.model_validate(data)

    # Verifica se o nome é "Estela"
    assert user.username == "Estela"
