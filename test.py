{
	int x=3,y=5;
	y=x+3;
	for (int i = 0 ; i< 2 ; i = i +1)
	{
		int temp = x;
		x = y;
		y = temp;
	}
}
