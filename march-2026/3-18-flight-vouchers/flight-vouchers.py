# Flight Vouchers 🏖️
# Alan

def pick_voucher(vouchers, delays, max_wait):
  best_option_index = -1
  best_option_value = -1

  for i in range(len(vouchers)):
    if delays[i] <= max_wait and delays[i] > 0:
      dollars_per_hour_waited = vouchers[i] / delays[i]
      if dollars_per_hour_waited > best_option_value:
        best_option_index = i
        best_option_value = dollars_per_hour_waited

  return best_option_index
