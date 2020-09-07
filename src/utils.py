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
    popular = data.groupby('item_id')['user_id'].nunique().reset_index() / data['user_id'].nunique()
    popular.rename(columns={'user_id': 'share_unique_users'}, inplace=True)

    top_popular = popular[popular['share_unique_users'] > 0.75].item_id.tolist()
    data = data[~data['item_id'].isin(top_popular)]
    
    # 4. Выбор топ-N самых популярных товаров (N = take_n_popular)
    # your_code
    popularity = data.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)

    top_n = popularity.sort_values('n_sold', ascending=False).head(take_n_popular).item_id.tolist()
    data = data[data.item_id.isin(top_n)]
    
    return data