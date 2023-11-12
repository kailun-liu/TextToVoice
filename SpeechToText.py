import speech_recognition as sr
import numpy as np
import soundfile as sf

# 初始化語音識別器
recognizer = sr.Recognizer()

# 載入音頻文件
def load_audio_file(file_path):
    try:
        # 使用 soundfile 從文件讀取音頻數據
        audio_data, sample_rate = sf.read(file_path, dtype='int16')
        return audio_data, sample_rate
    except Exception as e:
        print(f"讀取音頻文件過程中發生錯誤: {e}")
        return None, None

# 識別音頻
def recognize_audio(audio_data, sample_rate):
    # 將numpy陣列轉換為音頻數據
    audio = sr.AudioData(np.array(audio_data, dtype=np.int16).tobytes(), sample_rate, 2)
    try:
        # 使用Google的API進行語音識別
        text = recognizer.recognize_google(audio, language='zh-TW')
        print("識別結果： " + text)
    except sr.UnknownValueError:
        print("無法理解音頻內容")
    except sr.RequestError as e:
        print(f"無法從Google語音識別服務獲取結果; {e}")

if __name__ == "__main__":
    # 替換為指定的音頻文件
    audio_file_path = './output.wav'  
    # 調用自訂的 load_audio_file() 函數，傳入音頻文件
    audio_data, sample_rate = load_audio_file(audio_file_path)
    # 確保文件存在
    if audio_data is not None:
        # 調用自訂的 recognize_audio() 進行識別
        recognize_audio(audio_data, sample_rate)