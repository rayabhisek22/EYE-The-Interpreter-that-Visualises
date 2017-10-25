int x=10;

int gcd(int a,int b)
{
	x=x-1;
	if(a%b==0)
	{
		return b;
	}
	return gcd(b,a%b);
}

int lcm(int a, int b)
{
	return (a*b)/gcd(a,b);
}

int factorial(int n)
{
	if (n==0)

	{
	return  1;
	}
	return n*factorial(n-1);
}

main_program
{
/*
	doublyLinkedList<int> d;
	d.push(90);	
	d.push(85);
	d.insert(1,30);
	d.get(1);
	cout<<d.top()<<endl;
	cout<<d.indexOf(85)<<endl;
	*/
	hashTable<int> h(29);
	for (int i = 0 ; i < 15 ; i =i+ 1)
	{
		h.push((i+1)*49);
	}
	cout<<h.find(49)<<endl;
	h.erase(98);
}