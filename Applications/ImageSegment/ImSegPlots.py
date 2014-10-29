from matplotlib import pyplot as plt
from matplotlib.image import imsave
import solutions

def monuments_seg():
    img_color = plt.imread('monument.png')
    img = (img_color[:,:,0]+img_color[:,:,1]+img_color[:,:,2])/3.0
    pos, neg = solutions.segment(img)

    img_color1 = img_color.copy()
    img_color2 = img_color.copy()
    img_color1[neg>0,:] = 0.
    img_color2[pos>0,:] = 0.

    imsave('NegMon.png', img_color1)
    imsave('PosMon.png', img_color2)
    imsave('RegMon.png', img_color)
    
def dream_seg():
    img_color = plt.imread('dream.png')
    img = (img_color[:,:,0]+img_color[:,:,1]+img_color[:,:,2])/3.0
    pos, neg = solutions.segment(img)
    
    imsave('NegDream.png', neg)
    imsave('PosDream.png', pos)
    imsave('RegDream.png', img_color)
    
if __name__ == "__main__":
    monuments_seg()
    dream_seg()

