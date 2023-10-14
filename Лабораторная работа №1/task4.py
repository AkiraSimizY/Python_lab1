users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dec = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
lei = len(users)
umi = len(set(users))
dec["Общее количество"] = lei
dec["Уникальные посещения"] = umi
print(dec)
