from gensim.models import Word2Vec
from gensim.models.word2vec import  LineSentence
import multiprocessing
import os
os.chdir(r"中文语义")
import glob
txt_out_list = glob.glob("*.txtout")
yuliao = open("WXNovel.input","w",encoding='utf-8')
for txt_out in txt_out_list:
    with open(txt_out,encoding='utf8') as f:
        novel_content = f.read()
        yuliao.write(novel_content)
yuliao.close()
model = Word2Vec(LineSentence("WXNovel.input"),size=400,workers=multiprocessing.cpu_count())
model.save("WXNovel.model")
# model.save_word2vec_format("WXNovelOriginal.model",binary=False)
model.wv.save_word2vec_format("WXNovelOriginal.model",binary=False)
