int fib(int n)
{
	if(n==0)
	{
		return 0;
	}
	elif(n==1)
	{
		return 1;
	}
	return fib(n-1)+fib(n-2);
}

main_program{
	cout<<fib(4);
}