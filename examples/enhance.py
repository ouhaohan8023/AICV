import cv2
from modelscope.pipelines import pipeline

# 图像增强（人像修复） GPEN人像修复增强 result3
portrait_matting = pipeline('image-portrait-enhancement', 'damo/cv_gpen_image-portrait-enhancement', device="cpu")

# GPEN人像增强修复-大分辨率人脸 result2
# portrait_matting = pipeline('image-portrait-enhancement', 'damo/cv_gpen_image-portrait-enhancement-hires', device="cpu")


result = portrait_matting('images/2.png')
cv2.imwrite('images/denoiseing-enhance.png', result['output_img'])
