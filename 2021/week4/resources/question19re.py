def fibonacci_r(n) :
 	if n==0 or n==1 :
        	return n
    	else :
        	return fibonacci_r(n-1) + fibonacci_r(n-2)