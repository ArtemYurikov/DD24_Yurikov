# TODO Напишите функцию для поиска индекса товара


def search(llist, find_item):
    if find_item in llist:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {llist.index(find_item)}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

search(items_list, "банан")
search(items_list, "груша")
search(items_list, "персик")