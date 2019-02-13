//
// node.h
//

#pragma once

#include <functional>
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

template <typename BaseData>
class Node {
  public:
  using BaseData_t = BaseData;
  using Node_t = Node<BaseData_t>;
  using V_t = std::vector<std::shared_ptr<const Node_t>>;

  private:
  std::shared_ptr<const BaseData_t> m_baseData;
  V_t m_childNodes;

  public:
  Node() {}

  void push_back(const Node_t& node)
  {
    m_childNodes.push_back(std::make_shared<Node_t>(node));
  }

  void push_back(Node_t&& node)
  {
    m_childNodes.push_back(std::make_shared<Node_t>(std::move(node)));
  }

  const BaseData_t* base_data() const
  {
    return m_baseData.get();
  }

  //template <typename Fn>
  //void mutate_base_data(Fn&& fn)
  void mutate_base_data(std::function<void(BaseData_t&)> fn)
  {
    if (!m_baseData) {
      auto pbd = std::make_shared<BaseData_t>();
      BaseData_t& bd = *pbd;
      fn(bd);
      m_baseData = pbd;
    } else {
      auto pbd = std::make_shared<BaseData_t>(*m_baseData);
      BaseData_t& bd = *pbd;
      fn(bd);
      m_baseData = pbd;
    }
  }

  const V_t& ChildNodes() const
  {
    return m_childNodes;
  }
};
