// #include<iostream>

// using namespace std;

int arr[4];
int n;

void mergesort(int start, int end)
{
	if (start>=end){return;}
	else
	{
		int middle = (start+end)/2;
		mergesort(start, middle);
		mergesort(middle, end);
		int fIndex = start, sIndex = middle;
		int index = start;
		int temp[n];
		while ((fIndex < middle) && (sIndex < end))
		{
			if (arr[fIndex]<arr[sIndex])
			{
				temp[index] = arr[fIndex];
				fIndex += 1;
			}
			else
			{
				temp[index] = arr[sIndex];
				sIndex += 1;
			}
			index += 1;
		}
		while (fIndex < middle)
		{
			temp[index] = arr[fIndex];
			fIndex += 1;
			index += 1;
		}
		while (sIndex < end)
		{
			temp[index] = arr[sIndex];
			sIndex += 1;
			index += 1;
		}
		for (int i = start; i < end ; i +=1)
		{
			arr[i] = temp[i];
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