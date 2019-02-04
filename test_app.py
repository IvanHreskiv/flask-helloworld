

def test_get(client):
    # Visit home page
    response = client.get("/")
    assert response.status_code==200

def test_post(client):
    # Visit home page
    response = client.post("/", json=dict(name='Ivan'))
    assert response.status_code==200
    assert response.json['message'] == 'Hello, Ivan!' 

    response = client.post("/", json=dict(name='Anna'))
    assert response.status_code==200
    assert response.json['message'] == 'Hello, Anna!' 
