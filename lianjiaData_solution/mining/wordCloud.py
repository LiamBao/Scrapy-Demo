#-*- coding=utf8-*-

import jieba
import WordCloud
import matplotlib.pyplot as plt
import numpy as np



class Image():
    data = []
    jieba.analyse.set_stop_words("./stop.txt")

    with codecs.open("lianjiaData.csv", 'r', encoding="utf-8") as f:
        for text in f.readlines():
            data.extend(jieba.analyse.extract_tags(text, topK=20))
        data = " ".join(data)
        mask_img = imread('./lianjiaImg.jpg', flatten=True)
        wordcloud = WordCloud(
            font_path='msyh.ttc',
            background_color='white',
            mask=mask_img
        ).generate(data)
        plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3),
                   interpolation="bilinear")
        plt.axis('off')
        plt.savefig('./heart2.jpg', dpi=1600)



