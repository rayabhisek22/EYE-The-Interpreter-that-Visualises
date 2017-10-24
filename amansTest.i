stack<int> s1;
stack<int> s2;

void refill()
{
    while(!s1.empty())
    {
        s2.push(s1.top());
        s1.pop();
    }
    return 0;
}

main_program{
    string s;
    cin>>s;
    while(true)
    {
        if (s == "push")
        {
            int n;
            cin>>n;
            s1.push(n);
        }
        elif (s == "top")
        {
            if (s1.empty() && s2.empty())
            {
                cout<<"the queue is empty"<<endl;
            }
            elif(s2.empty())
            {
                refill();
                cout<<s2.top()<<endl;
            }
            else
            {
                cout<<s2.top()<<endl;
            }
        }
        elif (s == "pop")
        {
            if (s1.empty() && s2.empty())
            {
                cout<<"the queue is empty"<<endl;
            }
            elif(s2.empty())
            {
                refill();
                s2.pop();
            }
            else
            {
                s2.pop();
            }
        }
        else
        {
            cout<<"wrong command"<<endl;
        }
        cin>>s;
    }
}


