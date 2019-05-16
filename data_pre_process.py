# -*- coding: utf-8 -*-
"""
把我们的序列标注格式转化为项目支持的格式
"""
if __name__ == '__main__':

    import codecs

    with codecs.open('./sample_data/dev.bmes', "r", "utf-8") as f1, codecs.open('temp_res.txt', "w", "utf-8") as f2:
        for line in f1.readlines():
            if line.startswith('B') or line.startswith('E'):
                continue

            line = line.strip('\n')
            splits = line.split('\t')
            # print(splits)

            if len(splits) > 1:
                f2.write(splits[1]+' [POS]' + splits[2] + ' [DICT]' + splits[3] + ' ' + splits[4] + '\n')
            else:
                f2.write('\n')




