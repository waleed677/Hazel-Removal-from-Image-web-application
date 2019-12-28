from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import numpy as np


def index(request):
    # return HttpResponse('Hello from Images') 

    return render(request,'image/index.html')

def replace(request):
    text = "replaced"
    return render(request, 'image/index.html', {'text': text})


# Function to remove the hazel from the input image
def haze_removal(image, windowSize=24, w0=0.6, t0=0.1):

    darkImage = image.min(axis=2)
    maxDarkChannel = darkImage.max()
    darkImage = darkImage.astype(np.double)

    t = 1 - w0 * (darkImage / maxDarkChannel)
    T = t * 255
    T.dtype = 'uint8'

    t[t < t0] = t0

    J = image
    J[:, :, 0] = (image[:, :, 0] - (1 - t) * maxDarkChannel) / t
    J[:, :, 1] = (image[:, :, 1] - (1 - t) * maxDarkChannel) / t
    J[:, :, 2] = (image[:, :, 2] - (1 - t) * maxDarkChannel) / t
    result = Image.fromarray(J)
    #result.show()
    return result

def open_image(request):
    if request.method == 'POST':
        imageName = request.FILES['picture'].name
  
    image = np.array(Image.open('D:\image\static\image/' + imageName))  #location of the image folder
    result = haze_removal(image)
    result.save('image/static/image/my_pic.png')     # location of output image
    return render(request, 'image/result.html' ,{'image':imageName})
  