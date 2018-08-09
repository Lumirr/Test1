from os import path
import jieba.posseg as pseg
import jieba.analyse
import sys

def test():
    d =path.dirname(__file__) # __file__输出当前文件路径
    print(__file__)
    # print('d: ', d)

    # 提高分词准确率的一种方法：添加自定义词库
    # jieba.set_dictionary()
    # jieba.suggest_freq()
    # jieba.enable_parallel()
    # jieba.add_word()
    text_path = '高危职业_DangerousJob.txt' #/home/lumir/git/playForFun/test81/nltkTest/
    text = open(path.join(d, text_path), encoding='gbk').read()
    jieba.analyse.set_stop_words(path.join(d, 'discontinuation_words_list.txt'))
    for key, p in jieba.analyse.extract_tags(text, topK=50, withWeight=True):
        # print(key.encode('gbk'))
        print(key, p)

if __name__ == '__main__':
    test()
    # print(sys.version_info)
    str = '中文'
    str.deco
