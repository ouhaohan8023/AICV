import cv2
from modelscope.pipelines import pipeline

# 图像分割
portrait_matting = pipeline('portrait-matting', device="cpu")
result = portrait_matting('https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/image_matting.png')
cv2.imwrite('images/result.png', result['output_img'])