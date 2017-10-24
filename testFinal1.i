main_program {
    int length = 5;
    stack<int> st, st1;
    queue<int> qu,qu1;
    int a[5];
    for (int i = 0; i < length; i = i + 1)
    {
        st.push(i);
        qu.pushBack(i);
    }
    for (int i = 0; i < length; i = i + 1)
    {
        st1.push(st.top());
        st.pop();
        qu1.pushBack(qu.front());
        qu.popFront();
    }
}
