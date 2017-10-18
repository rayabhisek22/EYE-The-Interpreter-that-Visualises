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
int y=2;
int f(int i)
{
	int a[i];
	for(int j=0;j<i;j +=1)
	{
		a[j]=g(j+1);
	}
	a[1]=5;
	float mult=1;
	for(int k=0;k<i;k=k+1)
	{
	if(k==2)
		{mult *=a[k];}
	}
	return mult;
}

int g(int x)
{
	return x/x*y+y/x;
} 

main_program{
	stack<int> st;
	int x=4;
	st.push(x+2);
	x=x+2;
	int y=x+3%5;
	st.push(y);
	int a=st.top();
	st.pop();
	int b=st.top();
	st.pop();
	int p=gcd(a,b);
	cout<<f(p)<<endl;
	y=y-1;
	cout<<y<<endl;
}