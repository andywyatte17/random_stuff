//
// main.cpp
//

#include "node.h"
#include "node_algos.h"

struct S {
  std::string uuid;
  S() = default;
  S(const S&) = default;
  S& operator=(const S&) = default;
};

int main(int n, char**)
{
  using Node_t = Node<S>;

  auto MakeNode = [](std::string uuid) {
    Node_t node;
    node.mutate_base_data([&](S& s) { s.uuid = uuid; });
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

  auto a = MakeNode("A");
  a.push_back(Make_BDF());
  a.push_back(Make_CG());
  a.push_back(Make_E());

  auto f = DFS(&a);
  for (;;) {
    auto p = f();
    if (!p)
      break;
    printf("%s", p->base_data()->uuid.c_str());
  }
  printf("\n");
}