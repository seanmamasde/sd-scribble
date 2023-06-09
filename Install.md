# Installation

## Versions

The instructions were tested **ONLY** under:

- Windows 11 build 23471 (dev channel) and build 22621 (stable channel)
- Stable Diffusion WebUI [commit 5ab7f213](https://github.com/AUTOMATIC1111/stable-diffusion-webui/tree/5ab7f213bec2f816f9c5644becb32eb72c8ffb89)
- Control Net v1.1 [commit 69fc48b](https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/69fc48b9cbd98661f6d0288dc59b59a5ccb32a6b)
- Python 3.10.11 [official site](https://www.python.org/downloads/release/python-31011/)

<span style="font-size: larger"><b>Caution: Attempts to run the project under an untested environment MAY NOT grant the desired outcome.</b></span>

> The reason why we can't utilize the GPU from NYCU IT center is due to the fact that the OS version (Ubuntu 18.04 LTS) and nVidia driver version are too low.
> We can't just upgrade the driver straight up from inside the container.

## Setup

1. Clone this tool: `git clone https://github.com/AI-Final-Proj/sd-scribble`
2. ControlNet models:

	```bash
	git lfs install
	git clone https://huggingface.co/lllyasviel/ControlNet-v1-1
	```

	> Note: `git lfs install` needs to be ran before cloning the repo.

3. Stable diffusion webui: `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui`
4. Add `--api` after `set COMMANDLINE_ARGS=` in `webui-user.bat` inside the stable diffusion folder, sos it looks like this: `set COMMANDLINE_ARGS=--api`.
5. Your folder should now look like this:
	```bash
	.
	├── ControlNet-v1-1
	├── sd-scribble
	└── stable-diffusion-webui
	```
6. Run the webui by launching `stable-diffusion-webui\webui-user.bat` (with administrator)
7. Open the browser and visit address at `https://127.0.0.1:7860`
8. In the webui, navigate to the "Extensions" tab on the top of the page, and go to "Install from URL" tab. Then add the extension from `https://github.com/Mikubill/sd-webui-controlnet`
9. Go back to the "Installed" tab, it should now say "processing"
10. Press the "Check for Updates" button, and press "Apply and Restart UI" just in case.
11. Once reloaded, navigate to the "Settings" tab next to the "Extensions" tab. Open ControlNet settings and look for "Allow other script to control this extension" and enable it, then apply settings
12. Close the WebUI and terminal windows running stable diffusion. Restart you PC is necessary (optional, but shouldn't be needed)
13. Move the `.pth` files from AI models folder `ControlNet-v1-1` to the folder at `stable-diffusion-webui\extensions\sd-webui-controlnet\models` (Also ensure that every `.pth` file has a corresponding `.yaml` file)

## Usage

1. Launch the webui by running the `stable-diffusion-webui\webui-user.bat` (note: you should wait until "Startup time:" is shown in the terminal before it's ready to be used)
2. Run the `Start.bat` inside the `real` folder. It'll be installing some packages only for the very first time, then it'll open canvas.
3. With the canvas open, now ready for some commands!

## Commands

| Key / Mouse button            | Control                                                    |
|-------------------------------|------------------------------------------------------------|
| Left button                   | Draw with the current brush size                           |
| Middle button                 | Draw with a white color brush                              |
| `e` + Left button             | Eraser brush (bigger)                                      |
| Wheel scroll up / down        | Increase / decrease brush size                             |
| `backspace`                   | Erase the entire sketch                                    |
| `shift` + Left button         | Draw a line between two clicks                             |
| `RETURN` or `ENTER`           | Request image rendering                                    |
| `ctrl` + `c`                  | Interrupt image rendering                                  |
| `c`                           | Display current configuration while pressed                |
| `p`                           | Edit prompt                                                |
| `alt` + `p`                   | Edit negative prompt                                       |
| `a`                           | Toggle autosave                                            |
| `ctrl` + `p`                  | Pause dynamic rendering                                    |
| `q`                           | Toggle quick rendering : low steps & HR fix off            |
| `n`                           | Random seed value                                          |
| `ctrl` + `n`                  | Edit seed value                                            |
| `UP` / `DOWN`                 | Increase / decrease seed by 1                              |
| `ctrl`+ `s`                   | Save the current generated image                           |
| `ctrl`+ `o`                   | Open an image file as sketch                               |
| `b`                           | Toggle batch rendering                                     |
| `x` or `ESC`                  | Quit                                                       |

## Appendices

- The default model is available [here](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors)
- You can find full list of supported modules [here](http://127.0.0.1:7860/controlnet/module_list)