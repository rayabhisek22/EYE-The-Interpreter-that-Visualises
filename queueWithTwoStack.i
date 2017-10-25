stack<int> s1;
binarySearchTree<int> BinarySearchTree;
stack<int> s2;
queue<int> q;
hashTable<int> h(9);
void refill()
{
    while(!s1.empty())
    {
        s2.push(s1.top());
        s1.pop();
    }
    return;
}

int main(){
    string s;
    cin>>s;
    while(true)
    {
        if (s == "push")
        {
            int n;
            cin>>n;
            s1.push(n);
            q.pushBack(n);
            h.push(n);
            BinarySearchTree.insert(n);
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
            cout<<q.front()<<endl;
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
            q.popFront();
        }
        else
        {
            cout<<"wrong command"<<endl;
        }
        cin>>s;
    }
}