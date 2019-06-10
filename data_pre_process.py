# -*- coding: utf-8 -*-
"""
把我们的序列标注格式转化为项目支持的格式
"""

import codecs

if __name__ == '__main__':
    with codecs.open('./ner.tvseries/test_crfpp_char.txt', "r", "utf-8") as f1, \
            codecs.open('./ner.tvseries/test.txt', "w", "utf-8") as f_train:

        sentence = list([])
        chars = list([])
        pos = list([])

        for line in f1.readlines():
            if line.startswith('B') or line.startswith('E'):
                continue

            line = line.strip('\n')
            splits = line.split('\t')

            if len(splits) > 1:
                sentence.append([splits[1], '[POS]' + splits[2], '[DICT]' + splits[3], splits[4]])
                chars.append(splits[1])
                pos.append(splits[2])
            elif len(sentence) > 1:
                for i in range(len(chars)-1):
                    sentence[i].append('[BI]'+chars[i]+chars[i+1])
                    sentence[i].append('[BI_POS]'+pos[i]+pos[i+1])

                # logging.info(sentence)
                sentence[-1].append('[BI]'+chars[-1]+'#')
                sentence[-1].append('[BI_POS]'+pos[-1] + '#')

                res = list([])
                for item in sentence:
                    res.append(item[0] + ' ' + item[-1] + ' ' + item[-2] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3])
                res_str = '\n'.join(res)
                sentence.clear()
                chars.clear()
                pos.clear()
                f_train.write(res_str + '\n\n')