# https://programmers.co.kr/learn/courses/30/lessons/60059

import numpy as np
import pandas as pd


def solution(key, lock):
    key = pd.DataFrame(key)
    for four in range(4):
        df = pd.DataFrame(lock)
        for rot in range(four):
            df = df.transpose()[::-1]
        df.index = range(len(lock))
        df.columns = range(len(lock))

        for step in range(len(key)-1):
            df = pd.DataFrame([[0]*len(lock)]).append(df)
            df = df.append([[0]*len(lock)])
        for step in range(len(key)-1):
            df[len(lock)+step] = 0
            df.insert(0,50+step,0)

        for r_dir in range(len(key) + len(lock) - 1):
            for c_dir in range(len(key) + len(lock) - 1):
                df.iloc[c_dir:c_dir+len(key),r_dir:r_dir+len(key)] = df.iloc[c_dir:c_dir+len(key),r_dir:r_dir+len(key)].values + key.values

                center = df.iloc[len(key)-1:len(lock) + len(key) -1,len(key)-1:len(lock) + len(key) -1]

                if center.sum().sum() == len(lock)*len(lock):
                    if center.std().std() == 0:
                        return True

                df.iloc[c_dir:c_dir+len(key),r_dir:r_dir+len(key)] = df.iloc[c_dir:c_dir+len(key),r_dir:r_dir+len(key)].values - key.values

    
    return False