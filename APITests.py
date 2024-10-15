import requests

#Test case to check the random dog image

def test_get_random_dog_image():
    #send request
    response= requests.get("https://dog.ceo/api/breeds/image/random")

    #check the status code=200
    assert response.status_code==200
    
    #parse the response
    json_data= response.json()

    #assert status
    assert json_data["status"]== "success"

    #assert the message field exists
    assert "message" in json_data

    #assert the message field contains url
    assert json_data["message"].startswith("https://")
    print("Test passed for test_get_random_dog_image")

test_get_random_dog_image()


#Test case to check the breed list
def test_get_breed_list():
    #send request
    response= requests.get("https://dog.ceo/api/breeds/list/all")

    #check the status code=200
    assert response.status_code==200
    
    #parse the response
    json_data= response.json()

    #assert status
    assert json_data["status"]== "success"

    #assert the message field exists
    assert "message" in json_data

    #assert the message field contains a dictionary
    assert isinstance(json_data["message"],dict)
    print("Test passed for test_get_breed_list")

test_get_breed_list()


#Test case to check the breed list
def test_get_images_by_breed():
    breed="hound"
    #send request
    response= requests.get(f"https://dog.ceo/api/breed/{breed}/images")

    #check the status code=200
    assert response.status_code==200
    
    #parse the response
    json_data= response.json()

    #assert status
    assert json_data["status"]== "success"

    #assert the message field exists
    assert "message" in json_data

    #assert the message field contains a dictionary
    assert isinstance(json_data["message"],list)
    print("Test passed for test_get_images_by_breed")
    
test_get_images_by_breed()


#Test case to check the breed list
def test_get_sub_breed():
    breed= "bulldog"
    #send request
    response= requests.get(f"https://dog.ceo/api/breed/{breed}/list")

    #check the status code=200
    assert response.status_code==200
    
    #parse the response
    json_data= response.json()

    #assert status
    assert json_data["status"]== "success"

    #assert the message field exists
    assert "message" in json_data

    #assert the message field contains a dictionary
    assert isinstance(json_data["message"],list)
    print("Test passed for test_get_sub_breed")
    
test_get_sub_breed()