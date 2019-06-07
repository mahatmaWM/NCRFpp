# -*- coding: utf-8 -*-
"""
把我们的序列标注格式转化为项目支持的格式
"""

import codecs
import random

if __name__ == '__main__':
    with codecs.open('./temp/sys.video.film/test_crfpp_char.txt', "r", "utf-8") as f1, \
            codecs.open('./temp/sys.video.film/test-bi-simple.txt', "w", "utf-8") as f_train:

        sentence = list([])
        chars = list([])

        for line in f1.readlines():
            if line.startswith('B') or line.startswith('E'):
                continue

            line = line.strip('\n')
            splits = line.split('\t')


            if len(splits) > 1:
                # sentence.append(splits[1] + ' [DICT]' + splits[3] + ' ' + splits[4])
                sentence.append([splits[1], '[POS]' + splits[2], '[DICT]' + splits[3], splits[4]])
                chars.append(splits[1])
            elif len(sentence) > 1:
                for i in range(len(chars)-1):
                    sentence[i].append('[BI]'+chars[i]+chars[i+1])

                # logging.info(sentence)
                sentence[-1].append('[BI]'+chars[-1]+'#')


                res = list([])
                for item in sentence:
                    res.append(item[0] + ' ' + item[-1] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3])
                res_str = '\n'.join(res)
                sentence.clear()
                chars.clear()
                f_train.write(res_str + '\n\n')