# AUTOGENERATED! DO NOT EDIT! File to edit: app.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'intf', 'classify_image']

# %% app.ipynb 1
from fastai.vision.all import *
import gradio as gr
import timm

# %% app.ipynb 3
learn = load_learner('model.pkl')

# %% app.ipynb 5
categories = learn.dls.vocab

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

# %% app.ipynb 7
image = gr.Image(height=192, width=192) # lecture material deprecated
label = gr.Label()
examples = ['basset.jpg']

# %% app.ipynb 8
intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)
