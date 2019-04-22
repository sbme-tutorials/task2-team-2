from PIL import Image, ImageEnhance 
import numpy as np
x=np.load('square_phantom.npy')
SeparatingArrays=(len(x)/3)
I=x[1:int(SeparatingArrays),:]
im=Image.fromarray(I)
im=im.convert("L")
im.save('original.png')
enhancer = ImageEnhance.Brightness(im)
enhancher2=ImageEnhance.Contrast(im)
enhanced_im2 = enhancher2.enhance(1.5)
enhanced_im = enhancer.enhance(.5)
enhanced_im.save("brightnessdark.png")
enhanced_im2.save("contrast.png")