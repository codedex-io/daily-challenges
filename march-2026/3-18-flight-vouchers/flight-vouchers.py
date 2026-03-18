def pick_voucher(vouchers, delays, max_wait):
  best_option_index = -1
  best_option_value = -1

  # for every element in vouchers
  for i in range(len(vouchers)):
    # if the delay is shorter or equal to max_wait
    # and strictly over 0 to avoid a division of 0
    if delays[i] <= max_wait and delays[i] > 0:
      # calculate the dollars per hour waited
      dollars_per_hour_waited = vouchers[i] / delays[i]
      # if strictly over the current best option value
      # and not higher or equal because we only keep
      # the first one
      if dollars_per_hour_waited > best_option_value:
        # we set the best option index and value to
        # current values
        best_option_index = i
        best_option_value = dollars_per_hour_waited

  return best_option_index