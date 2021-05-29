import json

from app.models.data import Data


def info_query():
    info = []
    data = Data.query.all()
    # data = Data.query.filter_by(name='张三').first()
    for i in data:
        info.append(
            Data.to_json(i)
        )

    return info
