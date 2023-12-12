#-------------------------------------------------------------------------------
# Name:        ChoseYourChaosGood
# Purpose:     Come to the dark side
# Author:      Nemius
# Created:     10/12/2023
# Copyright:   (c) Nemanja 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from funkcije import *
from bazaslika import *
import tkinter as tk
import sys
import os
from pathlib import Path
import json

#startuje program i proverava da li postoji json fajl
def main():
    path = Path("./izbor.json")
    postojiLifajl = (path.is_file())
    if postojiLifajl == True:
        proveraIzbora()
        chaosChosen = proveraIzbora()
        if chaosChosen == "niko":
            program()
        else:
            akojeVecIzabrao()
    else:
        napraviJson()
        main()

if __name__ == '__main__':
    main()
