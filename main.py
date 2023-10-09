# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
path = r'C:\Users\01szy\OneDrive\Obrazy\Zrzuty ekranu\Zrzut ekranu 2023-03-10 225702'
image = cv2.imread(path)
window_name =' nazwa '
cv2.imshow(window_name, image)
cv2.waitKey()
cv2.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
