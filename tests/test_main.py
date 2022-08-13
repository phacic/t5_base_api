import json

import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_root(app_client):
    resp = app_client.get("/")

    # should be redirect response with status 307
    assert resp.history[0].status_code == status.HTTP_307_TEMPORARY_REDIRECT

    # actual response should be 200
    assert resp.status_code == status.HTTP_200_OK

    # url after redirect should be /docs
    assert resp.request.path_url == "/docs"


@pytest.mark.asyncio
async def test_translate_without_model_init(app_client):
    """
    model init is handled by startup event and since this client (app_client) do not that event,
    translate should return a ValueError
    """
    data = {
        "source_language": "en",
        "destination_language": "fr",
        "input_text": "How about you?",
    }

    with pytest.raises(ValueError):
        app_client.post("/api/v1/translate/", data=json.dumps(data))


@pytest.mark.asyncio
async def test_translate_with_model_init(app_client_startup):
    """
    translate with model init should work as expected
    :param app_client_startup:
    :return:
    """
    data = {
        "source_language": "en",
        "destination_language": "fr",
        "input_text": "How old are you??",
    }

    resp = app_client_startup.post("/api/v1/translate/", data=json.dumps(data))

    assert resp.status_code == status.HTTP_200_OK
