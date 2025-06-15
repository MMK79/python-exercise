def dream_home(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
    portion_down_payment = 0.25
    amount_saved = 0
    r = 0.05
    count = 0
    desire_amount = cost_of_dream_home*portion_down_payment

    while desire_amount > amount_saved:
        # print(amount_saved * (r/12), yearly_salary / 12 * portion_saved) # Debug
        amount_saved += ( amount_saved * (r/12) ) 
        amount_saved += ( yearly_salary / 12 * portion_saved )
        count += 1
        if count % 6 == 0:
            yearly_salary = yearly_salary + yearly_salary*semi_annual_raise
            # print(yearly_salary) # Debug
        # Debug
        # if count > 100:
        #     break
        # print(amount_saved, count) # Debug
    return count

# yearly_salary = int(input("Enter your yearly salaery"))
# portion_saved = float(input("Enter your how much you want to save"))
# cost_of_dream_home = int(input("Enter your dream home cost"))
# semi-annual_raise = int(input("Enter your annual raise"))
print(dream_home(110000, 0.15, 750000, 0.03))
print(dream_home(350000, 0.3, 10000000, 0.05))
