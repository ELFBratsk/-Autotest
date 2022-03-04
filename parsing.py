import requests

class TestFirstApi :
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = 'Vitalii'
        data = {'name' : name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Не выполнилось"

        response_dict = response.json()
        assert "ответ" in response_dict, "Ошибка"

        expected_response_text = f"привет" , {name}
        actual_response_text = response_dict ['ответ2']
        assert actual_response_text == expected_response_text , "Не актуально"
