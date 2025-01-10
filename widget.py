# This Python file uses the following encoding: utf-8
import os
import shutil  # 用于文件复制
import sys
import ffmpeg
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from funasr import AutoModel
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from form import Ui_Widget
import subprocess
from datetime import timedelta, datetime
import threading
import queue
import json
from pydub import AudioSegment
from modelscope.pipelines import pipeline

from modelscope.utils.constant import Tasks


inference_pipeline_2 = pipeline(
    task=Tasks.auto_speech_recognition,
    model='C:\\Users\\13714\\.cache\\modelscope\\hub\\iic\\speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch',
    model_revision="v2.0.4")

inference_pipeline_3 = pipeline(
    Tasks.acoustic_noise_suppression,
    model='C:\\Users\\13714\\.cache\\modelscope\\hub\\iic\\speech_frcrn_ans_cirm_16k')

inference_pipeline = pipeline(
    task=Tasks.emotion_recognition,
    model='C:\\Users\\13714\\.cache\\modelscope\\hub\\iic\\emotion2vec_plus_large')


sv_pipeline = pipeline(
    task='speaker-verification',
    model='C:\\Users\\13714\\.cache\\modelscope\\hub\\iic\\speech_eres2net_sv_zh-cn_16k-common',
    model_revision='v1.0.5'
)


home_directory = os.path.expanduser("~")
asr_model_path = os.path.join(home_directory, ".cache", "modelscope", "hub", "iic", "speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch")
asr_model_revision = "v2.0.4"
vad_model_path = os.path.join(home_directory, ".cache", "modelscope", "hub", "iic", "speech_fsmn_vad_zh-cn-16k-common-pytorch")
vad_model_revision = "v2.0.4"
punc_model_path = os.path.join(home_directory, ".cache", "modelscope", "hub", "iic", "punc_ct-transformer_zh-cn-common-vocab272727-pytorch")
punc_model_revision = "v2.0.4"
spk_model_path = os.path.join(home_directory, ".cache", "modelscope", "hub", "iic", "speech_campplus_sv_zh-cn_16k-common")
spk_model_revision = "v2.0.4"
spk2_model_path = os.path.join(home_directory, ".cache", "modelscope", "hub", "iic", "speech_eres2net_sv_zh-cn_16k-common")
spk2_model_revision = "v2.0.4"




ngpu = 1
device = "cuda"
ncpu = 4

# ASR 模型
model = AutoModel(model=asr_model_path,
                  model_revision = asr_model_revision,
                  vad_model=vad_model_path,
                  vad_model_revision=vad_model_revision,
                  punc_model=punc_model_path,
                  punc_model_revision=punc_model_revision,
                  spk_model=spk_model_path,
                  spk_model_revision = spk_model_revision,
                  ngpu=ngpu,
                  ncpu=ncpu,
                  device=device,
                  disable_pbar=True,
                  disable_log=True,
                  disable_update=True
                  )
result_queue = queue.Queue()



def save_audio_to_file(audio_bytes, output_path):
    with open(output_path, 'wb') as f:
        f.write(audio_bytes)


def convert_to_wav(input_file, output_file, sample_rate=16000):
    """
    使用 ffmpeg 将输入文件转换为 WAV 格式，并设置采样率
    :param input_file: 输入文件路径
    :param output_file: 输出文件路径
    :param sample_rate: 采样率，默认为 16000 Hz
    """
    command = [
        'ffmpeg',
        '-i', input_file,  # 输入文件
        '-ar', str(sample_rate),  # 设置采样率
        '-ac', '1',  # 单声道
        '-acodec', 'pcm_s16le',  # 16-bit PCM 编码
        output_file  # 输出文件
    ]

    try:
        subprocess.run(command, check=True)
        print(f"文件已成功转换为 {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {e}")
        QMessageBox.critical(None, "错误", f"转换失败: {e}")
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.partition_widget3)
        self.ui.pushButton_2.clicked.connect(self.pretreatment_widget4)
        self.ui.pushButton_3.clicked.connect(self.identify_tabwidget)
        self.ui.pushButton_4.clicked.connect(self.select_multi_file)
        self.ui.pushButton_5.clicked.connect(self.savefile)
        self.ui.pushButton_6.clicked.connect(self.start_transcription_thread)
        self.ui.pushButton_7.clicked.connect(self.select_input_folder)
        self.ui.pushButton_8.clicked.connect(self.select_output_folder)
        self.ui.pushButton_9.clicked.connect(self.qingganshibie)
        self.ui.pushButton_10.clicked.connect(self.process_files)
        self.ui.pushButton_11.clicked.connect(self.select_audio_file_1)
        self.ui.pushButton_12.clicked.connect(self.select_audio_file_2)
        self.ui.pushButton_13.clicked.connect(self.savepath)
        self.ui.pushButton_14.clicked.connect(self.process_folder)
        self.ui.pushButton_15.clicked.connect(self.yuyingshibie)
        self.ui.pushButton_16.clicked.connect(self.select_qingganaudio)
        self.ui.pushButton_17.clicked.connect(self.savepath_qinggan)
        self.ui.pushButton_18.clicked.connect(self.qidong_qinggan)
        self.ui.pushButton_19.clicked.connect(self.select_yuyingaudio)
        self.ui.pushButton_20.clicked.connect(self.savepath_yuying)
        self.ui.pushButton_21.clicked.connect(self.qidong_yuying)
        self.ui.pushButton_22.clicked.connect(self.jiangzao)
        self.ui.pushButton_24.clicked.connect(self.save_jiangzao)
        self.ui.pushButton_23.clicked.connect(self.choose_jiangzao)
        self.ui.pushButton_25.clicked.connect(self.qidong_jiangzao)
        self.ui.pushButton_26.clicked.connect(self.shichangfenge)
        self.ui.pushButton_27.clicked.connect(self.select_shichangfenge)
        self.ui.pushButton_28.clicked.connect(self.save_shichangfenge)
        self.ui.pushButton_29.clicked.connect(self.split_audio)
        self.selected_file_list = []


