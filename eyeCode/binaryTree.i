int main(){
	binarySearchTree<int> bst;
    bst.insert(3);
	bst.insert(1);
	bst.insert(2);
	bst.insert(0);
	bst.insert(5);
    bst.insert(4);
	bst.insert(6);
    int x = bst.search(1);
    bst.erase(1);
}
