#--web true
#--param OPENAI_API_HOST https://openai.nuvolaris.io
#--param OPENAI_API_KEY $AUTH
#--kind python:default

from chat import chat

def main(args):
    return chat(args)
