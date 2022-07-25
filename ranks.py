ranks = ('common', 'uncommon', 'rare', 'epic', 'legendary')


def get_rank_name_by_num(num):
    return ranks[num - 1]
