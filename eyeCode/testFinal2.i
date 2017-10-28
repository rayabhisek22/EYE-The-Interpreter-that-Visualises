main_program
{
    int length = 5;
    int arr[length];
    for (int i = 0; i < length; i = i + 1)
    {
        arr[i] = (3*i) % 5;
    }
    for (int i = 0; i < length ; i = i + 1)
    {
        int j = i;
        while(j < length - 1)
        {
            if (arr[j+1] < arr[j])
            {
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
            j = j + 1;
        }
    }
}
