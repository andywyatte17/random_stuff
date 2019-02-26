// tree_in_raw_storage.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
// ...
#include "tree.h"
#include <vector>

int main()
{
  std::vector<std::unique_ptr<INode>> v;
  for (int i = 0; i < 1000; ++i)
  {
    printf("\n%d\n\n", i);
    auto pRoot = MakeHolderNode();
    pRoot->add_child(MakeLeafNode());

    auto p1 = dynamic_cast_to_LeafNode(pRoot.get());
    auto p2 = dynamic_cast_to_LeafNode(&(pRoot->at(0)));
    printf("%p\n", p1);
    printf("%p\n", p2);

    printf("%10.1f\n", reinterpret_cast<uint64_t>(pRoot->content()) / double(pRoot->contentAlignof()));
    printf("%10.1f\n", reinterpret_cast<uint64_t>(pRoot->at(0).content()) / double((pRoot->at(0).contentAlignof())));

    v.push_back(std::move(pRoot));
  }
  return 0;
}

