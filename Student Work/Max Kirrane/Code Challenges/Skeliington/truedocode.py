def list_sum_recursive
	if len(list) == 0:
		return 0

	else:
		return list[0] + list_sum_recursive(list[1:])
        


