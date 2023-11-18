original_amount_invested = int(1000)
rate_of_returns = float(0.07)
number_of_years1 = int(10)
number_of_years2 = int(20)
number_of_years3 = int(30)

amount_on_deposit1 = original_amount_invested * ((1 + rate_of_returns) ** number_of_years1)

total_money_after_ten_years = int(original_amount_invested + amount_on_deposit1)

print(f"Total money after 10 years equals ${total_money_after_ten_years}")

amount_on_deposit2 = total_money_after_ten_years * ((1 + rate_of_returns) ** number_of_years2)

total_money_after_twenty_years = int(total_money_after_ten_years + amount_on_deposit2)

print(f"Total money after 20 years equals ${total_money_after_twenty_years}")

amount_on_deposit3 = total_money_after_twenty_years * ((1 + rate_of_returns) ** number_of_years3)

total_money_after_thirty_years = int(total_money_after_twenty_years + amount_on_deposit3)

print(f"Total money after 30 years equals ${total_money_after_thirty_years}")
