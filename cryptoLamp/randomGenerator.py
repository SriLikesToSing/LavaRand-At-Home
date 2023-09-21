import numpy as np
from hashlib import sha1

#https://gist.github.com/UnquietCode/99b69b99e00ce52e34c1
#https://jeremykun.com/2016/07/11/the-blum-blum-shub-pseudorandom-generator/
#https://www.computerworld.com/article/3173616/the-sha1-hash-function-is-now-completely-unsafe.html

filename = "seed_val.txt"
lavaImage = ""


#shoudl we incrypt the n file?
def save_seed(val, filename=filename):
    """ saves val. Called once in simulation1.py """
    with open(filename, "w") as f:
        f.write(str(val))
#save_seed(0)

def load_seed(filename=filename):
    """ loads val. Called by all scripts that need the shared seed value """
    with open(filename, "r") as f:
        # change datatype accordingly (numpy.random.random() returns a float)
        return int(f.read())

def generateNumber(Low, High, Size):
    #hash the image produced by physically random lavalamp
    hashedImage = sha1(open(lavaImage, 'rb').read()).hexdigest()
    seed = np.random.default_rng(int(hashedImage, 16))
    rng = np.random.default_rng(int(hashedImage, 16)+seed.integers(low=1, high=500000, size=1))
    rint = rng.integers(low=Low, high=High, size=Size)

    return list(rint)

def boink():
    save_seed(load_seed()+1)

print("type 'done' when finished")
lavaImage = input("input image name from lavalamp \n")

if(lavaImage.endswith('.png') or lavaImage.endswith('.jpg')):
    pass
elif lavaImage == 'done':
    exit(0)
else:
    raise Exception("Input valid image")

#print(load_seed())

print("type low, high, and number of values to be generated separated by comma. ex: 2,50,5")
print("if you want to input a new lava lamp image type 'new image' \n")
print("type 'done' when finished")
INPUT = ""

while INPUT != 'done':
    INPUT = input()
    if INPUT == 'done':
        break
    if INPUT == 'new image':
        lavaImage = input()
        if(lavaImage.endswith('.png') or lavaImage.endswith('.jpg')):
            continue
        else:
            raise Exception("Input valid image")

    array = INPUT.split(',')
    print(generateNumber(int(array[0]), int(array[1]), int(array[2])))



