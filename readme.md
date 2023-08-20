## 使用
0. pip install -r requirements.txt
1. 将 .env.example 复制成 .env
2. 配置.env
3. python main.py {filename 文件名}


## 手动调试
0. 使用pycharm配置conda环境，python3.7
1. pip3 install torch torchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple
2. pip install modelscope -i https://pypi.tuna.tsinghua.edu.cn/simple
3. pip3 install transformers -i https://pypi.tuna.tsinghua.edu.cn/simple
4. pip3 install opencv_python -i https://pypi.tuna.tsinghua.edu.cn/simple
5. pip install --upgrade tensorflow==1.15 -i https://pypi.tuna.tsinghua.edu.cn/simple  （分GPU tensorflow-gpu/CPU tensorflow）
6. pip install protobuf==3.20 -i https://pypi.tuna.tsinghua.edu.cn/simple
7. pip install python-dotenv -i https://pypi.tuna.tsinghua.edu.cn/simple
8. pip install timm -i https://pypi.tuna.tsinghua.edu.cn/simple

## 效果
![example](https://raw.githubusercontent.com/ouhaohan8023/AICV/main/images/example.png)