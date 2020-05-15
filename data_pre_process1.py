# -*- coding: utf-8 -*-
"""
把我们的序列标注格式转化为项目支持的格式
"""

import codecs
import random

random.seed(2019)
res = set([])
with codecs.open('./datagrand/corpus.txt', "r", "utf-8") as fr, \
        codecs.open('./datagrand/corpus_new.txt', "w", "utf-8") as fw, \
        codecs.open('./datagrand/vocab.txt', "w", "utf-8") as fw1:
    for line in fr.readlines():
        for item in line.strip('\n').split('_'):
            res.add(item)
        fw.write('%s' % ' '.join(line.split('_')))

    for item in res:
        fw1.write('%s\n' % item)

# if __name__ == '__main__':
#     with codecs.open('./datagrand/train_train.txt', "r", "utf-8") as fr, \
#             codecs.open('./datagrand/train_train_crf.txt', "w", "utf-8") as fw:
#         for line in fr.readlines():
#             new_line = list([])
#             line = line.strip('\n')
#             splits = line.split(' ')
#             for item in splits:
#                 if len(item) == 0:
#                     continue
#                 sp = item.split('_')
#                 for it in sp:
#                     temp_sp = it.split('/')
#
#                     if len(temp_sp) == 1:
#                         new_line.append((temp_sp[0], None))
#                     else:
#                         # print(temp_sp)
#                         new_line.append((temp_sp[0], temp_sp[1]))
#             for item in new_line:
#                 fw.write('%s %s\n' % (item[0], 'O' if item[1] is None else item[1]))
#             fw.write('\n')
