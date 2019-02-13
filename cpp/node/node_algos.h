//
// node_algos.h
//

#pragma once

#include "node.h"
#include <algorithm>
#include <functional>
#include <vector>

/// Depth-first search
inline std::function<const Node*()> DFS(const Node* node)
{
  std::vector<const Node*> stack;
  stack.push_back(node);
  return [=]() mutable -> const Node* {
    if (stack.empty())
      return static_cast<const Node*>(nullptr);
    auto top = stack.back();
    stack.pop_back();
    auto* pStack = &stack;
    std::for_each(top->m_childNodes.rbegin(), top->m_childNodes.rend(),
        [pStack](const std::shared_ptr<const Node>& sp) {
          pStack->push_back(sp.get());
        });
    return top;
  };
}