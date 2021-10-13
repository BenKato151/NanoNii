#!/usr/bin/python
import sys

from nano_nii import NanoNii
import argparse


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

    def default_task(self):
        # TODO: Create a loop where you can write a command, executes it, repeat
        print(f"Executing default of {self.nanoNii.name}")

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
    commands = CommandHandler()
    commands.create_tasks()
