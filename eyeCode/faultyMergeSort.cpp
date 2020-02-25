// #include<iostream>

// using namespace std;

long arr[4];
long n;

long mergesort(long start, long end)
{	
	long num_inv = 0;
	if (start>(end-1)){return 0;}
	else
	{
		long middle = (start+end)/2;
		long v1 = mergesort(start, middle);
		long v2 = mergesort(middle, end);
		long fIndex = start, sIndex = middle;
		long index = start;
		long tmp[n];
		num_inv += v1 + v2;
		
		while ((fIndex < middle) && (sIndex < end))
		{
			if (arr[fIndex]<=arr[sIndex])
			{
				tmp[index] = arr[fIndex];
				fIndex += 1;
			}
			else
			{
				tmp[index] = arr[sIndex];
				sIndex += 1;
				num_inv += middle-fIndex;
			}
			index += 1;
		}
		while (fIndex < middle)
		{
			tmp[index] = arr[fIndex];
			fIndex += 1;
			index += 1;
		}
		while (sIndex < end)
		{
			tmp[index] = arr[sIndex];
			sIndex += 1;
			index += 1;
			num_inv += middle-fIndex;
		}
		for (long i = start; i < end ; i +=1)
		{
			arr[i] = tmp[i];
		}
	}
	return num_inv;
}

int main()
{
	cin>>n;
	for (long i = 0 ; i < n  ; i += 1)
	{
		cin>>arr[i];
	}
	 long v = mergesort(0, n);
	// for (long i = 0 ; i < n ; i += 1)
	// {
	// 	cout<<arr[i]<<" ";
	// }
	// cout<<endl;
	cout<<v;
}
