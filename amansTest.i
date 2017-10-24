int main()
{
    stack<int> s ;
    linkedList<int> l;
    queue<int> q;

    for(int i = 0; i < 20; i+=1)
    {
        s.push(i);
        q.pushBack (i);
        l.push(i);
    }
    cout<<endl;
}
