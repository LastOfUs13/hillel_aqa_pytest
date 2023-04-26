from collection_from_db import PsGamesCollection

ps_games_collection = PsGamesCollection()
new_item_in_collection = ({"genre": "sport", "title": "Fifa2023"})
res = ps_games_collection.my_insert_one(new_item_in_collection)

new_items_in_collection = [{"genre": "shooter", "title": "call of duty"}, {"genre": "rpg", "title": "God of War"}]
ps_games_collection.my_insert_many(new_items_in_collection)

show_one_item = ps_games_collection.my_find_one({"genre": "rpg"})
print(show_one_item)

show_all_items = ps_games_collection.my_find()
for items in show_all_items:
    print(items)
