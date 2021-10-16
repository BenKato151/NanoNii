#!venv/bin/python
import sys
import argparse
from nano_nii import NanoNii
from dotenv import dotenv_values
config = dotenv_values(".env")
commands_list = "Following commands can be used:\n\t- You are cute\n\t- Socials\n\t- Nyaaa\n\t- Emotion\n\t- " \
                "Fix audio issues\n\t- Set height\n\t- Help\n\t- Exit"


class CommandHandler:

    def __init__(self):
        self.nanoNii = NanoNii()
        self.parser = argparse.ArgumentParser()
        self.add_args()
        self.args = self.parser.parse_args()

    # Adds terminal arguments, creates tasks given by functions of NanoNii class
    def add_args(self):
        self.parser.add_argument("--fix-audio-issues", help="NanoNii turning into nano-mode and fixing issues",
                                 action='store_true')
        self.parser.add_argument("--get-socials", help="Prints all socials with it's links", action="store_true")
        self.parser.add_argument("--set-height", type=bool, help="Switch between nano sized NanoNii and visible form"
                                                                 "True for nano mode and false for human mode")
        self.parser.add_argument("--call-me-cute", help="Call NanoNii cute")
        self.parser.add_argument("--nyaaa", help="Make NanoNii Nyaaa for you uwu!", action="store_true")
        self.parser.add_argument("--process-emotion", help="Make NanoNii feel something!")

    # region Default task - command Loop

    def default_task(self):
        print(f"Executing default of {self.nanoNii.name}")
        print(commands_list)
        master_name = input(f"Oh, you are now my master! I am {self.nanoNii.name}. What is your name master? :3\t")
        # master_name = "BenKato"
        print(f"Understood, {master_name} is my master! uwu")
        running = True
        while running:
            try:
                command = input("Write a command\n")
                if command.lower() == "socials":
                    self.nanoNii.get_links_to_socials()
                elif command.lower() == "nyaaa":
                    self.nanoNii.nyaaa()
                elif command.lower() == "emotion":
                    emotion = input("What do you want me to feel?\t")
                    self.nanoNii.get_emotion(emotion)
                elif command.lower() == "you are cute":
                    self.nanoNii.get_called_cute(master_name)
                elif command.lower() == "set height":
                    switch_nano_nii = input(f"In which form do you want me? [human,nano]:\n\t")
                    if switch_nano_nii.lower() == "human":
                        self.nanoNii.set_height(self.nanoNii.Forms.HUMAN)
                    elif switch_nano_nii.lower() == "nano":
                        self.nanoNii.set_height(self.nanoNii.Forms.NANO)
                    else:
                        print("Wrong mode")
                elif command.lower() == "fix audio issues":
                    self.nanoNii.fix_audio_issues()
                elif command.lower() == "help":
                    print(commands_list)
                elif command.lower() == "exit":
                    print("Exit")
                    break
                else:
                    print("no valid command")
            except KeyboardInterrupt:
                print("\nExit")
                running = False

    # endregion

    def create_tasks(self):
        if self.args.fix_audio_issues:
            self.nanoNii.fix_audio_issues()
        if self.args.get_socials:
            self.nanoNii.get_links_to_socials()
        if self.args.call_me_cute:
            self.nanoNii.get_called_cute(self.args.call_me_cute)
        if self.args.nyaaa:
            self.nanoNii.nyaaa()
        if self.args.process_emotion:
            self.nanoNii.get_emotion(self.args.process_emotion)
        if self.args.set_height:
            self.nanoNii.set_height(self.args.set_height)
        # If no args are given, then it will run the default task, which should be interactive
        if len(sys.argv) == 1:
            self.default_task()


if __name__ == '__main__':
    try:
        commands = CommandHandler()
        commands.create_tasks()
    except KeyboardInterrupt:
        print("\nExit")
