// #include<iostream>

// using namespace std;

int n;
int arr[6];

void mergesort(int start, int end)
{
	if (start>=(end-1)){return;}
	else
	{
		int middle = (start+end)/2;
		mergesort(start, middle);
		mergesort(middle, end);
		int fIndex = start, sIndex = middle;
		int index = start;
		int tmp[n];
		while ((fIndex < middle) && (sIndex < end))
		{
			if (arr[fIndex]<arr[sIndex])
			{
				tmp[index] = arr[fIndex];
				fIndex += 1;
			}
			else
			{
				tmp[index] = arr[sIndex];
				sIndex += 1;
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
		}
		for (int i = start; i < end ; i +=1)
		{
			arr[i] = tmp[i];
		}
	}
	return;
}

int main()
{
	cin>>n;
	for (int i = 0 ; i < n  ; i += 1)
	{
		cin>>arr[i];
	}
	mergesort(0, n);
	for (int i = 0 ; i < n ; i += 1)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}
