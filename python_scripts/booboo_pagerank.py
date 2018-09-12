# -*- coding:utf8 -*-
"""
Created on:
@author: BoobooWei
Email: rgweiyaping@hotmail.com
Version: V.18.09.12.0
Description: 学习pagerank时的计算辅助
Help:
"""

import math


class PageRank():
    def __init__(self, S_dict):
        self.N = len(S_dict)
        self.page = S_dict.values()
        self.S_dict = S_dict
        self.Q_next_dict = []
        for i in range(self.N):
            self.Q_next_dict.append(1)


    def get_G(self):
        """
		根据 G = \alpha S + ( 1 - \alpha ) \frac{1}{N} U 计算 G_a G_b G_c G_d
        :return:
        """
        G_dict = {}
        for k, v in self.S_dict.items():
            G = []
            for s in v:
                G.append(0.85 * s + 0.15 / self.N)
            G_dict[k] = G
        return G_dict

    def convert_G(self, G_dict):
        """
        行列转换
        :param G_dict:
        :return:
        """
        G_dict_convert = {}
        y_dict = dict(zip(range(len(G_dict)), G_dict.keys()))
        for j in range(len(G_dict)):
            G_dict_convert[y_dict[j]] = []
            for k,v in G_dict.items():
                #print('出链网页{0} 入链网页{1} 状态转移概率值{2}'.format(k,y_dict[j],v[j]))
                G_dict_convert[y_dict[j]].append(v[j])
        return G_dict_convert


    def test_Q(self, G_dict_convert, Q_cur_list):
        Q_next_list = []
        for v in G_dict_convert.values():
            q = 0
            for i in range(self.N):
                q = q + v[i] * Q_cur_list[i]
            Q_next_list.append(q)
        return Q_next_list


    def get_pagerank(self, G_dict):
        Q_next_list = self.Q_next_dict
        num = 1
        while True:
            num = num + 1
            Q_cur_list = Q_next_list
            Q_next_list = self.test_Q(G_dict, Q_cur_list)
            #Q_next_list = self.get_Q(G_dict, Q_cur_list)
            if Q_next_list == Q_cur_list:
                Q_page_list = G_dict.keys()
                Q_page_dict = dict(zip(Q_page_list, Q_next_list))
                return (num, Q_page_dict)
                break


def app(S_dict):
    api = PageRank(S_dict)
    G_dict = api.get_G()
    G_dict_convert = api.convert_G(G_dict)
    return api.get_pagerank(G_dict_convert)


if __name__ == '__main__':
    """
    S_dict 为 已经计算好的概率转移矩阵
    """
    S_dict = {'A': [0, 1 / 3, 1 / 3, 1 / 3], 'B': [0, 0, 1 / 2, 1 / 2], 'C': [0, 0, 0, 1], 'D': [0, 1, 0, 0]}
    #S_dict = {
    #    'A':[0, 1/5, 1/5, 1/5, 1/5, 0, 1/5],
    #    'B':[1, 0, 0, 0, 0, 0, 0],
    #    'C':[1/2, 1/2, 0, 0, 0, 0, 0],
    #    'D':[0, 1/3, 1/3, 0, 1/3, 0, 0],
    #    'E':[1/4, 0, 1/4, 1/4, 0, 1/4, 0],
    #    'F':[1/2, 0, 0, 0, 1/2, 0, 0],
    #    'G':[0, 0, 0, 0, 1, 0, 0]
    #}
    num,result = app(S_dict)
    print('迭代次数{}'.format(num))
    for i in sorted(result.items(), key=lambda x: x[1], reverse=True):
        print(i)






