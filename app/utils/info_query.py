import json

from app.models.data import Data


def info_query():
    # info = {}
    # data = Data.query.first()
    # for i in data:
    #   info.add(
    #       Data.to_json(i)
    #   )
    info = []
    data = Data.query.all()
    for i in data:
        info.append(
            Data.to_json(i)
        )

    return info
