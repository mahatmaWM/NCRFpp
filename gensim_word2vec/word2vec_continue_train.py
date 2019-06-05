from gensim.models import KeyedVectors
from gensim.models import Word2Vec
from gensim.models import word2vec

import re, codecs, sys, os

def seg_char(sent):
    """
    把句子按字分开，不破坏英文结构
    """
    pattern = re.compile(r'([\u4e00-\u9fa5])')
    chars = pattern.split(sent)
    chars = [w for w in chars if len(w.strip()) > 0]
    return chars


# with codecs.open('all_corpus.txt', 'r', 'utf-8') as fr, codecs.open('all_corpus_segment.txt', 'w', 'utf-8') as fw:
#     for line in fr.readlines():
#         line = line.strip()
#         fw.write(' '.join(seg_char(line)) + '\n')

# with codecs.open('all_corpus.txt', 'r', 'utf-8') as fr, codecs.open('all_corpus_bi_segment.txt', 'w', 'utf-8') as fw:
#     for line in fr.readlines():
#         line = line.strip()
#         seg = seg_char(line)
#         res = list([])
#         for i in range(len(seg) - 1):
#             res.append(seg[i]+seg[i+1])
#         res.append(seg[-1]+'#')
#         fw.write(' '.join(res) + '\n')

sentences = word2vec.LineSentence('./all_corpus_bi_segment.txt')
model_new = Word2Vec(size=300, min_count=3, iter=5)
model_new.build_vocab(sentences)
print('before new model vocab size ', len(model_new.wv.vocab.keys()))
total_examples = model_new.corpus_count
print('total corpus size ', total_examples)
model_new.train(sentences, total_examples=total_examples, epochs=model_new.iter)
temp_emb = 'bi.word.emb.txt'
model_new.wv.save_word2vec_format(temp_emb)




# sentences = word2vec.LineSentence('./all_corpus_segment.txt')
#
# # 定义一个新的模型
# model_new = Word2Vec(size=300, min_count=3, iter=5)
# model_new.build_vocab(sentences)
# print('before new model vocab size ', len(model_new.wv.vocab.keys()))
# total_examples = model_new.corpus_count
# print('total corpus size ', total_examples)
#
# # 加载已有的模型，like-word2vec.txt=====word.emb
# pre_train_emb = 'like-word2vec.txt'
# model_pre = KeyedVectors.load_word2vec_format(pre_train_emb, binary=False)
# print('before pre model vocab size ', len(list(model_pre.vocab.keys())))
#
# # 重新训练
# model_new.build_vocab([list(model_pre.vocab.keys())], update=True)
# print('after new model vocab size ', len(model_new.wv.vocab.keys()))
#
# model_new.intersect_word2vec_format("like-word2vec.txt", binary=False, lockf=1.0)
# model_new.train(sentences, total_examples=total_examples, epochs=model_new.iter)
#
# print('train over')
# # model_new.save("res.emb.all")
#
# temp_emb = 'res.emb.temp.txt'
# model_new.wv.save_word2vec_format(temp_emb)
# emb = 'res.emb.txt'
#
# with codecs.open(temp_emb, 'r', 'utf-8') as fr1, \
#         codecs.open(pre_train_emb, 'r', 'utf-8') as fr2, \
#         codecs.open(emb, 'w', 'utf-8') as fw:
#     temp_res = set([])
#     for line in fr1.readlines():
#         line = line.strip()
#         splits = line.split()
#         if len(splits) != 301:
#             continue
#         else:
#             temp_res.add(splits[0])
#             fw.write(line + '\n')
#     for line in fr2.readlines():
#         line = line.strip()
#         splits = line.split()
#         if len(splits) != 301:
#             continue
#         else:
#             if splits[0] not in temp_res:
#                 temp_res.add(splits[0])
#                 fw.write(line + '\n')
#
# os.system('rm %s' % temp_emb)
