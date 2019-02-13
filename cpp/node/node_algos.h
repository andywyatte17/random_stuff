//
// node_algos.h
//

#pragma once

#include "node.h"
#include <algorithm>
#include <functional>
#include <vector>

/// Depth-first search
template <typename BaseData>
inline auto DFS(const Node<BaseData>* node, bool reverse = false) -> std::function<const Node<BaseData>*()>
{
  using Node_t = Node<BaseData>;
  std::vector<const Node_t*> stack;
  stack.push_back(node);
  return [=]() mutable -> const Node_t* {
    auto f = [&](const std::shared_ptr<const Node_t>& sp) {
      stack.push_back(sp.get());
    };
    if (stack.empty())
      return nullptr;
    auto top = stack.back();
    stack.pop_back();
    if (reverse) {
      std::for_each(top->ChildNodes().begin(), top->ChildNodes().end(), f);
    } else {
      std::for_each(top->ChildNodes().rbegin(), top->ChildNodes().rend(), f);
    }
    return top;
  };
}