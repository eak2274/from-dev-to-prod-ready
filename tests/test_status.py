from fastapi.testclient import TestClient
from from_dev_to_prod_ready.main import app
from from_dev_to_prod_ready.settings import settings

def test_answer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status" : "ok"}
