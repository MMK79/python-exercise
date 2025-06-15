def rate(init_amount, error = 100):
    dream_house_payment = 800000
    down_payment_rate = 0.25
    count = 0
    high = 1
    low = 0
    need_payment = dream_house_payment*down_payment_rate
    flag = True
    while flag:
        amount_saved = init_amount
        r = ( high+low )/2
        for i in range(36):
            amount_saved = amount_saved*(1+r/12)
        #     print(i, amount_saved)
        # print(high, low, r, amount_saved)
        if abs(need_payment - amount_saved) > error:
            if amount_saved > need_payment:
                # print(f"you needed {need_payment} and you saved {amount_saved} with {r} interesert rate")
                # print("high set to r")
                high = r
            else:
                # print(f"you needed {need_payment} but you only saved {amount_saved} with {r} interesert rate")
                # print("low set to r")
                low = r
        else:
            flag = False
            return (r, count)
        count += 1
        if count > 100:
            break

print(rate(65000))
print(rate(150000))
print(rate(1000))
