import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, \
    QFileDialog, QMessageBox
from PySide6.QtCore import Qt
import soundfile as sf
import torch
import torchaudio
from concurrent.futures import ThreadPoolExecutor

class AudioSplitterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("音频分割器")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("选择一个音频文件并设置分割时长：")
        self.layout.addWidget(self.label)

        self.file_button = QPushButton("选择音频文件")
        self.file_button.clicked.connect(self.select_audio_file)
        self.layout.addWidget(self.file_button)

        self.file_label = QLabel("未选择文件")
        self.layout.addWidget(self.file_label)

        self.duration_label = QLabel("分割时长（分钟）：")
        self.layout.addWidget(self.duration_label)

        self.duration_input = QLineEdit()
        self.duration_input.setPlaceholderText("例如，30")
        self.layout.addWidget(self.duration_input)

        self.split_button = QPushButton("分割音频")
        self.split_button.clicked.connect(self.split_audio)
        self.layout.addWidget(self.split_button)

        self.status_label = QLabel("")
        self.layout.addWidget(self.status_label)

        self.audio_file_path = ""

    def select_audio_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("音频文件 (*.mp3 *.wav *.flac)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.audio_file_path = selected_files[0]
                self.file_label.setText(f"已选择文件: {os.path.basename(self.audio_file_path)}")

    def split_audio(self):
        if not self.audio_file_path:
            QMessageBox.warning(self, "警告", "请先选择一个音频文件。")
            return

        try:
            duration_minutes = float(self.duration_input.text())
            if duration_minutes <= 0:
                raise ValueError("时长必须是正数。")
        except ValueError:
            QMessageBox.warning(self, "警告", "请输入一个有效的正数作为时长。")
            return

        segment_length_ms = int(duration_minutes * 60 * 1000)
        output_folder = "output_segments"

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        try:
            # 使用 soundfile 加载音频文件
            audio, sr = sf.read(self.audio_file_path)
            total_length = len(audio) * 1000 / sr
            num_segments = int(total_length // segment_length_ms)
            if total_length % segment_length_ms != 0:
                num_segments += 1

            # 使用多线程处理
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = []
                for i in range(num_segments):
                    start_time = i * segment_length_ms
                    end_time = (i + 1) * segment_length_ms
                    output_file = os.path.join(output_folder, f"segment_{i + 1}.mp3")
                    futures.append(executor.submit(self.export_segment, self.audio_file_path, sr, start_time, end_time,
                                                   output_file))

                for future in futures:
                    future.result()  # 等待所有线程完成

            self.status_label.setText(f"音频已成功分割为 {num_segments} 段。")
            QMessageBox.information(self, "成功", f"音频已成功分割为 {num_segments} 段。")
        except Exception as e:
            self.status_label.setText(f"错误: {str(e)}")
            QMessageBox.critical(self, "错误", f"发生错误: {str(e)}")

    def export_segment(self, audio_file_path, sr, start_time, end_time, output_file):
        # 使用 soundfile 分块加载音频
        start_sample = int(start_time * sr / 1000)
        end_sample = int(end_time * sr / 1000)
        audio, _ = sf.read(audio_file_path, start=start_sample, stop=end_sample)

        # 将音频数据转换为 tensor 并使用 torchaudio 导出
        audio_tensor = torch.tensor(audio, dtype=torch.float32).unsqueeze(0)
        torchaudio.save(output_file, audio_tensor, sample_rate=sr)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioSplitterApp()
    window.show()
    sys.exit(app.exec())
