{
	int arr[11];
	for (int i = 0; i < 11; i = i + 1)
	{
		arr[i] = (i*8) % 11;
	}
	for (int i = 0; i < 11; i = i + 1)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
	for (int i = 0; i < 11; i = i + 1)
	{
		for (int j = i; j < 11; j = j + 1)
		{
			if (arr[i] > arr[j])
			{
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
	for (int i = 0; i < 11; i = i + 1)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}