int main(){
	binarySearchTree<int> bst;
	for (int i = 1 ; i < 6 ; i = i + 1){
		bst.insert(0);
		bst.insert(3);
		bst.insert(1);
		bst.insert(4);
		bst.insert(2);
	}
	bst.search(8);
	bst.erase(3);
	bst.search(8);
}