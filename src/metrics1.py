#import pandas as pd
#import numpy as np
def recall_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    
    flags = np.isin(bought_list, recommended_list)
    
    recall = flags.sum() / len(bought_list)
  
    return recall
	
def precision_at_k(recommended_list, bought_list, k=5):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = recommended_list[:k]
    
    flags = np.isin(bought_list, recommended_list)
    
    precision = flags.sum() / len(recommended_list)
    
    
    return precision
	
#был ли хотя бы 1 релевантный товар среди топ-k рекомендованных
def hit_rate_at_k(recommended_list, bought_list, k):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    
    flags = np.isin(bought_list, recommended_list)
    
    hit_rate = (flags.sum() > 0) * 1
    
    return hit_rate
	
#(revenue of recommended items @k that are relevant) / (revenue of recommended items @k)
def money_precision_at_k(recommended_list, bought_list, prices_recommended, k):
        
    # your_code
    # Лучше считать через скалярное произведение, а не цикл
    
    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    
    flags = np.isin(recommended_list, bought_list) #вернет размерность recommended_list, т.е. k
    
    precision = np.dot(flags, prices_recommended) / prices_recommended.sum()
    
    
    return precision

#Money Recall@k = (revenue of recommended items @k that are relevant) / (revenue of relevant items) 
def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k):
    bought_list = np.array(bought_list)
    prices_bought = np.array(prices_bought)
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    
    flags = np.isin(recommended_list, bought_list)
    
    r1 = np.dot(flags,prices_recommended)
    r2 = prices_bought.sum()
    recall = r1 / r2
  
    return recall
	
def reciprocal_rank(recommended_list, bought_list):
    
    flags = np.isin(recommended_list, bought_list)
    
    if sum(flags) == 0:
        return 0
    
    sum_ = 0
    count = 0
    for i in range(1, len(flags)+1):
        if flags[i-1]:
            sum_ += 1/i
            print(f'iteration:{i}',f'rank (1/i):{1/i}')
            count += 1
    result = sum_ / count
    
    return result