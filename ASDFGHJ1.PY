def total_calc(bill_amount, tip_perc):
    tip_amont =(tip_perc/ 100) *bill_amount
    total = bill_amount* tip_amont
    print('bill amunt',bill_amount)
    print('tip,',tip_amont)
    print('g',total)
    return total
total_calc(1000,10)