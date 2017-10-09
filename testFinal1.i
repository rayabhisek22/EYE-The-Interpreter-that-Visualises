main_program {
    int length = 5;
    stack<int> st, st1;
    queue<int> qu,qu1;
    linkedList<int> li, li1;
    for (int i = 0; i < length; i = i + 1)
    {
	li.push(i);
    }
    for (int i = 0; i < length; i = i + 1)
    {
	li1.push(li.top());
	li.erase(li.top());
    }
}
