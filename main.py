import openai
import speech_recognition

api_key = 'KEY'
openai.api_key = api_key

model_id = 'gpt-3.5-turbo'

sr = speech_recognition.Recognizer()


def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation


conversation = [{'role': 'system', 'content': 'How may I help you?'}]

conversation = ChatGPT_conversation(conversation)
print(conversation[-1]['content'])

while True:
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        prompt = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
