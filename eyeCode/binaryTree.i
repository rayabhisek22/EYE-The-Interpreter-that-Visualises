int main(){
	binarySearchTree<int> bst;
	for (long i = 1 ; i < 2 ; i = i + 1){
		bst.insert(1);
		bst.insert(2);
	}
	int x = bst.search(2);
	for (long j = 1 ; j < 2 ; j = j + 1){
		bst.insert(3);
		bst.insert(4);
	}
//	bst.erase(3);
//	bst.search(8);
}
