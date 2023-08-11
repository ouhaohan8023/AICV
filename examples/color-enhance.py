import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

img = 'images/2.png'
image_color_enhance = pipeline(Tasks.image_color_enhancement,
                               model='damo/cv_csrnet_image-color-enhance-models', device="cpu")
result = image_color_enhance(img)
cv2.imwrite('images/denoiseing-enhance-color-enhance.png', result[OutputKeys.OUTPUT_IMG])