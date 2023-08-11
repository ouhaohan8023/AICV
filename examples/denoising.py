import cv2
from modelscope.pipelines import pipeline

# NAFNet图像去噪
p = pipeline('image-denoising', 'damo/cv_nafnet_image-denoise_sidd', device="cpu")
result = p('images/2.png')
cv2.imwrite('images/denoiseing2222.png', result['output_img'])