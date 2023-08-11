import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

# DDColor 图像上色模型
img_colorization = pipeline(Tasks.image_colorization,
                            model='damo/cv_ddcolor_image-colorization', device="cpu")
img_path = 'images/2.png'
result = img_colorization(img_path)
cv2.imwrite('images/denoiseing-enhance-color2.png', result[OutputKeys.OUTPUT_IMG])
