# AI Final Project

> Introduction to Artificial Intelligence Final Project
>
> Prof. Yi-Ting Chen, Academic Year 111-2

## Project Title

<span style="font-size: larger"><b>Scribble-Drafting in Realtime Made Possible by Stable-Diffusion</b></span>

A script written in python that lets you paint on a canvas and sends that image every stroke to the automatic1111 API
and update the canvas whenever a new image is generated.

## Basic Info

- Group #: 29
- Group Name: 🗿🗿🗿
- Members:

    | Student ID | Name |
    |:----------:|:----:|
    | 110550074  | 馬楷翔  |
    | 110550038  | 莊書杰  |
    |  0717078   | 柯孟豪  |

## Motivation

There're lots of text-to-image solutions out there, like Dall-E by openAI and Midjourney on Discord; or img2img services like stable diffusion, but the workflow isn't as streamlined as we thought to be. So we re-imagined the way it could be, by adding a simple canvas right next to it, you can now draw and see it render in realtime

## Methods

We created a simple diffusion api using diffuser and flask, so that we can send our drawing/prompt to it and get the diffused result in return.

1. The first simple diffusion api we made is just for demonstration, and test out how our concept works.

2. The real one is here: we use automatic1111's `stable-diffusion-webui` project and the `controlnet` plugin for it, and so we can host it on anywhere and just submit our drawing/prompt to get the results!

## Repository Overview

File Structure Tree

```bash
.
├── demo
│  ├── call.py
│  ├── demo.py
│  ├── test-img.jpg
│  └── test-output.png
├── demo_setup.md
├── Install.md
├── README.md
└── real
   ├── config.json
   ├── controlnet.json
   ├── extra
   ├── INSTALL_Windows.md
   ├── main.py
   ├── outputs
   ├── presets.json
   ├── README.md
   ├── requirements.txt
   ├── Start.bat
   └── venv

```

## About

- for the demo, please see `demo_setup.md`

- for the more detailed one, please see `install.md`

## Resources

- [Diffusers](https://github.com/huggingface/diffusers)
- [Control Net v1.1](https://huggingface.co/lllyasviel/ControlNet)
- [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
