from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
# Author: Roman Duirs

if __name__ == '__main__':

    labels = get_pet_labels('pet_images')
    classify_images('pet_images',labels,'vgg')
    adjust_results4_isadog(labels, 'dognames.txt')
    for i,j in labels.items():
        print("="*50)
        print(i,":",j)