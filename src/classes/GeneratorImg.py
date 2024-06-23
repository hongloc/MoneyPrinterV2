"""
freeGPT's prodia module
"""

from requests import get, post
from random import randint
from requests.exceptions import RequestException
import time
# import prodiapy
from requests.adapters import HTTPAdapter
import requests

class Generation:
    """
    This class provides methods for generating images based on prompts.
    """

    def create(self, prompt):
        """
        Create a new image generation based on the given prompt.

        Args:
            prompt (str): The prompt for generating the image.

        Returns:
            resp: The generated image content
        """
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
            # "X-Prodia-Key": "555889c5-0dd6-43af-b96c-a7d0aa8d6186"
        }
        try:
            changed_prompt = "Korean idol face. " + prompt
            print('changed_prompt: ', changed_prompt)
            # prodia = prodiapy.Prodia(api_key="555889c5-0dd6-43af-b96c-a7d0aa8d6186")

            # prompt = changed_prompt

            # job = prodia.sdxl.generate(
            #   prompt=prompt,
            #   model="sd_xl_base_1.0.safetensors [be9edd61]",
            #   negative_prompt="verybadimagenegative_v1.3, ng_deepnegative_v1_75t, (ugly face:0.5),cross-eyed,sketches, (worst quality:2), (low quality:2.1), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy, DeepNegative, facing away, tilted head, {Multiple people}, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, repeating hair",
            #   width=1024,
            #   height=1024,
            #   sampler="DPM++ 2M Karras",
            #   seed=randint(1, 10000),
            #   cfg_scale=7,
            #   steps=20
            # )
            # result = prodia.wait(job)

            # print(result.image_url)
            # # return result.image_url
            # return get(
            #     result.image_url + "?download=1",
            #     headers=headers,
            # ).content


            # payload = {
            #     "model": "shoninsBeautiful_v10.safetensors [25d8c546]",
            #     "prompt": changed_prompt,
            #     "negative_prompt": "verybadimagenegative_v1.3, ng_deepnegative_v1_75t, (ugly face:0.5),cross-eyed,sketches, (worst quality:2), (low quality:2.1), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy, DeepNegative, facing away, tilted head, {Multiple people}, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, repeating hair",
            #     "width": 1024,
            #     "height": 1024,
            #     "sampler": "DPM++ 2M Karras",
            #     "seed": randint(1, 10000),
            #     "cfg_scale": 7,
            #     "steps": 20
            # }
            # url = "https://api.prodia.com/v1/sd/generate"
            # resp = post(url, json=payload, headers=headers)
            s = requests.Session()
            s.mount("https://api.prodia.com/generate", HTTPAdapter(max_retries=5))
            resp = s.get(
                "https://api.prodia.com/generate",
                params={
                    "new": "true",
                    "prompt": changed_prompt,
                    # "model": "dreamshaper_6BakedVae.safetensors [114c8abb]",
                    # "negative_prompt": "(nsfw:1.5),verybadimagenegative_v1.3, ng_deepnegative_v1_75t, (ugly face:0.5),cross-eyed,sketches, (worst quality:2), (low quality:2.1), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy, DeepNegative, facing away, tilted head, {Multiple people}, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, repeating hair",
                    # "steps": "50",
                    # "cfg": "9.5",
                    # "seed": randint(1, 10000),
                    # "sampler": "Euler",
                    # "aspect_ratio": "square",


                    # "model": "breakdomain_I2428.safetensors [43cc7d2f]",
                    # "model": "dreamlike-anime-1.0.safetensors [4520e090]",
                    # "model": "absolutereality_v181.safetensors [3d9d4d2b]",
                    # breakdomain_M2150.safetensors [15f7afca]
                    # anythingV5_PrtRE.safetensors [893e49b9]
                    # shoninsBeautiful_v10.safetensors [25d8c546]
                    # dalcefo_v4.safetensors [425952fe]
                    # EimisAnimeDiffusion_V1.ckpt [4f828a15] ani
                    # dreamshaper_8.safetensors [9d40847d] hum
                    # epicrealism_naturalSinRC1VAE.safetensors [90a4c676]
                    # revAnimated_v122.safetensors [3f4fefd9]
                    "model": "epicrealism_naturalSinRC1VAE.safetensors [90a4c676]",
                    "negative_prompt": "verybadimagenegative_v1.3, ng_deepnegative_v1_75t, (ugly face:0.5),cross-eyed,sketches, (worst quality:2), (low quality:2.1), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy, DeepNegative, facing away, tilted head, {Multiple people}, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, repeating hair",
                    "steps": "20",
                    "cfg": "7",
                    "seed": randint(1, 10000),
                    "sample": "DPM++ 2M Karras",
                    "aspect_ratio": "square"
                },
                headers=headers,
                timeout=30,
            )
            data = resp.json()
            print('data: ', data)
            time.sleep(20)
            while True:
                # resp = get(f"https://api.prodia.com/v1/job/{data['job']}", headers=headers)
                
                s = requests.Session()
                s.mount(f"https://api.prodia.com/job/{data['job']}", HTTPAdapter(max_retries=5))
                resp = s.get(f"https://api.prodia.com/job/{data['job']}", headers=headers)
                
                json = resp.json()
                print('json: ', json)
                time.sleep(20)
                if json["status"] == "succeeded":
                    return s.get(
                        f"https://images.prodia.xyz/{data['job']}.png?download=1",
                        headers=headers,
                    ).content
        except RequestException as exc:
            raise RequestException("Unable to fetch the response.") from exc

