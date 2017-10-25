int main()
{
    stack<   int> s ;
    linkedList<int   > l;
    queue<  int  > q;

    for(int inti = 0; inti < 20; inti+=1)
    {
        s.push(inti);
        q.pushBack (inti);
        l.push(inti);
    }
    cout<<endl;
}
