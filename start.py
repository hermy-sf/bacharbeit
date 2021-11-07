try:
    import os
    import pip
    import sys
    import threading
except ImportError:
    print(" import error in start.py")

import logging  # DEBUG INFO WARNING ERROR
from logging.handlers import QueueHandler
logging.basicConfig(filename="log/win_main_log.log",
                    level=logging.DEBUG,  # <- set logging level
                    format="%(name)s ______  %(asctime)s : %(levelname)s : \n %(message)s")  # set level


def test_version():

    # python system  check
    # print(sys.version)
    version = sys.version_info[0:2]

    print("Python version ", sys.version[0:40])

    if not sys.version_info[:2][0] > 2:
        print("\n Error \n installed python: ", "version ",
              version[0], ".", version[1], sep="")
        #print("version available ",sys.version_info)
        print("\n minimum requirements is python 3.7 \n ERROR end")
        return False

    return True


def test_import():
    #print("\n python modulse avalibel: ")
    #os.system('pip list')
    #print("\n end python modulse")

    #print("eggs geladen: ",'eggs' in sys.modules)
    #print("numpy geladen: ",'numpy' in sys.modules)

    #print("INFO imported \n")
    # print(*sys.modules.keys(),sep="\n")

    # list of all necessery imports
    try:
        import numpy
        #import eggs
        import tkinter

    except ModuleNotFoundError as err:
        # Error handling
        print("\nERROR loading import \n")
        print(err)

        return False
    else:
        return True


def test_settings():

    return True


def info_dialog():
    text = """************************************************  \n
    Autor: Philipp MALIN
    Date: 01.07.2021
    Version: 1.2
    Description: Grapical user interface to control SDR
                 for MR-Analys of contrast medium.
    \n************************************************  """
    return text


# start programm
if __name__ == "__main__":
    print("start GUI")

    print("number of treads running: ", threading.active_count())
    print("current treads: ", threading.current_thread())
    print("list of all treads: ", threading.enumerate())

    print(info_dialog())
    # do all checks
    test_dict = {}

    test_dict["test_version"] = test_version()
    test_dict["test_import"] = test_import()
    test_dict["test_settings"] = test_settings()

    print("Check list:", *test_dict.items(), sep="\n")

    if False in test_dict.values():
        print("ERROR \n problem with imports \n")
        raise ImportError("not all imports are satisfied")

    else:
        print("\n\nimports alles ok\n\n")

    # start Program
    sys.path.append("program")

    import GUI  # start GUI

    print("-_____END check start of GUI ____-")
