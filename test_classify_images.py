from get_pet_labels import get_pet_labels
from classify_images import classify_images
# Author: Roman Duirs

labels = get_pet_labels('pet_images')
classify_images('pet_images',labels,'vgg')
for i,j in labels.items():
    print("="*50)
    print(i,":",j)