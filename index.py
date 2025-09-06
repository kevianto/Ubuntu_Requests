import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # 🌐 Prompt the user for an image URL
    url = input("Enter the image URL: ")

    # 📂 Directory for storing images
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)  # Respectfully create if not exists

    try:
        # 🌍 Connect to the community (download image)
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Handle HTTP errors

        # 📝 Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If no filename, generate one
            filename = "image_from_ubuntu.jpg"

        # 📌 Full path for saving the image
        filepath = os.path.join(directory, filename)

        # 💾 Save the image in binary mode
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"✅ Image saved successfully in '{filepath}'")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Request error occurred: {req_err}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    fetch_image()
