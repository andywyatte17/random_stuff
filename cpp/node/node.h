//
// node.h
//

#pragma once

#include <memory>
#include <string>
#include <vector>

enum class NodeType {
  root,
  group,
};

struct INodeData {
  virtual ~INodeData() {}
};

struct Node {
  Node() {}
  std::vector<std::shared_ptr<const Node>> m_childNodes;
  std::shared_ptr<const INodeData> m_nodeData;
  std::shared_ptr<const std::string> m_uuid;
  void push_back(const Node& node);
};

inline void Node::push_back(const Node& node)
{
  m_childNodes.push_back(std::make_shared<Node>(std::move(node)));
}
