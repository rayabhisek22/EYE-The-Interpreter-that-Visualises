stack<int> Stack;
binarySearchTree<int> BinarySearchTree;
queue<int> Queue;
hashTable<int> HashTable(6);
int arr[10];

int main(){
    for(int i = 3; i >= 0; i-=1)
    {
        Stack.push(i);
        BinarySearchTree.insert((i*3)%7);
        Queue.pushFront(i);
        HashTable.push(i*2);
        arr[5-i] = i; 
    }
    for(int i = 4; i < 7; i+=1)
    {
        Stack.push(i);
        BinarySearchTree.insert(((i*3)%7) - 4);
        Queue.pushFront(i);
        HashTable.push(i*2);
        arr[i] = i; 
    }
}