import sys, numpy as np
from PIL import Image, ImageFilter
def stats(p):
    im=Image.open(p).convert('RGB').resize((1280,720),Image.LANCZOS)
    a=np.asarray(im).astype(float); L=np.asarray(im.convert('L')).astype(float)
    hsv=np.asarray(im.convert('HSV')).astype(float)
    lap=np.asarray(im.convert('L').filter(ImageFilter.FIND_EDGES)).astype(float)
    r,g,b=a[...,0],a[...,1],a[...,2]
    return dict(L=round(L.mean(),1),contrast=round(L.std(),1),S=round(hsv[...,1].mean()/255,2),
        warm=round((r>b+10).mean(),2),cold=round((b>r+10).mean(),2),texture=round(lap.mean(),1),RB=round((r-b).mean(),1))
for p in sys.argv[1:]: print(p.split('/')[-1], stats(p))
