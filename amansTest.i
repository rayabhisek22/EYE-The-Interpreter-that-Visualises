int factorial(int a)
{
    if (a == 0)
    {
        return 1;
    }
    else
    {
        return a*factorial(a-1);
    }
}
main_program
{
        cout << factorial(3) ;
}
