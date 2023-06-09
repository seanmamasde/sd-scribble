from flask import Flask, request, send_file
from PIL import Image
from io import BytesIO
import torch
from diffusers import StableDiffusionImg2ImgPipeline

# the model can be modified
model = "nitrosocke/Ghibli-Diffusion"
device = "cuda"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    model,
    torch_dtype=torch.float16,
).to(device)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    img = Image.open(request.files["image"])
    prompt = request.headers["prompt"]
    print(img, prompt)
    prompt = "ghibli style, a fantasy landscape with castles"
    generator = torch.Generator(device=device).manual_seed(1024)
    image = pipe(
        prompt=prompt,
        image=img,
        strength=0.75,
        guidance_scale=7.5,
        generator=generator,
    ).images[0]
    out_img = BytesIO()
    image.save(out_img, format="PNG")
    out_img.seek(0)
    return send_file(out_img, mimetype="image/png", download_name="image.png")


app.run(debug=False)
