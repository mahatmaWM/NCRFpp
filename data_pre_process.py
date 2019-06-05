# -*- coding: utf-8 -*-
"""
把我们的序列标注格式转化为项目支持的格式
"""

import codecs
import random
seed_num = 42
random.seed(seed_num)

if __name__ == '__main__':
    with codecs.open('./slot.music/origin-data/features', "r", "utf-8") as f1, \
            codecs.open('train-simple.txt', "w", "utf-8") as f_train, \
            codecs.open('dev-simple.txt', "w", "utf-8") as f_dev, \
            codecs.open('test-simple.txt', "w", "utf-8") as f_test:

        sentence = list([])

        for line in f1.readlines():
            if line.startswith('B') or line.startswith('E'):
                continue

            line = line.strip('\n')
            splits = line.split('\t')

            if len(splits) > 1:
                # splits[1] + ' [POS]' + splits[2] + ' [DICT]' + splits[3] + ' ' + splits[4]
                sentence.append(splits[1] + ' ' + splits[4])
            else:
                res = '\n'.join(sentence)
                sentence.clear()
                sample = random.random()
                if 0 < sample < 0.8:
                    f_train.write(res + '\n\n')
                elif 0.8 <= sample < 0.9:
                    f_dev.write(res + '\n\n')
                else:
                    f_test.write(res + '\n\n')