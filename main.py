from get_curent_price import get_shoe_min_price, get_SOL, get_GMT, get_GST
from mint_price import get_mint_price
from level_up_price import get_level_up_price
from shoe import Shoe


def get_promised_cash(shoes):
    amount_of_shoes = len(shoes)
    match amount_of_shoes:
        case 0:
            print(0)
        case 1:
            print(1)
        case 2:
            print(2)
        case _:
            print('more then 2')


def level_up_our(to):
    price = 0
    sol = 0
    gst = 0
    gmt = 0
    time = 0
    level_up_price = get_level_up_price(5, to)
    gst += level_up_price[0]
    gmt += level_up_price[1]
    time += level_up_price[2]
    price += gst * get_GST() + gmt * get_GMT()
    print(f"{gst} - GST, {gmt} - GMT, {time} - время, цена в доларах {price}$")


def zero_case():
    price = 0
    sol = 0
    gst = 0
    gmt = 0
    time = 0
    earn = 0
    price_for_shoe_sol = get_shoe_min_price()
    time += 48
    sol += (price_for_shoe_sol + 2)  * 2
    level_up_price = get_level_up_price(0, 5)
    gst += level_up_price[0] * 2
    gmt += level_up_price[1] * 2
    time += level_up_price[2] * 2
    shoe_1 = Shoe(0, 1)
    shoe_2 = Shoe(0, 1)
    shoes = [shoe_1, shoe_2]
    shoe_info = shoe_1.mint(shoe_2)
    shoes.append(shoe_info[0])
    for shoe in shoes:
        time += shoe.cooldown
        shoe.cooldown = 0
        # print(shoe.cooldown)
    gst += shoe_info[1][0]
    gmt += shoe_info[1][1]
    # price += gst * get_GST() + gmt * get_GMT() + sol * get_SOL()
    # earn -= price
    earn += price_for_shoe_sol * get_SOL()
    # print(f'{earn} - earn, {time} - time, {gst} - GST, {gmt} - GMT, {sol} - SOL, {price} - price')
    time += 48
    gst += level_up_price[0]
    gmt += level_up_price[1]
    time += level_up_price[2]
    shoe_info = shoes[2].mint(shoes[0])
    gst += shoe_info[1][0]
    gmt += shoe_info[1][1]
    # price += gst * get_GST() + gmt * get_GMT() + sol * get_SOL()
    # earn -= price
    earn += price_for_shoe_sol * get_SOL()
    for shoe in shoes:
        time += shoe.cooldown
        shoe.cooldown = 0
    shoe_info = shoes[2].mint(shoes[1])
    gst += shoe_info[1][0]
    gmt += shoe_info[1][1]
    # price += gst * get_GST() + gmt * get_GMT() + sol * get_SOL()
    # earn -= price
    earn += price_for_shoe_sol * get_SOL()
    # for shoe in shoes:
    #     time += shoe.cooldown
    #     shoe.cooldown = 0
    earn += price_for_shoe_sol * get_SOL() * 2
    price += gst * get_GST() + gmt * get_GMT() + sol * get_SOL()
    print(f'{earn} - earn, {time} - time, {gst} - GST, {gmt} - GMT, {sol} - SOL, {price} - price')


def our_case():
    price = 0
    sol = 0
    gst = 0
    gmt = 0
    time = 0
    earn = 0
    price_for_shoe_sol = get_shoe_min_price()
    shoe_1 = Shoe(1, 1)
    shoe_2 = Shoe(1, 1)
    shoe_3 = Shoe(0, 1)
    shoes = [shoe_1, shoe_2, shoe_3]
    time += 48
    shoe_info = shoes[2].mint(shoes[0]) # минт илья и мама
    gst += shoe_info[1][0]
    gmt += shoe_info[1][1]
    shoes[2].cooldown -= 48
    new_shoes = [shoe_info[0]]
    time += 48
    shoe_info = shoes[2].mint(shoes[1]) # минт папа и мама
    gst += shoe_info[1][0]
    gmt += shoe_info[1][1]
    new_shoes.append(shoe_info[0])
    level_up_price = get_level_up_price(0, 5)
    gst += level_up_price[0] * 2    # увеличение уровня на 2х новых кросовках
    gmt += level_up_price[1] * 2
    time += level_up_price[2]

    shoe_info = new_shoes[0].mint(new_shoes[1]) # минт одного новго со всторым
    new_shoes.append(shoe_info[0])
    for shoe in new_shoes:
        time += shoe.cooldown
        shoe.cooldown = 0
    gst += shoe_info[1][0]
    gmt += shoe_info[1][1]
    time += 48

    gst += level_up_price[0] # увеличение уровня на 3ем
    gmt += level_up_price[1]
    time += level_up_price[2]

    shoe_info = new_shoes[2].mint(new_shoes[0]) # минт 3 с 1
    new_shoes.append(shoe_info[0])
    gst += shoe_info[1][0]
    gmt += shoe_info[1][1]
    for shoe in new_shoes:
        time += shoe.cooldown
        shoe.cooldown = 0

    shoe_info = new_shoes[2].mint(new_shoes[1]) # минт 3 с 2
    new_shoes.append(shoe_info[0])
    gst += shoe_info[1][0]
    gmt += shoe_info[1][1]

    for shoe in new_shoes:
        earn += (price_for_shoe_sol - (price_for_shoe_sol/100 * 6)) * get_SOL()
    earn += 4 * get_SOL()
    price += gst * get_GST() + gmt * get_GMT() + sol * get_SOL()
    print(f'{earn} - earn, {time} - time, {gst} - GST, {gmt} - GMT, {sol} - SOL, {price} - price')
    # итоговый результат при минте до 2 уровня

    for shoe in new_shoes:
        time += shoe.cooldown
        shoe.cooldown = 0


def mint_uncommon(price_uncommon):
    price = 0
    sol = price_uncommon * 2
    gst = 0
    gmt = 0
    time = 0
    earn = 0
    shoe_1 = Shoe(0, 2)
    shoe_2 = Shoe(0, 2)
    level_up_price = get_level_up_price(0, 5)
    gst += level_up_price[0] * 2  # увеличение уровня на 2х новых кросовках
    gmt += level_up_price[1] * 2
    time += level_up_price[2]
    shoe_info = shoe_1.mint(shoe_2)
    gst += shoe_info[1][0]
    gmt += shoe_info[1][1]
    new_shoe = shoe_info[0]
    print(f'{gst * get_GST() + gmt * get_GMT()} mint price')
    earn += ((price_uncommon - 3 - ((price_uncommon - 3)/100 * 6)) * get_SOL()) * 3
    price += gst * get_GST() + gmt * get_GMT() + sol * get_SOL()
    print(f'{earn} - earn, {time} - time, {gst} - GST, {gmt} - GMT, {sol} - SOL, {price} - price')


# zero_case()

# our_case()

mint_uncommon(43)

# level_up_our(30)
# sol = get_SOL()
# new = 42 * sol
# our = 18 * sol
# raz = new - our
# print(new)
# print(our)
# print(raz)