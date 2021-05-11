# Srijana Shrestha
# 1918305

# Srijana Shrestha
# 1918305
import csv
import datetime

'''Create a new empty 'items' dictionary, read 'ManufactureList.csv' file and place the items_id as
KEY and another dictionary as VALUE which includes manufacturer, item_type and damaged value from the csv file.
'''
items = {}
with open('ManufacturerList.csv', 'r') as csv_file:
    mfList_reader = csv.reader(csv_file, delimiter=',')
    for line in mfList_reader:
        item_id = line[0]
        items[item_id] = {}
        mf_name = line[1]
        item_type = line[2]
        damaged = line[3]
        items[item_id]['manufacturer'] = mf_name.strip()
        items[item_id]['item_type'] = item_type.strip()
        items[item_id]['damaged'] = damaged

'''Read 'PriceList.csv' file and add data such as the price of the product from the csv file to the 'items'
dictionary in their respective item_id.
'''
with open('PriceList.csv', 'r') as csv_file:
    item_reader = csv.reader(csv_file, delimiter=',')
    plist = []
    for line1 in item_reader:
        plist.append(line1)
    for line2 in plist:
        p_item_id = line2[0]
        p_price = line2[1]
        items[p_item_id]['price'] = p_price

'''Read 'ServiceDatesList.csv' file and add data such as the service date of the product from the csv file to
the 'items' dictionary in their respective item_id
'''
with open('ServiceDatesList.csv', 'r') as csv_file:
    service_reader = csv.reader(csv_file, delimiter=',')
    for line in service_reader:
        s_item_id = line[0]
        s_service = line[1]
        items[s_item_id]['service_date'] = s_service

'''Create an empty 'full_il' and 'half_il' lists and add all data into full_il list such as item_id, manufacturer, 
item_type, price, service_date and damaged from 'items' dictionary using those lists. Then use bubble sort to sort 
the data based on 'manufacturer' and finally write the sorted data in 'full_inventory.csv' file.
 '''
full_il = []
with open('full_inventory.csv', 'w') as new_file:
    full_inventory_write = csv.writer(new_file)
    half_il = []
    for k, v in items.items():
        a = k
        b = (items[k]['manufacturer'])
        c = (items[k]['item_type'])
        d = (items[k]['price'])
        e = (items[k]['service_date'])
        f = (items[k]['damaged'])
        half_il = [a, b, c, d, e, f]
        full_il.append(half_il)

    for i in range(0, len(full_il)):
        for j in range(0, len(full_il) - i - 1):
            if full_il[j][1] > full_il[j + 1][1]:
                t = full_il[j]
                full_il[j] = full_il[j + 1]
                full_il[j + 1] = t
    for i in range(0, len(full_il)):
        full_inventory_write.writerow(full_il[i])

'''Create an empty 'item_type_list' and 'single_item_type' to save the all the unique item_type from 'items'
dictionary into single_item_type list'''
item_type_list = []
for k, v in items.items():
    item_type = (items[k]['item_type'])
    item_type_list.append(item_type)
single_item_type = []
for single in item_type_list:
    if single not in single_item_type:
        single_item_type.append(single)

'''Create an empty 'each_il' list and 'Big_list' and make use of them to add all the data such as item_id, manufacturer,
price, service_date, damaged and item_type to the 'Big_list' '''
each_il = []
Big_list = []
for k, v in items.items():
    a = k
    b = (items[k]['manufacturer'])
    c = (items[k]['price'])
    d = (items[k]['service_date'])
    e = (items[k]['damaged'])
    f = (items[k]['item_type'])
    each_il = [a, b, c, d, e, f]
    Big_list.append(each_il)

'''Use Bubble sort to sort the list based on item_id'''
for i in range(0, len(Big_list)):
    for j in range(0, len(Big_list) - i - 1):
        if int(Big_list[j][0]) > int(Big_list[j + 1][0]):
            t = Big_list[j]
            Big_list[j] = Big_list[j + 1]
            Big_list[j + 1] = t

'''Write the data from 'Big_list' into different 'Inventory.csv' files based on the unique 'item_type' present in the 
single_item_type. Respective item_id, manufacturer_name, price, service data and damaged would be written in the output
csv file based on each item_type.
 '''
for each in single_item_type:
    each_il = []
    with open(str(each) + '_Inventory.csv', 'w') as new_file:
        write = csv.writer(new_file)
        Main_list = []
        for each_item_type in Big_list:
            if each_item_type[5] == each:
                a = each_item_type[0]
                b = each_item_type[1]
                c = each_item_type[2]
                d = each_item_type[3]
                e = each_item_type[4]
                each_il = [a, b, c, d, e]
                Main_list.append(each_il)
                write.writerow(each_il)

