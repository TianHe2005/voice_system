from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import subprocess
import os

# 使用 ffmpeg 转换音频文件
input_file = r'C:\Users\HP\PycharmProjects\PythonProject1\123.wav'
output_file = r'C:\Users\HP\PycharmProjects\PythonProject1\output\1234.wav'

# 确保输出目录存在
output_dir = os.path.dirname(output_file)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 构建 ffmpeg 命令，使用绝对路径
ffmpeg_path = r'C:\ffmpeg\bin\ffmpeg.exe'
command = [
    ffmpeg_path,
    '-i', input_file,
    '-ar', '16000',
    '-ac', '1',
    output_file
]

# 执行 ffmpeg 命令
try:
    subprocess.run(command, check=True)
    print(f"Successfully converted {input_file} to {output_file}")
except subprocess.CalledProcessError as e:
    print(f"Error converting file: {e}")
