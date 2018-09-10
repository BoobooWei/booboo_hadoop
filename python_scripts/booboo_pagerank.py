# -*- coding:utf8 -*-
"""
Created on:
@author: BoobooWei
Email: rgweiyaping@hotmail.com
Version: V.18.09.10.0
Description: 学习pagerank时的计算辅助
Help:
"""

import math


class PageRank():
    def __init__(self):
        pass

    def get_G(self, S_dict):
        G_dict = {}
        for k, v in S_dict.items():
            G = []
            for s in v:
                G.append(0.85 * s + 0.15 / 4)
            G_dict[k] = G
        return G_dict

    def get_Q(self, G_dict, Q_cur_list):
        Q_next_list = []
        for i in range(4):
            Q_next_list.append(
                G_dict['A'][i] * Q_cur_list[0] + G_dict['B'][i] * Q_cur_list[1] + G_dict['C'][i] * Q_cur_list[2] +
                G_dict['D'][i] * Q_cur_list[3])
        return Q_next_list

    def get_pagerank(self, G_dict):
        Q_next_list = [1, 1, 1, 1]
        num = 1
        while True:
            num = num + 1
            Q_cur_list = Q_next_list
            Q_next_list = self.get_Q(G_dict, Q_cur_list)
            if Q_next_list == Q_cur_list:
                Q_page_list = ['A', 'B', 'c', 'D']
                Q_page_dict = dict(zip(Q_page_list, Q_next_list))
                return (num, Q_page_dict)
                break



def app():
    api = PageRank()
    #S_dict = {'A': [0, 1 / 3, 1 / 3, 1 / 3], 'B': [0, 0, 1 / 2, 1 / 2], 'C': [0, 0, 0, 1], 'D': [0, 1, 0, 0]}
    S_dict = {'A': [0, 1 / 3, 1 / 3, 1 / 3], 'B': [0, 0, 1 / 2, 1 / 2], 'C': [1, 0, 0, 0], 'D': [0, 0, 1, 0]}
    G_dict = api.get_G(S_dict)
    print(api.get_pagerank(G_dict))

if __name__ == '__main__':
    """
    计算结果为：
    (74, {'A': 0.14999999999999947, 'B': 1.492990390050871, 'c': 0.8270209157716194, 'D': 1.529988694177496})
    说明循环74次后，每个网页pagerank值不再改变
    待改进：
    1. 根据网页入链和出链情况计算概率转移矩阵
    2. 将所有方法的网页数由固定的4改为任意n
    """
    app()





