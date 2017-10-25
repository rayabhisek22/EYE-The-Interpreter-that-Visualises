int fib(int n)
{
	if (n == 1)
	{
		return 1;
	}
	if (n == 2)
	{
		return 2;
	}
	return fib(n-1) + fib(n-2);
}

int main()
{
	int n;
	cin>>n;
	cout<<fib(n)<<endl;
}