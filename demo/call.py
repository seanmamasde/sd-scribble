import requests
import subprocess
import os
import time

image = open("test-img.png", "rb")
image = image.read()

res = requests.post(
    "http://localhost:5000",
    files={"image": image},
    headers={"prompt": "beautiful hand-drawn mountain ranges, detailed"},
)

while res.status_code != 200:
    if res.status_code == 200:
        output = open("test-output.jpg", "wb")
        output.write(res.content)
        output.close()
        subprocess.run(
            [
                "explorer",
                os.path.join(os.getcwd(), "test-output.png"),
            ],
        )
    else:
        print(f"request failed with status code {res.status_code}")
        print("trying again in 3 seconds...")
        time.sleep(3)
