import re
import pandas as pd

def ads_transaction_preprocessing(df_ads_transaction):
    # Rename the id for more clarity
    df_ads_transaction.index.rename('id_transaction',inplace=True)
    
    print('ads_transaction preprocessing done')
    
    return df_ads_transaction

def referrals_preprocessing(df_referrals):
    # Rename the id for more clarity
    df_referrals.index.rename('id_referrals',inplace=True)
    
    print('referrals preprocessing done')
    
    return df_referrals

def users_preprocessing(df_users):
    # Split the 'misc' column into two columns: phone_number and connections
    df_users['misc'] = df_users['misc'].map(eval)
    df_users = pd.concat([df_users.drop(['misc'], axis=1), df_users['misc'].apply(pd.Series)], axis=1)
    df_users['connections']= df_users['connections'].astype('str')
    
    print('users preprocessing done')
    
    return df_users

    

def ads_preprocessing(df_ads):

    # Set index and rename it
    df_ads.set_index('id',inplace=True)
    df_ads.index.rename('id_ads',inplace=True)
    
    # Lowercase the 'category' column
    df_ads['category'] = df_ads['category'].apply(lambda x: x.lower())
    
    # Clean category names (spelling typos...)
    def is_realestate(x):
        if 'estate' in x:
            return 'real_estate'
        else:
            return x

    df_ads['category'] = df_ads['category'].apply(is_realestate)

    # Create subcategory based on title
    def offer_type(x):
        if 'Loue' in x:
            return 'location'
        elif 'Vends' in x:
            return 'vente'
        elif 'Recherche' in x:
            return 'recherche'
        else:
            return x

    df_ads['offer_type'] = df_ads['title'].apply(offer_type)

    df_ads['property_size'] =  df_ads['title'].str.extract(r'([TF][1-9])')
    df_ads['property_size'].fillna(value='Unspecified', inplace=True)

    print('ads preprocessing done')
    
    return df_ads