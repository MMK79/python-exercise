def dream_home(yearly_salary, portion_saved, cost_of_dream_home):
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
    return count

# yearly_salary = int(input("Enter your yearly salaery"))
# portion_saved = float(input("Enter your how much you want to save"))
# cost_of_dream_home = int(input("Enter your dream home cost"))
print(dream_home(112000, 0.17, 750000))
print(dream_home(65000, 0.2, 400000))
print(dream_home(35000, 0.3, 1000000))
