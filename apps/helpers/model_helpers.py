from django.db import models

# from django.db import DEFAULT_DB_ALIAS


def getObjects(model: models.Model, id: str = None):
    if id is None:
        return model.objects.all()
    try:
        return model.objects.get(pk=id)
    except model.DoesNotExist:
        return None


# def get_or_none(model: models.Model, using: str = DEFAULT_DB_ALIAS, **kwargs):
#     try:
#         return model.objects.using(using).get(**kwargs)
#     except model.MultipleObjectsReturned as e:
#         raise Exception(
#             "Multiple objects returned instead of one.\nOriginal Error: ", str(e)
#         )

#     except model.DoesNotExist:
#         return None
