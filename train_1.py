import gradio
import numpy as np

def greet(nom:str):
    print(f'Salut {nom}')

def salutation(nom:str):
    return (f'Salut {nom}')

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img







demo = gradio.Interface(fn=salutation,inputs="text",outputs="text")


demo.launch()