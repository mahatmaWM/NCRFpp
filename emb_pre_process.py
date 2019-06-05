# -*- coding: utf-8 -*-
"""
把我们的序列标注格式转化为项目支持的格式
"""

import codecs
import random

if __name__ == '__main__':
    with codecs.open('./emb/res.emb.txt', "r", "utf-8") as f1, \
            codecs.open('./emb/res.emb.new.txt', "w", "utf-8") as f_train:

        sentence = list([])

        for line in f1.readlines():
            line = line.strip('\n')
            splits = line.split()
            if len(splits) != 301:
                continue
            f_train.write(line + '\n')