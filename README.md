# 语音处理与分析系统

## 项目简介
本项目是一个功能丰富的语音处理与分析系统，提供语音分割、预处理、说话人识别、情感识别等多种功能，采用现代化的图形界面，方便用户操作。

## 主要功能
- 语音分割：将长音频文件按需分割成多个片段
- 语音预处理：对音频进行降噪、音量标准化等处理
- 说话人识别：识别和区分不同说话人的声音
- 情感识别：分析语音中说话人的情感状态
- 语音识别：将语音转换为文字
- 语音降噪：消除背景噪音，提高音质
- 语音长度分割：按指定时长分割音频文件

## 系统要求
- Python 3.8+
- Windows/Linux/MacOS

## 安装步骤
1. 克隆项目到本地：
```bash
git clone [项目地址]
cd [项目目录]
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用说明
1. 启动程序：
```bash
python widget.py
```

2. 使用界面：
- 在左侧功能栏选择需要的处理功能
- 按照界面提示选择输入文件/文件夹
- 设置相关参数
- 选择输出路径
- 点击开始处理

## 界面预览
系统提供了直观的图形界面，方便用户操作：
- 主界面：![1.png](https://github.com/TianHe2005/voice_system/blob/master/file/1.png)
- 语音分割界面：![2](https://github.com/TianHe2005/voice_system/blob/master/file/2.png)
- 说话人识别界面：![3](https://github.com/TianHe2005/voice_system/blob/master/file/3.png)
- 情感识别界面：![4](https://github.com/TianHe2005/voice_system/blob/master/file/4.png)
- 语音降噪界面：![5](https://github.com/TianHe2005/voice_system/blob/master/file/5.png)

## 核心模型介绍

### 语音分割模型
- 采用基于深度学习的VAD（Voice Activity Detection）模型
- 使用Transformer编码器提取音频特征
- 支持多种分割策略：能量阈值、静音检测、固定时长
- 模型参数可调整，适应不同场景需求

### 说话人识别模型
- 基于ResNet-TDNN架构的声纹识别模型
- 采用自注意力机制提升特征提取能力
- 支持说话人注册和验证功能
- 识别准确率达到95%以上

### 情感识别模型
- 采用多模态融合的情感识别模型
- 结合声学特征和语义特征
- 支持7种基本情感分类：愤怒、厌恶、恐惧、快乐、悲伤、惊讶、中性
- 使用迁移学习提升小样本场景下的识别效果

## 处理结果说明
处理后的结果将保存在以下位置：

### 语音分割结果
- 输出路径：output_segments/
- 分割后的音频片段：segment_*.mp3
- 分割信息记录：录音.txt

### 特征分析结果
- 存储位置：resource/
- 音频特征数据：45.txt
- 包含以下信息：
  - MFCC特征
  - 音高曲线
  - 能量分布
  - 说话人特征向量
  - 情感识别概率分布

## 项目结构
```
src/
├── ui/          # 用户界面相关代码
├── core/        # 核心业务逻辑
└── utils/       # 工具函数

input/          # 输入文件目录
output_segments/ # 输出文件目录
resource/       # 资源文件目录
```

## 技术栈
- PySide6：GUI界面开发
- librosa：音频处理
- PyTorch：深度学习框架
- transformers：预训练模型

## 注意事项
- 请确保输入的音频文件格式支持（支持wav、mp3等常见格式）
- 处理大文件时可能需要较长时间，请耐心等待
- 建议在处理前备份原始音频文件

## 许可证
MIT License

## 联系方式
如有问题或建议，请提交Issue或Pull Request。
