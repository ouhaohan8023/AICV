import cv2
import sys
import os
from modelscope.pipelines import pipeline
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()
# 获取环境变量的值
input_file_path = os.getenv('INPUT_FILE_PATH', './')
out_file_path = os.getenv('OUT_FILE_PATH', './')

def enhance_func(fileName):
    # 图像增强（人像修复） GPEN人像修复增强
    portrait_matting = pipeline('image-portrait-enhancement', 'damo/cv_gpen_image-portrait-enhancement', device="cpu")
    result = portrait_matting(input_file_path + "/" + fileName)
    cv2.imwrite(out_file_path + "/" + fileName, result['output_img'])
    return fileName


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_image_path")
        sys.exit(1)

    file_name = sys.argv[1]
    enhanced_url = enhance_func(file_name)
    print("Input File Path:", input_file_path)
    print("Output File Path:", out_file_path)
    print("File Name:", file_name)
    print("Enhanced image Name:", enhanced_url)

