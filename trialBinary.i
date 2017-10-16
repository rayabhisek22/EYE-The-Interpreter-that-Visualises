main_program{
	binarySearchTree<int> bst;
	for (int i = 1 ; i < 6 ; i = i + 1){
		bst.insert((i*8)%13);
	}
	bst.search(8);
	bst.erase(3);
	bst.search(8);
}