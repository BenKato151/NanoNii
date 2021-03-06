#!venv/bin/python
import random
from time import sleep
from enum import Enum
from twitch_api import checkUser


class NanoNii:
    # Description of Nano Nii

    class Forms(Enum):
        NANO = 1
        HUMAN = 2
    name = "Nano Nii"
    age = "21+"
    species = "Nyandroid"
    visible_size = 137.16
    nano_size = visible_size / (10*9)  # I think this is the right convert from centimeters to nanometers? xD
    size = visible_size  # default is human-mode (size)
    height_type = "centimeter"
    current_mode = Forms.HUMAN
    is_live_on_twitch = False
    current_emotion = None
    lore = "<WIP>"  # TODO: Write the whole lore down when everything got published
    socials = {'Twitch': 'https://www.twitch.tv/nanoniittv', 'Youtube': 'https://www.youtube.com/c/NanoNiitv',
               'Twitter': 'https://twitter.com/NanoNii_', 'Patreon': 'https://www.patreon.com/Nii_Nii',
               'Discord': 'https://discord.gg/wSzETEhENW'}

    def __init__(self):
        print("Nano Nii is now running")

    # region NanoNii action functions
    def get_called_cute(self, viewer):
        print(f"Ahh... thanks >.< \nBut... I am not that cute senpai... but thank you {viewer}!\n"
              f"I am so {self.process_emotion('blushing')}")

    def process_emotion(self, emotion):
        # TODO: Make something with these emotions
        emotion_set = ['happiness', 'anger', 'sadness', 'fear', 'disgust', 'surprise', 'cheerful',
                       'blushing', 'crying', 'amusement', 'excitement', 'love', 'lewd', 'laughing',
                       'seiso', 'proud']
        # compare the given emotion parameter with the ones in the list and if found returns, if not, raise an Error
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

    def set_height(self, mode):
        # assign the param (bool) to the class field and if NanoNii is in Nano-mode, the size is assigned to it's value
        # and the right measurement type

        if mode == self.Forms.NANO:
            self.size = self.nano_size
            self.height_type = "nanometer"
            self.current_mode = self.Forms.NANO
        elif mode == self.Forms.HUMAN:
            self.size = self.visible_size
            self.height_type = "centimeter"
            self.current_mode = self.Forms.HUMAN
        else:
            print("wrong form")
            return
        print(f"My height is now {self.size} {self.height_type}")

    def get_links_to_socials(self):
        for social in self.socials.items():
            print(f"{social[0]}: {social[1]}")

    def fix_audio_issues(self):
        # This is lore stuff:
        # NanoNii can shrink into nano-size and can fix (preferred audio) issues
        # After NanoNii fixed everything, it will go to human-form
        if self.current_mode is not self.Forms.NANO:
            self.set_height(self.Forms.NANO)
        print(f"I am now in {self.current_mode.name} and it's time to fix your audio issues... nya~!")
        sleep(random.randint(1, 6))
        print("Your Nyandroid NanoNii fixed all your audio issues master! Nyaaa~!")
        self.set_height(self.Forms.HUMAN)

    @staticmethod
    def nyaaa():
        # Every Nyandroid should nyaaa every once in a while :3
        print("!!!~~NYAAA MASTER~~!!!")

    def get_live_status_twitch(self, twitch_link, user_id):
        self.is_live_on_twitch = checkUser(user_id)
        if self.is_live_on_twitch:
            return f"NanoNii is live on: {twitch_link}"
        else:
            return "NanoNii is not live! :("

    # TODO: Add more NanoNii actions
    # endregion


if __name__ == '__main__':
    nanoNii = NanoNii()
