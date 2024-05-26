"""
This file contains all the constants used in the program.
"""
import g4f

TWITTER_TEXTAREA_CLASS = "public-DraftStyleDefault-block public-DraftStyleDefault-ltr"
TWITTER_POST_BUTTON_XPATH = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]"

OPTIONS = [
    "YouTube Shorts Automation",
    "Twitter Bot",
    "Affiliate Marketing",
    "Outreach",
    "Quit"
]

TWITTER_OPTIONS = [
    "Post something",
    "Show all Posts",
    "Setup CRON Job",
    "Quit"
]

TWITTER_CRON_OPTIONS = [
    "Once a day",
    "Twice a day",
    "Thrice a day",
    "Quit"
]

YOUTUBE_OPTIONS = [
    "Upload Short",
    "Show all Shorts",
    "Setup CRON Job",
    "Quit"
]

YOUTUBE_CRON_OPTIONS = [
    "Once a day",
    "Twice a day",
    "Thrice a day",
    "Quit"
]

# YouTube Section
YOUTUBE_TEXTBOX_ID = "textbox"
YOUTUBE_MADE_FOR_KIDS_NAME = "VIDEO_MADE_FOR_KIDS_MFK"
YOUTUBE_NOT_MADE_FOR_KIDS_NAME = "VIDEO_MADE_FOR_KIDS_NOT_MFK"
YOUTUBE_NEXT_BUTTON_ID = "next-button"
YOUTUBE_RADIO_BUTTON_XPATH = "//*[@id=\"radioLabel\"]"
YOUTUBE_DONE_BUTTON_ID = "done-button"

# Amazon Section (AFM)$
AMAZON_PRODUCT_TITLE_ID = "productTitle"
AMAZON_FEATURE_BULLETS_ID = "feature-bullets"

def parse_model(model_name: str) -> any:
    if model_name == "gpt4":
        return g4f.models.gpt_4
    elif model_name == "gpt35_turbo":
        return g4f.models.gpt_35_turbo
    elif model_name == "llama2_7b":
        return g4f.models.llama2_7b
    elif model_name == "llama2_13b":
        return g4f.models.llama2_13b
    elif model_name == "llama2_70b":
        return g4f.models.llama2_70b
    elif model_name == "mixtral_8x7b":
        return g4f.models.mixtral_8x7b
    elif model_name == "openchat_35":
        return g4f.models.openchat_35
    elif model_name == "dbrx-instruct":
        return g4f.models.dbrx_instruct
    elif model_name == "lzlv-70b":
        return g4f.models.lzlv_70b
    elif model_name == "airoboros-70b":
        return g4f.models.airoboros_70b
    elif model_name == "pi":
        return g4f.models.pi
    elif model_name == "codellama-34b-instruct":
        return g4f.models.codellama_34b_instruct
    elif model_name == "codellama-70b-instruct":
        return g4f.models.codellama_70b_instruct
    elif model_name == "dolphin-mixtral-8x7b":
        return g4f.models.dolphin_mixtral_8x7b
    elif model_name == "gigachat":
        return g4f.models.gigachat
    elif model_name == "claude_3_opus":
        return g4f.models.claude_3_opus
    elif model_name == "blackbox":
        return g4f.models.blackbox
    elif model_name == "mistral_7b":
        return g4f.models.mistral_7b
    elif model_name == "gpt_4o":
        return g4f.models.gpt_4o
    elif model_name == "codellama_34b_instruct":
        return g4f.models.codellama_34b_instruct
    elif model_name == "claude_3_haiku":
        return g4f.models.claude_3_haiku
    else:
        # Default model is gpt3.5-turbo
        return g4f.models.gpt_35_turbo
