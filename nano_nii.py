#!/usr/bin/python
import random
from time import sleep


class NanoNii:
    name = "Nano Nii"
    age = "21+"
    species = "Nyandroid"
    visible_size = 137.16
    nano_size = visible_size / (10*9)
    size = visible_size
    is_in_nano_form = False
    current_emotion = None
    lore = "<WIP>"
    socials = {'Twitch': 'https://www.twitch.tv/nanoniittv', 'Youtube': 'https://www.youtube.com/c/NanoNiitv',
               'Twitter': 'https://twitter.com/NanoNii_', 'Patreon': 'https://www.patreon.com/Nii_Nii',
               'Discord': 'https://discord.gg/wSzETEhENW'}

    def __init__(self):
        print("Nano Nii is now running")

    def get_called_cute(self, viewer):
        print(f"Ahh... thanks >.< \nBut... I am not that cute senpai... but thank you {viewer}!\n"
              f"I am so {self.process_emotion('blushing')}")

    def process_emotion(self, emotion):
        # Make something with these emotions
        emotion_set = ['happiness', 'anger', 'sadness', 'fear', 'disgust', 'surprise', 'cheerful',
                       'blushing', 'crying', 'amusement', 'excitement', 'love', 'lewd', 'laughing',
                       'seiso', 'proud']
        valid_emotion = None
        for _emotion in emotion_set:
            if _emotion == emotion:
                valid_emotion = emotion
                self.current_emotion = valid_emotion

        if valid_emotion is None:
            raise NotImplementedError("couldn't process given emotion")
        return valid_emotion

    def get_emotion(self, emotion):
        print(f"There is something going inside of me... it's... I feel {self.process_emotion(emotion)} right now!")

    def set_height(self, is_nano):
        self.is_in_nano_form = is_nano
        if self.is_in_nano_form:
            self.size = self.nano_size
            height_type = "nanometer"
        else:
            self.size = self.visible_size
            height_type = "centimeter"
        print(f"My height is now {self.size} {height_type}")

    def get_links_to_socials(self):
        for social in self.socials.items():
            print(f"{social[0]}: {social[1]}")

    def fix_audio_issues(self):
        if self.is_in_nano_form is not True:
            self.set_height(True)
        print("I am now in nano-mode and it's time to fix your audio issues... nya~!")
        sleep(random.randint(1, 6))
        print("Your Nyandroid NanoNii fixed all your audio issues master! Nyaaa~!")
        self.set_height(False)

    @staticmethod
    def nyaaa():
        print("!!!~~NYAAA MASTER~~!!!")


if __name__ == '__main__':
    nanoNii = NanoNii()
