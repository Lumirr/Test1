#!usr/bin/env python
import jieba
import jieba.posseg as pseg
import jieba.analyse
import os

def test():
    # print(os.getcwd())
    path = '/home/lumir/git/playForFun/test81/nltkTest/高危职业_DangerousJob.txt'
    openFile = open(path, 'r+', encoding='gbk')
    content = openFile.read()
    try:
        jieba.analyse.set_stop_words('/home/lumir/git/playForFun/test81/nltkTest/discontinuation_words_list.txt')
        tags = jieba.analyse.extract_tags(content, topK=50, withWeight=True)
        for v,n in tags:
            print(v + '\t' + str(int(n*10000)))
    finally:
        openFile.close()
    '''
    example 1:
    words = pseg.cut('我来自湖南大学，我不是湖南人。')
    for w in words:
        print(w.word, w.flag)
        
    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    print('Full mode: ', '/'.join(seg_list))
    seg_list2 = jieba.cut("我来到北京清华大学", cut_all=False)
    print('Default mode: ', '/'.join(seg_list2))
    seg_list3 = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模
    print(','.join(seg_list3))
    '''

if __name__ == '__main__':
    test()
