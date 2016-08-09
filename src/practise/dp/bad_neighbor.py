donation = [ 10, 3, 2, 5, 7, 8 ]
donation = [ 11, 15 ]
donation = [ 7, 7, 7, 7, 7, 7, 7 ]
donation = [ 94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 ]
  
donation = [ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ]


max_donation_at_i = [ -1 for i in range(len(donation)) ]
is_first_choosen_at_i = [ 0 for i in range(len(donation)) ]

def calculate_max_donation():
  max_donation_at_i[0] = donation[0]
  is_first_choosen_at_i[0] = 1
  max_donation_at_i[1] = max(donation[1],max_donation_at_i[0])
  is_first_choosen_at_i[1] = 0 if donation[1]>max_donation_at_i[0] else 1
  for i in range(2, len(max_donation_at_i)):
    if not (i == len(max_donation_at_i) - 1 and is_first_choosen_at_i[i-2] == 1):
      max_donation_at_i[i] = max(donation[i]+max_donation_at_i[i-2],max_donation_at_i[i-1])
      is_first_choosen_at_i[i] = is_first_choosen_at_i[i-2] if (donation[i]+max_donation_at_i[i-2]
                        >max_donation_at_i[i-1]) else is_first_choosen_at_i[i-1]
    else:
      max_donation_at_i[i] = max(donation[i],max_donation_at_i[i-1])
      is_first_choosen_at_i[i] = 0 if donation[i] > max_donation_at_i[i-1] else is_first_choosen_at_i[i-1]
                                   


calculate_max_donation()

print max_donation_at_i[-1]
                                  