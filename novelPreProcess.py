import os

os.chdir(r"中文语义")
import glob
import jieba

with open("stopwords.dat",encoding="utf-8") as f:
    stop_words = f.read().split("\n")
txt_list = glob.glob("*.txt")
jieba.load_userdict("user-dictory.dic")
for txt_name in txt_list:
    print(txt_name)
    with open(txt_name, encoding="utf-8") as f:
        novel_content = f.read()
    with open(txt_name + "out", "w", encoding="utf-8") as f:
        for novel_line in novel_content.split("\n"):
            if len(novel_line) > 8:
                words = jieba.lcut(novel_line.strip(), cut_all=False)
                for word in words:
                    if word not in stop_words:
                        f.write(word+" ")
                f.write("\n")

import w2vTest
