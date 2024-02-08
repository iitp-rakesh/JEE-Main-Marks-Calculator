import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from config import application_number, dob  # Importing from config.py

# Function to extract captcha image URL
def extract_captcha_image_url(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    captcha_img_tag = soup.find('img', id='dynamicmodel-verifycode-image')
    if captcha_img_tag:
        return captcha_img_tag['src']
    return None

# Function to display captcha image in terminal and prompt for captcha value
def display_captcha_and_get_input(captcha_image_url):
    response = requests.get(captcha_image_url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        image.show()
        captcha_value = input("Enter the captcha value: ")
        return captcha_value
    else:
        print("Failed to retrieve captcha image.")
        return None

# URL of the login page
login_url = 'https://jeemain.ntaonline.in/frontend/web/answer-key-challenge/login-answer'

# Send a GET request to the login page
response = requests.get(login_url)

# Check if the request was successful
if response.status_code == 200:
    # Extract captcha image URL from the HTML content
    captcha_image_url = extract_captcha_image_url(response.content)
    if captcha_image_url:
        # Display captcha image in terminal and get user input
        captcha_value = display_captcha_and_get_input(captcha_image_url)
        if captcha_value:
            # Form data for login
            login_data = {
                'DynamicModel[ApplicationNumber]': application_number,
                'DynamicModel[Day]': dob.split('-')[0],
                'DynamicModel[Month]': dob.split('-')[1],
                'DynamicModel[Year]': dob.split('-')[2],
                'DynamicModel[verifyCode]': captcha_value,
            }
            # Send a POST request to login
            login_response = requests.post(login_url, data=login_data)
            # Check if login was successful
            if login_response.status_code == 200:
                print("Login successful")
                # Proceed with further actions after successful login
            else:
                print("Login failed. Status code:", login_response.status_code)
        else:
            print("Failed to get captcha value.")
    else:
        print("Failed to extract captcha image URL from the login page.")
else:
    print("Failed to retrieve the login page.")
