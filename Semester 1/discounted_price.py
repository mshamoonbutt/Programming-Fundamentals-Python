def discounted_price(price,discount_rates):
    final_price=price*discount_rates/100
    print(final_price)
    
price=int(input("Enter price: "))
discount_rates=int(input("Enter discount rates in %: "))    
discounted_price(price,discount_rates)
