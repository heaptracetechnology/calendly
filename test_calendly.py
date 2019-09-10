from http import HTTPStatus

def test_create_request(client):
    url = "/create"
    data = {
     "events":"invitee.created",
     "url":"https://blah.foo/bar"
    }
    response = client.post(url,json=data)
    assert response.status_code == HTTPStatus.OK

def test_subscribe_request(client):
    url = "/subscribe"
    data = {
      "hooksId":"497220"
    }
    response = client.post(url,json=data)
    assert response.status_code == HTTPStatus.OK

def test_list_request(client):
    url = "/subscribe/list"
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK

def test_delete_request(client):
    url = "/delete"
    data = {
      "hooksId":"497220"
    }
    response = client.post(url,json=data)
    assert response.status_code == HTTPStatus.OK    

def test_eventList_request(client):
    url = "/event/type"
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK    

def test_about_request(client):
    url = "/about"
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK      