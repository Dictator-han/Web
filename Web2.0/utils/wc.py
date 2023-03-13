from wordcloud import WordCloud
import os

def get_word_cloud(text):
        wc = WordCloud(
            collocations=False, #去除重复词
            font_path='simhei.ttf',  # 字体
            background_color='white',
            width=1000,
            height=800,
            max_font_size=50,
            max_words=1000
        )
        wc.generate(text)
        wc.to_file(os.path.abspath("static/img/res.png"))
        return 1