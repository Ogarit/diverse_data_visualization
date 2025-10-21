import tkinter
import pyautogui


def get_dpi():
    """Verifica qual o dpi do sitema."""
    root = tkinter.Tk()
    root.withdraw()
    dpi = root.winfo_fpixels('1i')
    root.destroy()
    return dpi


def get_gui_size():
    """Verifica o tamanho da tela"""
    x = pyautogui.size()[0] / get_dpi()
    y = pyautogui.size()[1] / get_dpi()
    dimensions = {'x': x, 'y': y}
    return dimensions