'''Create an empty past_s_l list and fill the list with item_id, manufacturer, item_type, price, service_date,
damaged if the service_date is in the past. Use the bubble sort to sort the data inside the list based on service_date
from old to new and finally write the data into a CSV file
'''
with open('pastServiceDateInventory.csv', 'w') as new_file:
    pastServiceDateInventory_write = csv.writer(new_file)

    past_s_l = []
    for k, v in items.items():
        e = (items[k]['service_date'])
        first_slash = e.find("/", 0, 3)
        second_slash = e.find("/", 3, 6)

        month = e[0:first_slash]
        day = e[first_slash + 1: second_slash]
        year = e[second_slash + 1:]
        ans_date = datetime.date(int(year), int(month), int(day))
        current_date = datetime.date.today()
        if ans_date < current_date:
            a = k
            b = (items[k]['manufacturer'])
            c = (items[k]['item_type'])
            d = (items[k]['price'])
            f = (items[k]['damaged'])
            past_service_date_il = [a, b, c, d, ans_date, f]
            past_s_l.append(past_service_date_il)

    for i in range(0, len(past_s_l)):
        for j in range(0, len(past_s_l) - i - 1):
            if (past_s_l[j][4]) > (past_s_l[j + 1][4]):
                t = past_s_l[j]
                past_s_l[j] = past_s_l[j + 1]
                past_s_l[j + 1] = t

    for i in range(0, len(past_s_l)):
        pastServiceDateInventory_write.writerow(past_s_l[i])

'''Create an empty damaged_item list and fill the list with item_id, manufacturer, item_type, price, service_date from
items dictionary if the item is damaged. Use the bubble sort to sort the data based on price from higher to lower.
Finally, write the data into CSV file.
'''
with open('damageInventory.csv', 'w') as new_file:
    damageInventory_write = csv.writer(new_file)
    damaged_item = []
    for k, v in items.items():
        if items[k]['damaged'] == 'damaged':
            a = k
            b = (items[k]['manufacturer'])
            c = (items[k]['item_type'])
            d = (items[k]['price'])
            e = (items[k]['service_date'])
            damaged_i = [a, b, c, d, e]
            damaged_item.append(damaged_i)

    for i in range(0, len(damaged_item)):
        for j in range(0, len(damaged_item) - i - 1):
            if int(damaged_item[j][3]) < int(damaged_item[j + 1][3]):
                t = damaged_item[j]
                damaged_item[j] = damaged_item[j + 1]
                damaged_item[j + 1] = t

    for i in range(0, len(damaged_item)):
        damageInventory_write.writerow(damaged_item[i])

###################################################################################
final_types = []
final_manufacturers = []
for item in items:
    listed_manufacturer = items[item]['manufacturer']
    listed_type = items[item]['item_type']

    if listed_type not in final_types:
        final_types.append(listed_type)
    if listed_manufacturer not in final_manufacturers:
        final_manufacturers.append(listed_manufacturer)


print(final_types)
print(final_manufacturers)
print(items)

user_input = None
while user_input != 'q':
    user_input = input("\nPlease enter a manufacturer name and item type or type 'q' to quit:\n")

    if user_input == 'q':
        break
    else:
        input_manufacturer = None
        input_types = None
        user_input = user_input.split()

        false_input = False
        for word in user_input:
            if word in final_manufacturers:
                if input_manufacturer:
                    false_input = True
                else:
                    input_manufacturer = word
                    print(input_manufacturer)
            elif word in final_types:
                if input_types:
                    false_input = True
                else:
                    input_types = word
                    print(input_types)
        if not input_manufacturer or not input_types or false_input:
            print("No such item in inventory")

        else:
            values = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

            matched_items = []
            similar_items = {}

            for item in values:
                if items[item]['item_type'] == input_types:
                    current_day = datetime.date.today()
                    service_date = items[item]['service_date']
                    service_expiration = datetime.datetime.strptime(service_date, "%m/%d/%Y").date()
                    expired = service_expiration < current_date
                    if items[item]['manufacturer'] == input_manufacturer:
                        if not expired and not items[item]['damaged']:
                            matched_items.append((item, items[item]))
                    else:
                        if not expired and not items[item]['damaged']:
                            similar_items[item] = items[item]

            if matched_items:
                item = matched_items[0]
                item_id = item[0]
                manufacturer_name = item[1]['manufacturer']
                item_type = item[1]['item_type']
                price = item[1]['price']

                print('Your item is:', item_id, ',', manufacturer_name, ',', item_type, ',', '$' + price)

                if similar_items:

                    closest_item = None
                    nearest_price_dif = None
                    matched_price = price

                    for item in similar_items:
                        if nearest_price_dif is None:
                            closest_item = similar_items[item]
                            nearest_price_dif = abs(int(matched_price) - int(similar_items[item]['price']))
                            item_id = item
                            manufacturer_name = similar_items[item]['manufacturer']
                            item_type = similar_items[item]['item_type']
                            price = similar_items[item]['price']

                        price_difference = abs(int(matched_price) - int(price))
                        if nearest_price_dif > price_difference :
                            closest_item = item
                            nearest_price_dif = price_difference
                            item_id = item
                            manufacturer_name = similar_items[item]['manufacturer']
                            item_type = similar_items[item]['item_type']
                            price = similar_items[item]['price']

                    print("You may, also, consider:", item_id, ",", manufacturer_name, ",", item_type, ",", "$"+price)
            else:
                print("No such item in inventory")
csv_file.close()
new_file.close()
