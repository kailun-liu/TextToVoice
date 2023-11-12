# 引入庫
from gtts import gTTS

# 要轉換為語音的文本
text = "你好，歡迎使用語音辨識系統。"

# 選擇語言，中文是 zh-TW，英文是 en。
language = 'zh-TW'

# 建立一個 gTTS 實體
speech = gTTS(text=text, lang=language, slow=False)

# 將轉換結果保存到音頻檔案
speech.save("hello.mp3")