'''
self image_prompts:  ["Anna, a selfless flower caregiver, surrounded by a vibrant bouquet of flowers, with a subtle hint of sadness in her eyes, reflecting her poignant realization at a friend's funeral.", 'Anna, with a gentle touch, tending to a wilting flower, symbolizing her own withering away, amidst a backdrop of lush greenery and colorful blooms.', "A close-up of Anna's hands, worn and weathered from years of nurturing flowers, yet still holding a delicate petal, representing her journey towards self-care.", 'Anna, standing in a field of sunflowers, their bright yellow petals shining like a beacon of hope, as she begins to prioritize her own growth and well-being.', 'A serene Anna, sitting in a garden, surrounded by a kaleidoscope of flowers, with a soft, warm light illuminating her face, symbolizing her newfound balance and harmony.', 'Anna, with a determined look, setting boundaries and saying no to the constant demands of others, amidst a backdrop of overgrown, tangled flowers, representing her old life.', "A split-screen image, with Anna's worn, tired face on one side, and a vibrant, blooming flower on the other, highlighting her transformation towards self-care and prioritizing her own needs.", 'Anna, gently watering a small, delicate flower, symbolizing her newfound ability to nurture and care for herself, amidst a backdrop of lush, green foliage.', 'A stunning Anna, standing in a blooming garden, surrounded by a riot of colors, with a confident smile, representing her growth and flourishing, as she learns to prioritize her own needs.', 'Anna, sitting in a cozy, intimate space, surrounded by candles, flowers, and soft, warm lighting, symbolizing her newfound love and care for herself, as she repots her own life.']

'''

"""
freeGPT's pollinations module
"""

# from requests import get
# from requests.exceptions import RequestException
# from random import randint


# class Generation:
#     """
#     This class provides methods for generating images based on prompts.
#     """

#     def create(self, prompt):
#         """
#         Create a new image generation based on the given prompt.

#         Args:
#             prompt (str): The prompt for generating the image.

#         Returns:
#             resp: The generated image content
#         """
#         try:
#             return get(
#                 url=f"https://image.pollinations.ai/prompt/{prompt}{randint(1, 10000)}",
#                 timeout=30,
#             ).content
#         except RequestException as exc:
#             raise RequestException("Unable to fetch the response.") from exc