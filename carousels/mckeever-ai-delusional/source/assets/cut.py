from PIL import Image, ImageFilter
import numpy as np
from scipy import ndimage as nd
U='/root/.claude/uploads/b8b2b9c8-be04-5441-abd3-8e85c4b90725/'
src={1:'792a6ec4',2:'d97cb196',3:'27406235',4:'b2d7d8e7',5:'41a6d511',6:'a07157ff',7:'9122876a',8:'7b7f118b'}
def cut(n,box,name,thr=14):
    rgb=Image.open(U+src[n]+'-image.png').convert('RGB').crop(box)
    a=np.asarray(rgb).astype(float)
    r,g,b=a[...,0],a[...,1],a[...,2]
    lum=0.3*r+0.59*g+0.11*b
    blue=((b-r)>14)&(b>26)
    fg=(lum>thr)&~blue
    fg=nd.binary_opening(fg,iterations=2)
    lab,nl=nd.label(fg); sizes=nd.sum(fg,lab,range(1,nl+1))
    main=lab==(np.argmax(sizes)+1)
    # fill each row between extremes, then fill holes
    solid=main.copy()
    for y in range(main.shape[0]):
        xs=np.where(main[y])[0]
        if len(xs): solid[y,xs[0]:xs[-1]+1]=True
    solid=nd.binary_closing(solid,iterations=6); solid=nd.binary_fill_holes(solid)
    solid=nd.binary_erosion(solid,iterations=2)
    al=Image.fromarray((solid*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.6))
    # blue fringe -> desaturate inside silhouette edges
    d=np.asarray(rgb).astype(float); m=blue[...,None]
    grey=d.mean(axis=2,keepdims=True)*0.35
    d=np.where(m,grey.repeat(3,2),d)
    im=Image.fromarray(d.astype('uint8')); im.putalpha(al); im.save(name)
    chk=Image.new('RGB',im.size,(200,40,40)); chk.paste(im,(0,0),im); chk.save('chk_'+name)
cut(5,(520,470,1080,1350),'c_armscross_smile.png')
cut(1,(240,440,960,1300),'c_armscross_serious.png')
cut(2,(590,310,1060,1300),'c_standing.png')
cut(4,(0,500,545,1350),'c_phone_left.png')
cut(6,(470,400,1080,1350),'c_phone_right.png')
cut(8,(360,430,720,1350),'c_fullbody.png')
import glob
fs=sorted(glob.glob('chk_c*.png')); s=Image.new('RGB',(6*300,420),'white')
for k,f in enumerate(fs):
  im=Image.open(f); im.thumbnail((300,420)); s.paste(im,(k*300,0))
s.save('chk_sheet.png')
