bool susu(int i){
    return i%2==0;
}

main_program{
    int n;
    cin>>n;
    stack<int> s;
    for(int i = 0; i < n; i = i + 1)
    {
        s.push(i);
    }
    for(int i = 0; i < n; i = i + 1)
    {
        int a = s.top();
        cout<<susu(a)<<endl;
        s.pop();
    }
}
