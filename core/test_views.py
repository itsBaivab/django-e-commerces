def test_example_view(client):
    response = client.get('/example-url/')
    assert response.status_code == 200
    assert 'Expected Content' in response.content.decode()