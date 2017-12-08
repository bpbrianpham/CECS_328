#include "BST.h"

	//default constructor
template <class T>
BST<T>::BST()
{
	root = nullptr;
}

	//destructor
template <class T>
BST<T>::~BST()
{
	destroyTree(root);
}

	//destroyTree
template <class T>
void  BST<T>::destroyTree()
{
	destroyTree(root);
}

	//inorderTraversal
template <class T>
void BST<T>::inorderTraversal() const
{
	if (root == nullptr)
		cerr << "There is no tree.";
	else
	{
		inorderTraversal(root);
	}
}

	//totalNodes
template <class T>
int BST<T>::totalNodes() const
{
	if (root == nullptr)
		return 0;
	else
		return totalNodes(root);
}

	//destroy
template <class T>
void  BST<T>::destroyTree(Node<T>* &p)
{
	if(p != nullptr)
	{
		destroyTree(p->llink);
		destroyTree(p->rlink);
		delete p;
		p = nullptr;
	}
}

/***************************************************************

	Implement your functions below this line.

***************************************************************/

//// Definition function insert (non-recursive)
//template <class T>
//void BST<T>::insert(const T& elem)
//{
//	Node<T> *current = new Node<T>;
//	Node<T> *parent;
//	current->data = elem;
//	current->llink = nullptr;
//	current->rlink = nullptr;
//	parent = nullptr;
//
//	if (root == nullptr)
//		root = current;
//	else
//	{
//		Node<T> *temp = new Node<T>;
//		temp = root;
//		while (temp)
//		{
//			parent = temp;
//			if (current->data > temp->data)
//				temp = temp->rlink;
//			else
//				temp = temp->llink;
//		}
//		if (current->data < parent->data)
//			parent->llink = current;
//		else
//			parent->rlink = current;
//	}
//}

//Definition function insert (recursive)
template <class T>
void BST<T>::insert(const T& d)
{
		insert(d, root);
}


// Definition overloaded function insert (recursive)
template <class T>
void BST<T>::insert(const T& d, Node<T>* p)
{
	if (p == nullptr)
	{
		Node<T> *newNode = new Node<T>;
		newNode->data = d;
		newNode->llink = nullptr;
		newNode->rlink = nullptr;
		root = newNode;
	}
	else
	{
		if (d < p->data)
		{
			if (p->llink == nullptr) 
			{
				Node<T> *newNode = new Node<T>;
				newNode->data = d;
				newNode->llink = nullptr;
				newNode->rlink = nullptr;
				p->llink = newNode;
			}
			else 
				insert(d, p->llink);
		}
		else if (d > p->data) 
		{
			if (p->rlink == nullptr) 
			{
				Node<T> *newNode = new Node<T>;
				newNode->data = d;
				newNode->llink = nullptr;
				newNode->rlink = nullptr;
				p->rlink = newNode;
			}
			else 
				insert(d, p->rlink);
		}
		else
			cerr << "The item to insert is already in the list � duplicates are not allowed.�\n";
	}
}



// Definition overloaded function inorderTraversal(Node*)
template <class T>
void BST<T>::inorderTraversal(const Node<T>* newNode) const
{
	if (newNode != nullptr)
	{
		if (newNode->llink) 
		{
			inorderTraversal(newNode->llink);
			cout << " ";
		}
		cout << newNode->data;
		if (newNode->rlink)
		{
			cout << " ";
			inorderTraversal(newNode->rlink);
		}
	}

}

// Definition overloaded function totalNodes(Node*)
template <class T>
int BST<T>::totalNodes(const Node<T>* newNode) const
{
	return ((newNode->llink) ? totalNodes(newNode->llink) : 0)
		+ 1 + ((newNode->rlink) ? totalNodes(newNode->rlink) : 0);
}


