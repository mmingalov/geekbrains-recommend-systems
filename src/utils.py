def prefilter_items(data, take_n_popular=5000):
    """Предфильтрация товаров"""
    
   # 1. Удаление товаров, со средней ценой < 1$
    # your_code
    data = data[data.sales_value / data.quantity < 1]
    
    # 2. Удаление товаров со соедней ценой > 30$
    # your_code
    data = data[data.sales_value / data.quantity > 30]

    # 3. Придумайте свой фильтр
    # your_code
    # Ещё один фильтр по популярности. 
    # Если товар покупает более 3/4 пользователей, то его рекомендовать не стоит, так как его и так купят.
    popular = data.groupby('item_id')['user_id'].nunique().reset_index()
    users_count = data['user_id'].nunique()
    popular['user_id'] = popular['user_id'].apply(lambda x: x / users_count)
    popular.rename(columns={'user_id': 'share_unique_users'}, inplace=True)
    popular.sort_values(by='share_unique_users', ascending=False, inplace=True)

    top_popular = popular[popular['share_unique_users'] > 0.75].item_id.tolist()
    data = data[~data['item_id'].isin(top_popular)]
    
    # 4. Выбор топ-N самых популярных товаров (N = take_n_popular)
    # your_code
    popularity_sales = data.groupby('item_id')['sales_value'].sum().reset_index()
    popularity_sales.sort_values('sales_value', ascending=False, inplace=True)
    n_popular = popularity_sales['item_id'][:take_n_popular].tolist()
    
    # Заведем фиктивный item_id (если юзер не покупал товары из топ-5000, то он "купил" такой товар)
    data.loc[~data['item_id'].isin(n_popular), 'item_id'] = 9999999
    n_popular.append(9999999)
    
    data = data[data['item_id'].isin(n_popular)]
    
    return data