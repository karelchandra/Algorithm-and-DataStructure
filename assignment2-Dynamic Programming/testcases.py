'''            
target_difficulty = 15
monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]

monster_list = [("Raiden Shogun", 666), ("Ganyu", 66), ("Bennett", 1), ("Hu Tao", 10), ("Venti", 6),
                    ("Morax", 9), ("Kokomi", 13)]
target_difficulty = 9999
monster_list = []
target_difficulty = 0
monster_list = [("Naruto", 2), ("Naruto", 2), ("Naruto", 2), ("Sasuke", 1)]
target_difficulty = 15
monster_list = [("PAIN", 9), ("Joker", 7), ("Darth Vader", 6), ("Thanos", 8), ("Voldemort", 5)]
target_difficulty = 0
print(count_encounters(target_difficulty, monster_list))
monster_list1 = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
print(count_encounters(15,monster_list1))
print(count_encounters(73,monster_list1))
monster_list2 = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10),("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
print(count_encounters(15,monster_list2))
monster_list3 = [("a", 5), ("imp", 7), ("b", 7), ("c", 10),("d", 5), ("e", 10), ("f", 3), ("g", 10)]
print(count_encounters(43,monster_list3))
print(count_encounters(0,monster_list3))
monster_list4 = [("monster",7)]
print(count_encounters(100,monster_list4))
print(count_encounters(5,monster_list4))
print(count_encounters(49,monster_list4))

target_difficulty = 100
monster_list = [("0", 12)]
for i in range(24):
    random.seed(i)
    monster_list.append((str(i), random.randint(1, 100)))
print(count_encounters(target_difficulty, monster_list))

target_difficulty = 1000
monster_list = [("0", 9)]
for i in range(499):
    random.seed(i - 10000)
    monster_list.append((str(i), random.randint(1, 1000)))
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 10000
monster_list = [("0", 345)]
for i in range(4999):
    random.seed(i * 47)
    monster_list.append((str(i), random.randint(1, 10000)))
print(count_encounters(target_difficulty, monster_list))

target_difficulty = 15
monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 0
monster_list = []
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 2343252
monster_list = []
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 18
monster_list = [("Zhongli", 6), ("Morax", 6), ("Rex Lapis", 6), ("Diluc", 5)]
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 16
monster_list = [("Genshin", 4), ("Genshin", 4), ("Genshin", 4), ("Mihoyo", 11), ("Genshin", 4)]
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 6
monster_list = [("Monke", 5), ("Thanos", 2), ("Thanos", 3)]
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 12
monster_list = [("FIT2014", 9), ("FIT1008", 5), ("FIT2004", 8), ("FIT3155", 15)]
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 0
monster_list = [("Iron Man", 324), ("Thor", 1432), ("Captain America", 23), ("Hulk", 2354)]
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 100
monster_list = [("0", 12)]
for i in range(24):
    random.seed(i)
    monster_list.append((str(i), random.randint(1, 100)))
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 1000
monster_list = [("0", 9)]
for i in range(499):
    random.seed(i - 10000)
    monster_list.append((str(i), random.randint(1, 1000)))
print(count_encounters(target_difficulty, monster_list))
target_difficulty = 10000
monster_list = [("0", 345)]
for i in range(4999):
    random.seed(i * 47)
    monster_list.append((str(i), random.randint(1, 10000)))
print(count_encounters(target_difficulty, monster_list))
'''