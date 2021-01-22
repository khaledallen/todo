#!/usr/bin/env python3

import os.path
import json
from record import Voice
from taskmanager import TaskManager
import speech_recognition as sr

def main():
    local_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(local_path, 'config.json')
    if not os.path.exists(config_path):
        print('Please create a config.json file')
        #This is where the install function will go
        return

    f = open(config_path)
    config = json.load(f)

    os.chdir(os.path.expanduser(config['tasksDirectory']))

    #audioInterface = Voice()
    #intent = audioInterface.get_intent()

    def listen():
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            print("Processing...")

        try:
            speech = r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)
            print(speech)
            intent = speech['entities']['intent'][0]['value']

            if intent == "task_create":
                try:
                    todo = TaskManager(config['dbName'])
                    task_name = speech['entities']['task_name'][0]['value'] 
                    todo.add(task_name, quick_input=True)
                    todo.list()
                except:
                    print("There was an error")
            if intent == "task_complete":
                try:
                    todo = TaskManager(config['dbName'])
                    task_id = speech['entities']['number'][0]['value']
                    todo.complete(task_id)
                except:
                    print("There was an error")
            if intent == "task_clear":
                try:
                    todo = TaskManager(config['dbName'])
                    todo.clear(force=True)
                except:
                    print("There was an error")
            if intent == "exit":
                print("exiting")
            return

        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))


    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            print("Processing...")

        # recognize speech using Wit.ai
        WIT_AI_KEY = config['witApiKey']
        intent = None
        try:
            speech = r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)
            print(speech)
            if speech['entities'] and speech['entities']['intent']:
                intent = speech['entities']['intent'][0]['value']
                if intent == "listen":
                    print("Listening")
                    listen()

        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))


if __name__ == "__main__":
    main()
