smallest_so_far = 100
print ('Before', smallest_so_far)
for the_num in [8 ,20 ,2 ,45 ,99 ,10 ,21] :
	if the_num < smallest_so_far :
		smallest_so_far = the_num
	print (smallest_so_far, the_num)
print('After', smallest_so_far)