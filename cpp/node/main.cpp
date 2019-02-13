//
// main.cpp
//

#include "node.h"
#include "node_algos.h"

int main(int n, char**)
{
  auto MakeNode = [](std::string uuid) {
    Node node;
    node.m_uuid = std::make_shared<std::string>(uuid);
    return node;
  };

  /*
  A
  B    C     E 
  DF   G

  DFS: ABDFCGE
  */

  auto Make_BDF = [=]() {
    auto b = MakeNode("B");
    b.push_back(MakeNode("D"));
    b.push_back(MakeNode("F"));
    return b;
  };

  auto Make_CG = [=]() {
    auto c = MakeNode("C");
    c.push_back(MakeNode("G"));
    return c;
  };

  auto Make_E = [=]() {
    return MakeNode("E");
  };

  Node a = MakeNode("A");
  a.push_back(Make_BDF());
  a.push_back(Make_CG());
  a.push_back(Make_E());

  auto f = DFS(&a);
  for (;;) {
    auto p = f();
    if (!p)
      break;
    printf("%s", p->m_uuid->c_str());
  }
  printf("\n");
}