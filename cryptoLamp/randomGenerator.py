import numpy as np
from hashlib import sha1

#https://gist.github.com/UnquietCode/99b69b99e00ce52e34c1
#https://jeremykun.com/2016/07/11/the-blum-blum-shub-pseudorandom-generator/
#https://www.computerworld.com/article/3173616/the-sha1-hash-function-is-now-completely-unsafe.html

filename = "seed_val.txt"


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

def generateNumber(Low, High, Size, n):
    #hash the image produced by physically random lavalamp
    hashedImage = sha1(open("opencv_frame_2.png", 'rb').read()).hexdigest()
    rng = np.random.default_rng(int(hashedImage, 16)+n)
    rint = rng.integers(low=Low, high=High, size=Size)

    return list(rint)

def boink():
    save_seed(load_seed()+1)


#print(generateNumber(0, 10, 10, load_seed()))
#print(load_seed())


hashedImage = sha1(open("opencv_frame_2.png", 'rb').read()).hexdigest()
rng = np.random.default_rng(int(hashedImage, 16)+load_seed())
rint = rng.integers(low=1, high=2, size=1)
print(rint)

print(load_seed())