# 选择需要分离的音频


    def partition_widget3(self):
        self.ui.widget_3.show()
        self.ui.widget_4.close()
        self.ui.tabWidget.close()
        self.ui.widget_5.close()
        self.ui.widget_6.close()
        self.ui.widget_7.close()
        self.ui.widget_8.close()

    def pretreatment_widget4(self):
        self.ui.widget_3.close()
        self.ui.widget_4.show()
        self.ui.tabWidget.close()
        self.ui.widget_5.close()
        self.ui.widget_6.close()
        self.ui.widget_7.close()
        self.ui.widget_8.close()


    def identify_tabwidget(self):
        self.ui.widget_3.close()
        self.ui.widget_4.close()
        self.ui.tabWidget.show()
        self.ui.widget_5.close()
        self.ui.widget_6.close()
        self.ui.widget_7.close()
        self.ui.widget_8.close()

    def qingganshibie(self ):
        self.ui.widget_3.close()
        self.ui.widget_4.close()
        self.ui.tabWidget.close()
        self.ui.widget_5.show()
        self.ui.widget_6.close()
        self.ui.widget_7.close()
        self.ui.widget_8.close()

    def yuyingshibie(self):
        self.ui.widget_3.close()
        self.ui.widget_4.close()
        self.ui.tabWidget.close()
        self.ui.widget_5.close()
        self.ui.widget_6.show()
        self.ui.widget_7.close()
        self.ui.widget_8.close()
    def jiangzao(self):
        self.ui.widget_3.close()
        self.ui.widget_4.close()
        self.ui.tabWidget.close()
        self.ui.widget_5.close()
        self.ui.widget_6.close()
        self.ui.widget_7.show()
        self.ui.widget_8.close()

    def shichangfenge(self):
        self.ui.widget_3.close()
        self.ui.widget_4.close()
        self.ui.tabWidget.close()
        self.ui.widget_5.close()
        self.ui.widget_6.close()
        self.ui.widget_7.close()
        self.ui.widget_8.show()


    def select_multi_file(self):
        self.selected_file_list.clear()
        # 使用 getOpenFileNames 替代 askopenfilenames
        selected_files, _ = QFileDialog.getOpenFileNames(
            self,
            '选择多个文件',
            filter='音频文件 (*.mp3 *.wav *.ogg *.flac *.aac);;视频文件 (*.mp4 *.avi *.mov *.mkv)'
        )
        for tmp_file in selected_files:
            self.selected_file_list.append(tmp_file)
            print(f"选择的音频或视频：{tmp_file}")
        if selected_files:
            # 使用换行符将文件路径连接成一个字符串
            files_str = '\n'.join(selected_files)
            self.ui.label.setText(files_str)
    def savefile(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            self.ui.label_2.setText(folder_path)

    def start_transcription_thread(self):
        # 创建并启动转写线程
        thread = threading.Thread(target=self.trans)
        thread.start()

    def trans(self):

        save_path = self.ui.label_2.text().strip()
        if len(self.selected_file_list) != 0 and save_path != '' and save_path is not None:
            for audio in self.selected_file_list:
                if os.path.exists(audio):
                    audio_name = os.path.splitext(os.path.basename(audio))[0]
                    _, audio_extension = os.path.splitext(audio)
                    self.ui.label_10.setText(f'正在执行中，请勿关闭程序。{audio}')
                    # 音频预处理
                    try:
                        audio_bytes, _ = (
                            ffmpeg.input(audio, threads=0, hwaccel='cuda')
                            .output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=16000)
                            .run(cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True)
                        )
                        res = model.generate(input=audio_bytes, batch_size_s=300, is_final=True,
                                             sentence_timestamp=True)
                        print(res)
                        rec_result = res[0]
                        asr_result_text = rec_result['text']
                        if asr_result_text != '':
                            sentences = []
                            for sentence in rec_result["sentence_info"]:
                                start = to_date(sentence["start"])
                                end = to_date(sentence["end"])
                                if sentences and sentence["spk"] == sentences[-1]["spk"]:
                                    sentences[-1]["text"] += "" + sentence["text"]
                                    sentences[-1]["end"] = end
                                else:
                                    sentences.append(
                                        {"text": sentence["text"], "start": start, "end": end,
                                            "spk": sentence["spk"]}
                                    )

                            # 剪切音频或视频片段
                            i = 0
                            for stn in sentences:
                                start = stn['start']
                                end = stn['end']
                                tmp_start = to_milliseconds(start)
                                tmp_end = to_milliseconds(end)
                                duration = (tmp_end - tmp_start) / 1000
                                spk = stn['spk']
                                # 根据文件名和 spk 创建目录
                                final_save_path = os.path.join(save_path, datetime.now().strftime("%Y-%m-%d"), audio_name, str(spk))
                                os.makedirs(final_save_path, exist_ok=True)
                                final_save_file = os.path.join(str(final_save_path), str(i) + '.mp3')
                                i += 1
                                print(f"final_save_file: {final_save_file}")
                                try:
                                    (
                                        ffmpeg.input(audio, threads=0, ss=start, t=duration, hwaccel='cuda')
                                        .output(final_save_file, codec='libmp3lame', preset='medium')
                                        .run(cmd=["ffmpeg", "-nostdin"], overwrite_output=True, capture_stdout=True, capture_stderr=True)
                                    )
                                except ffmpeg.Error as e:
                                    print(f"剪切音频发生错误，错误信息：{e}")
                            ret = {"text": asr_result_text, "sentences": sentences}
                            print(f'{audio} 切分完成')
                            result_queue.put(f'{audio} 切分完成')
                            self.ui.label_10.setText(f'{audio} 切分完成')
                            print(f'转写结果：{ret}')
                        else:
                            print("没有转写结果")
                    except Exception as e:
                        print(f"转写异常：{e}")
                else:
                    print("输入的文件不存在")
                    QMessageBox.information(self,"提醒","输入的文件不存在")
        else:
            print("没有填写输入输出")
            QMessageBox.information(self, "提醒", "没有填写选择文件或保存路径")

    def select_input_folder(self):
        input_folder = QFileDialog.getExistingDirectory(self, "选择输入文件夹")
        if input_folder:
            self.ui.label_3.setText(input_folder)

    def select_output_folder(self):
        output_folder = QFileDialog.getExistingDirectory(self, "选择输出文件夹")
        if output_folder:
            self.ui.label_9.setText(output_folder)

    def process_files(self):
        input_folder = self.ui.label_3.text().strip()
        output_folder = self.ui.label_9.text().strip()
        if not input_folder or not output_folder:
            QMessageBox.critical(self, "错误", "请选择输入和输出文件夹")
            return

        # 确保输出文件夹存在
        os.makedirs(output_folder, exist_ok=True)

        supported_formats = ('.mp3', '.wav', '.ogg', '.flac', '.aac')
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(supported_formats):
                input_file = os.path.join(input_folder, filename)
                output_filename = os.path.splitext(os.path.basename(filename))[0] + '.wav'
                output_file = os.path.join(output_folder, output_filename)
                convert_to_wav(input_file, output_file)

        QMessageBox.information(self, "信息", "预处理完成")



    def select_audio_file_1(self):
        # 打开文件对话框选择音频文件
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择语音文件", "",
                                                   "Audio Files (*.wav *.mp3 *.ogg);;All Files (*)")

        if file_path:
            # 将文件路径显示在标签上
            self.ui.label_4.setText(file_path)



    def select_audio_file_2(self):
        # 打开文件对话框选择文件夹
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "")

        if folder_path:
            # 将文件夹路径显示在标签上
            self.ui.label_5.setText(folder_path)

    def savepath(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            self.ui.label_6.setText(folder_path)

    def process_folder(self):
        folder_path = self.ui.label_5.text().strip()
        target_folder = self.ui.label_6.text().strip()
        target_name = self.ui.lineEdit_4.text().strip()

        if not target_folder or not target_name:
            QMessageBox.critical(self, '错误', '目标文件夹或目标文件名为空，请检查输入。')
            return

        audio_files = [f for f in os.listdir(folder_path) if f.endswith(('.wav', '.mp3', '.ogg'))]

        for audio_file in audio_files:
            audio1_path = os.path.join(folder_path, audio_file)
            audio2_path = self.ui.label_4.text().strip()

            if not audio2_path:
                QMessageBox.critical(self, '错误', '请先选择需要对比的语音文件。')
                return

            result = sv_pipeline([audio2_path, audio1_path], output_emb=True)
            resultlast = check_last_string(result)
            print(resultlast)

            if resultlast:
                target_file_path = os.path.join(target_folder, f"{target_name}_{audio_file}")
                try:
                    # 保存预处理后的音频文件到目标文件夹
                    shutil.copy(audio1_path, target_file_path)
                    QMessageBox.information(self, '信息', f'语音文件 {audio_file} 已成功保存到指定文件夹！')
                except Exception as e:
                    QMessageBox.critical(self, '错误', f'保存语音文件 {audio_file} 时出错：{e}')
    def qidong(self):
        audio1_path = self.ui.label_4.text()
        audio2_path = self.ui.label_5.text()
        if not audio1_path or not audio2_path:
            print("音频文件路径未正确设置")
            return

        result = sv_pipeline([audio1_path, audio2_path], output_emb=True)
        resultlast = check_last_string(result)
        print(resultlast)
        if resultlast:
            QMessageBox.information(self, "结果", "两段语音是同一个人发出！")
            # 获取目标文件名（这里简单地使用原文件名，但您可以根据需要修改）
            file_info = self.ui.label_2.text().strip()  # 去除前后空白
            folder_path = self.ui.label_3.text().strip()  # 去除前后空白
            target_file_name = self.ui.lineEdit.text().strip()  # 去除前后空白
            if not file_info or not folder_path or not target_file_name:
                QMessageBox.critical(self, '错误', '文件路径或目标文件名为空，请检查输入。')
                return
            target_file_path = os.path.join(folder_path, target_file_name)

            try:
                # 复制文件到目标文件夹
                # 确保 file_info 和 target_file_path 是字符串
                file_info = str(file_info)
                target_file_path = str(target_file_path)
                shutil.copy(file_info, target_file_path)
                QMessageBox.information(self, '信息', '语音文件已成功保存到指定文件夹！')
            except Exception as e:
                QMessageBox.critical(self, '错误', f'保存语音文件时出错：{e}')
        else:
            QMessageBox.information(self, '信息', '条件不满足，未保存语音文件。')

    def select_qingganaudio(self):
        # 打开文件对话框选择音频文件
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择语音文件", "",
                                                   "Audio Files (*.wav *.mp3 *.ogg);;All Files (*)")

        if file_path:
            # 将文件路径显示在标签上
            self.ui.label_14.setText(file_path)
    def savepath_qinggan(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            self.ui.label_15.setText(folder_path)

    def qidong_qinggan(self):
        audio1_path = self.ui.label_14.text()
        rec_result = inference_pipeline(
            [audio1_path],
            granularity="utterance", extract_embedding=False)
        print(rec_result)

        # 获取 label_15 的文件夹路径
        folder_path = self.ui.label_15.text()

        # 获取 label_14 的文件名（不包括路径）
        file_name = os.path.basename(audio1_path)
        # 去掉文件扩展名，添加新的扩展名（例如 .txt）
        base_name, _ = os.path.splitext(file_name)
        output_file_name = f"{base_name}.txt"
        output_file_path = os.path.join(folder_path, output_file_name)

        # 确保文件夹存在
        os.makedirs(folder_path, exist_ok=True)

        # 将 rec_result 保存为文本文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(rec_result, ensure_ascii=False, indent=4))

            QMessageBox.information(self, '信息', '文本文件已成功保存到指定文件夹！')

    def select_yuyingaudio(self):
        # 打开文件对话框选择音频文件
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择语音文件", "",
                                                   "Audio Files (*.wav *.mp3 *.ogg);;All Files (*)")

        if file_path:
            # 将文件路径显示在标签上
            self.ui.label_16.setText(file_path)

    def savepath_yuying(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            self.ui.label_17.setText(folder_path)

    def qidong_yuying(self):
        audio1_path = self.ui.label_16.text()
        rec_result = inference_pipeline_2(
            [audio1_path],
            granularity="utterance", extract_embedding=False)
        print(rec_result)

        # 获取 label_15 的文件夹路径
        folder_path = self.ui.label_17.text()

        # 获取 label_14 的文件名（不包括路径）
        file_name = os.path.basename(audio1_path)
        # 去掉文件扩展名，添加新的扩展名（例如 .txt）
        base_name, _ = os.path.splitext(file_name)
        output_file_name = f"{base_name}.txt"
        output_file_path = os.path.join(folder_path, output_file_name)

        # 确保文件夹存在
        os.makedirs(folder_path, exist_ok=True)

        # 将 rec_result 保存为文本文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(rec_result, ensure_ascii=False, indent=4))

            QMessageBox.information(self, '信息', '文本文件已成功保存到指定文件夹！')

    def choose_jiangzao(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择音频文件", "",
                                                   "Audio Files (*.wav *.mp3 *.ogg);;All Files (*)")
        if file_path:
            self.ui.label_18.setText(file_path)

    def save_jiangzao(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            self.ui.label_19.setText(folder_path)

    def qidong_jiangzao(self):
        audio1_path = self.ui.label_18.text()
        rec_result = inference_pipeline_3(
            [audio1_path],
            granularity="utterance", extract_embedding=False)
        print(rec_result)
        # 获取 label_15 的文件夹路径
        folder_path = self.ui.label_19.text()

        # 获取 label_14 的文件名（不包括路径）
        file_name = os.path.basename(audio1_path)
        # 去掉文件扩展名，添加新的扩展名（例如 .txt）
        base_name, _ = os.path.splitext(file_name)
        output_file_name = f"{base_name}.txt"
        output_file_path = os.path.join(folder_path, output_file_name)

        # 确保文件夹存在
        os.makedirs(folder_path, exist_ok=True)

        # 将 rec_result 保存为文本文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(rec_result, ensure_ascii=False, indent=4))

            QMessageBox.information(self, '信息', '文本文件已成功保存到指定文件夹！')

    def select_shichangfenge(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择音频文件", "",
                                                   "Audio Files (*.wav *.mp3 *.ogg);;All Files (*)")
        if file_path:
            self.ui.label_20.setText(file_path)

    def save_shichangfenge(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            self.ui.label_21.setText(folder_path)

    def split_audio(self):
        if not self.ui.label_20.text():
            QMessageBox.warning(self, "警告", "请先选择一个音频文件。")
            return

        try:
            duration_minutes = float(self.ui.lineEdit_5.text())
            if duration_minutes <= 0:
                raise ValueError("时长必须是正数。")
        except ValueError:
            QMessageBox.warning(self, "警告", "请输入一个有效的正数作为时长。")
            return

        segment_length_ms = int(duration_minutes * 60 * 1000)
        output_folder = self.ui.label_21.text()

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        try:
            audio = AudioSegment.from_file(self.ui.label_20.text())
            total_length = len(audio)
            num_segments = total_length // segment_length_ms
            if total_length % segment_length_ms != 0:
                num_segments += 1

            for i in range(num_segments):
                start_time = i * segment_length_ms
                end_time = (i + 1) * segment_length_ms
                segment = audio[start_time:end_time]
                output_file = os.path.join(output_folder, f"segment_{i + 1}.mp3")
                segment.export(output_file, format="mp3")

            self.ui.label_22.setText(f"音频已成功分割为 {num_segments} 段。")
            QMessageBox.information(self, "成功", f"音频已成功分割为 {num_segments} 段。")
        except Exception as e:
            self.ui.label_22.setText(f"错误: {str(e)}")
            QMessageBox.critical(self, "错误", f"发生错误: {str(e)}")









def check_last_string(result):
    # 打印 result 结构以调试
    print(f"Result: {result}")

    if 'outputs' in result and isinstance(result['outputs'], dict):
        score = result['outputs'].get('score')
        text_value = result['outputs'].get('text')

        if score is not None and score < 0.5:
            return 0
        elif score > 0.5:
            return 1
    return 0


def to_date(milliseconds):
    """将时间戳转换为SRT格式的时间"""
    time_obj = timedelta(milliseconds=milliseconds)
    return f"{time_obj.seconds // 3600:02d}:{(time_obj.seconds // 60) % 60:02d}:{time_obj.seconds % 60:02d}.{time_obj.microseconds // 1000:03d}"
def to_milliseconds(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M:%S.%f")
    time_delta = time_obj - datetime(1900, 1, 1)
    milliseconds = int(time_delta.total_seconds() * 1000)
    return milliseconds









if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
