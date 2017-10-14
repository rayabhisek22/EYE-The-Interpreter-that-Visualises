int x = 100;

int pow(int a, int b){
	int res = 1;
	for(int i = 0; i < b; i = i + 1){
		res = res * a;
	}
	return res;
}

int animesh(int a, int b){
	return pow(a, b);
}

main_program{
	cout << animesh(2, 3);
}