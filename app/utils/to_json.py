from app.models.data import Data


def items_to_json(items):
    lic = []
    for i in items:
        lic.append(
            Data.to_json(i)
        )
    return lic
