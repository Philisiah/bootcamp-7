def find_max_min(x):
	max_, min_ = x[0], x[0]
	list_ = []
	for i in x:
		if i > max_:
			max_= i
		if i < min_:
			min_ = i 
	if max_ == min_:
	  list_.append(len(x))
	  return list_
	else:
		list_.append(min_)
		list_.append(max_)
		return list_