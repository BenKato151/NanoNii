#!/usr/bin/python

from nano_nii import NanoNii
import argparse


class CommandHandler:

    def __init__(self):
        self.nanoNii = NanoNii()
        self.parser = argparse.ArgumentParser()
        self.add_args()
        self.args = self.parser.parse_args()

    def add_args(self):
        self.parser.add_argument("--fix-audio-issues", help="NanoNii turning into nano-mode and fixing issues",
                                 action='store_true')

    def create_tasks(self):
        if self.args.fix_audio_issues:
            self.nanoNii.fix_audio_issues()


if __name__ == '__main__':
    commands = CommandHandler()
    commands.create_tasks()
