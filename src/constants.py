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
    if model_name == "gpt4": # 018
        return g4f.models.gpt_4
    elif model_name == "gpt_4o": # okay
        return g4f.models.gpt_4o
    elif model_name == "gigachat": # 0 api key
        return g4f.models.gigachat
    elif model_name == "meta": # 500
        return g4f.models.meta
    elif model_name == "llama3_8b_instruct": # 018
        return g4f.models.llama3_8b_instruct
    elif model_name == "llama3_70b_instruct":
        return g4f.models.llama3_70b_instruct
    elif model_name == "codellama_34b_instruct": # 500
        return g4f.models.codellama_34b_instruct
    elif model_name == "codellama_70b_instruct": # 018
        return g4f.models.codellama_70b_instruct
    elif model_name == "mixtral_8x7b": # 500
        return g4f.models.mixtral_8x7b
    elif model_name == "mistral_7b": # 500
        return g4f.models.mistral_7b
    elif model_name == "mistral_7b_v02": # 500
        return g4f.models.mistral_7b_v02
    elif model_name == "claude_v2": # 018
        return g4f.models.claude_v2
    elif model_name == "claude_3_opus": # 500
        return g4f.models.claude_3_opus
    elif model_name == "claude_3_sonnet": # 500
        return g4f.models.claude_3_sonnet
    elif model_name == "claude_3_haiku":
        return g4f.models.claude_3_haiku
    elif model_name == "pi": # 500
        return g4f.models.pi
    elif model_name == "dbrx_instruct": # 018
        return g4f.models.dbrx_instruct
    elif model_name == "command_r_plus": # 500
        return g4f.models.command_r_plus
    elif model_name == "blackbox":
        return g4f.models.blackbox
    elif model_name == "reka_core": # 0 cookie
        return g4f.models.reka_core
    elif model_name == "nemotron_4_340b_instruct":
        return g4f.models.nemotron_4_340b_instruct
    elif model_name == "Phi_3_mini_4k_instruct":
        return g4f.models.Phi_3_mini_4k_instruct
    elif model_name == "Yi_1_5_34B_Chat":
        return g4f.models.Yi_1_5_34B_Chat
    elif model_name == "Nous_Hermes_2_Mixtral_8x7B_DPO":
        return g4f.models.Nous_Hermes_2_Mixtral_8x7B_DPO
    elif model_name == "llama_2_70b_chat":
        return g4f.models.llama_2_70b_chat
    elif model_name == "gemma_2_9b_it":
        return g4f.models.gemma_2_9b_it
    elif model_name == "gemma_2_27b_it":
        return g4f.models.gemma_2_27b_it
    else:
        # Default model is gpt3.5-turbo
        return g4f.models.gpt_35_turbo
