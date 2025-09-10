## Write a Python program to add key to a dictionary.
ind_crick_play_rank_dict = {
    'Shubman Gill' : 'Rank-1',
    'Virat Kohli' : 'Rank-4'
}

print("Some Indian Cricket Player Names With There ODI Ranking:\n",ind_crick_play_rank_dict)
#Adding Key And Value In Dictionary
new_key1 = 'Rohit Sharma'
new_value1 = 'Rank-1'

new_key2 = 'Jasprit Bhumrah'
new_value2 = 'Rank-5'

ind_crick_play_rank_dict[new_key1] = new_value1
ind_crick_play_rank_dict[new_key2] = new_value2

print("After Adding More Player Names With There Ranking:\n",ind_crick_play_rank_dict)