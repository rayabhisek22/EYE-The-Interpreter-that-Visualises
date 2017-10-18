int gcd(int a,int b)
{
	if(a%b==0)
	{
		return b;
	}
	else
	{
		return gcd(b,a%b);
	}
}

main_program{
	int n=5;
	int a[n];
	for(int i=0;i<n;i=i+1)
	{
		a[i]=2*i;
	}
	cout<<gcd(a[1],a[3])<<endl;
}