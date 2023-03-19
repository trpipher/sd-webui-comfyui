import sys, os
import multiprocessing
from modules import script_callbacks
from lib_comfyui import async_comfy_loader

thread = None
model_queue = multiprocessing.Queue()


def on_model_loaded(model):
    model_queue.put(model)
script_callbacks.on_model_loaded(on_model_loaded)


def start():
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    global thread
    thread = multiprocessing.Process(target=async_comfy_loader.main, args=(model_queue, ))
    thread.start()


def stop():
    global thread
    thread.terminate()
    thread = None