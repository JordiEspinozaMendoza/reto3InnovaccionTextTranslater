
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import os
from decouple import config

cog_key = config('cog_key')
cog_endpoint = config('cog_endpoint')

# print('Ready to use cognitive services at {} using key {}'.format(cog_endpoint, cog_key))
# Get a client for the computer vision service
computervision_client = ComputerVisionClient(cog_endpoint, CognitiveServicesCredentials(cog_key))

# Read the image file
def textTranlater(url):
    # image_path = os.path.join()
    # image_stream = open(url)

    # Use the Computer Vision service to find text in the image
    read_results = computervision_client.recognize_printed_text(url)

    result = ""
    # Process the text line by line
    for region in read_results.regions:
        for line in region.lines:

            # Read the words in the line of text
            line_text = ''
            for word in line.words:
                line_text += word.text + ' '
                result += word.text+' '
            print(line_text.rstrip())
    return result

# # Open image to display it.
# fig = plt.figure(figsize=(7, 7))
# img = Image.open(image_path)
# draw = ImageDraw.Draw(img)
# plt.axis('off')
# plt.imshow(img)