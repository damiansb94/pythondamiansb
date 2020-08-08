largest_so_far = -1
print ('Before', largest_so_far)
for the_num in [8 ,20 ,2 ,45 ,99 ,1 ,21] :
	if the_num > largest_so_far :
		largest_so_far = the_num
	print (largest_so_far, the_num)
print('After', largest_so_far)