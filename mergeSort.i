// #include<iostream>

// using namespace std;

int arr[4];
int n;

void mergesort(int start, int end)
{
	if (start>=(end-1)){return;}
	else
	{
		int middle = (start+end)/2;
		mergesort(start, middle);
		mergesort(middle, end);
		int firstIndex = start, secondIndex = middle;
		int index = start;
		int temp[n];
		while ((firstIndex < middle) && (secondIndex < end))
		{
			if (arr[firstIndex]<arr[secondIndex])
			{
				temp[index] = arr[firstIndex];
				firstIndex += 1;
			}
			else
			{
				temp[index] = arr[secondIndex];
				secondIndex += 1;
			}
			index += 1;
		}
		while (firstIndex < middle)
		{
			temp[index] = arr[firstIndex];
			firstIndex += 1;
			index += 1;
		}
		while (secondIndex < end)
		{
			temp[index] = arr[secondIndex];
			secondIndex += 1;
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