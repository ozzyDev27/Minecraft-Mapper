from PIL import Image
import os
ratio=128
def pythag(a,b):return (a**2+b**2)**.5
def getClosestColor(rgbIn):
	possible=((127, 178, 56), (247, 233, 163), (199, 199, 199), (255, 0, 0), (160, 160, 255), (167, 167, 167), (0, 124, 0), (255, 255, 255), (164, 168, 184), (151, 109, 77), (112, 112, 112), (64, 64, 255), (143, 119, 72), (255, 252, 245), (216, 127, 51), (178, 76, 216), (102, 153, 216), (229, 229, 51), (127, 204, 25), (242, 127, 165), (76, 76, 76), (153, 153, 153), (76, 127, 153), (127, 63, 178), (51, 76, 178), (102, 76, 51), (102, 127, 51), (153, 51, 51), (25, 25, 25), (250, 238, 77), (92, 219, 213), (74, 128, 255), (0, 217, 58), (129, 86, 49), (112, 2, 0), (209, 177, 161), (159, 82, 36), (149, 87, 108), (112, 108, 138), (186, 133, 36), (103, 117, 53), (160, 77, 78), (57, 41, 35), (135, 107, 98), (87, 92, 92), (122, 73, 88), (76, 62, 92), (76, 50, 35), (76, 82, 42), (142, 60, 46), (37, 22, 16), (189, 48, 49), (148, 63, 97), (92, 25, 29), (22, 126, 134), (58, 142, 140), (86, 44, 62), (20, 180, 133), (100, 100, 100), (216, 175, 147), (127, 167, 150))
	distances=[(x+1,round(pythag(pythag(abs(possible[x][0]-rgbIn[0]),abs(possible[x][1]-rgbIn[1])),abs(possible[x][2]-rgbIn[2])))) for x in range(len(possible))]
	return min(distances,key=lambda x:x[1])[0]
image=Image.open(input("Enter the directory of the image:\n>  ")).convert("RGB")
squareImage=image.resize((ratio,ratio),resample=Image.BOX)
colors=[]
for x in range(ratio):
	for y in range(ratio):
		r,g,b=squareImage.getpixel((y,x))
		colors.append(f"{getClosestColor((r,g,b))}.png")
try:os.remove(r"map.png")
except:pass
mosaic=Image.new(mode="RGB",size=(ratio*16,ratio*16),color=(255,255,255))
val=0
for x in range(ratio):
	for y in range(ratio):
		toPaste=Image.open(f"blocks\\{colors[val]}")
		mosaic.paste(toPaste,(y*16,x*16))
		val+=1
mosaic.show()
mosaic.save(r"map.png")
