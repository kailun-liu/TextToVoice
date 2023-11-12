# 會使用 os 模組透過 system 函數來執行系統指令
import os
# 使用 google cloud 的 texttospeech 進行轉換
from google.cloud import texttospeech

# 初始化 Google Text-to-Speech client
tts_client = texttospeech.TextToSpeechClient()

# 自訂一個轉換函數
def text_to_speech(text):
    # 
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # 設置語音參數
    voice_params = texttospeech.VoiceSelectionParams(
        language_code='cmn-Hant-TW', # 設定語言
        name='cmn-TW-Wavenet-C',    # 男生
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

    # 設置音頻輸出格式
    audio_config = texttospeech.AudioConfig(
        # LINEAR16 是 PCM 格式，適用於樹莓派
        audio_encoding=texttospeech.AudioEncoding.LINEAR16)  

    # 生成語音
    response = tts_client.synthesize_speech(
        input=synthesis_input, 
        voice=voice_params, 
        audio_config=audio_config)

    # 將回復的音頻內容寫入文件
    with open('output.wav', 'wb') as audio_file:
        audio_file.write(response.audio_content)
        print('音頻內容已寫入檔案 "output.wav"')
    # 這個函數會傳出一個檔案
    return 'output.wav'

def play_audio(file_name):
    # 播放音頻文件
    os.system(f"aplay {file_name}")

def main():
    # 捕捉過程中可能拋出的錯誤，讓程序可以更優雅
    try:
        # 無窮迴圈
        while True:
            # 使用者輸入
            text = input("請輸入要轉換為語音的文字內容，然後按下Enter：")
            # 去除頭尾空白
            if text.strip() == "":
                print("請注意，您沒有輸入任何文字。")
                # 使用 continue 進入下一輪迴圈
                continue
            
            # 假如有內容就會執行到這裡進行文字轉語音
            print("正在轉換文本到語音...")
            audio_file = text_to_speech(text)
            # 轉換完成進行播放
            print("正在播放語音...")
            play_audio(audio_file)
            # 播放後，使用者可以決定要繼續還是退出
            user_input = input("輸入 'exit' 退出，或按 Enter 繼續：").lower()
            if user_input == 'exit':
                print("退出程序")
                break
    except KeyboardInterrupt:
        print("用戶已經中斷程序")
    except Exception as e:
        print(f"程序發生錯誤：{e}")

if __name__ == "__main__":
    main()