#include "LinkedList.hpp"

int main()
{
    LinkedList bob = LinkedList();
    bob.push(0);
    bob.push(1);
    bob.push(2);

    std::cout << bob.pop();
}