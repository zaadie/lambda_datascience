#EXERCISE 1
mile_1 = 0
mile_2 = 0
total_gas = 0
fares_1 = 0
fares_2 = 0
total_fares = 0
profit_1 = 0
profit_2 = 0
total_profit = 0
tankSize = 20
miles_travelled = [160, 220]
passenger_total = [23, 17]
fare_avg = [29, 30]
gas_prices = [3.52, 3.57]



def gas():
    mile_1 = (gas_prices[0] / tankSize) * miles_travelled[0]
    mile_2 = (gas_prices[1] / tankSize) * miles_travelled[1]
    total_gas = mile_1 + mile_2
    return total_gas


def fares():
    fares_1 = fare_avg[0] * passenger_total[0]
    fares_2 = fare_avg[1] * passenger_total[1]
    total_fares = fares_1 + fares_2
    return total_fares


def profit():
    return fares() - gas()


def week_1_fares():
    fares_1 = fare_avg[0] * passenger_total[0]
    return fares_1


def week_1_gas():
    mile_1 = (gas_prices[0] / tankSize) * miles_travelled[0]
    return mile_1


def week_1_profit():
    profit_1 = (week_1_fares() - week_1_gas())/ passenger_total[0]
    return profit_1


def week_2_fares():
    fares_2 = fare_avg[1] * passenger_total[1]
    return fares_2


def week_2_gas():
    mile_2 = (gas_prices[1] / tankSize) * miles_travelled[1]
    return mile_2


def week_2_profit():
    profit_2 = (week_2_fares() - week_2_gas())/ passenger_total[1]
    return profit_2


def final_display():
    print'Total Profit (both weeks): $', profit()
    print'Week 1 Passenger Profit: $', week_1_profit()
    print'Week 2 Passenger Profit: $', week_2_profit()

final_display()
