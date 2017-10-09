main_program {
int n=5;
	int a[n];
	for (int i = 0 ; i < n ; i = i +1)
	{
		a[i] = (8*(i+1))%17;
	}
	for(int i=0;i<n;i=i+1)
	{
		for(int j=0;j<n-i-1;j=j+1)
		{
		cout<<j<<" "<<n-i-1<<endl;
			if(a[j]>a[j+1])
			{

				int temp=a[j+1];
				a[j+1]=a[j];
				a[j]=temp;
			}
		}
	}
}
