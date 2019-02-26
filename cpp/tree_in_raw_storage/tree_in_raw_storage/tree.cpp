//
// tree.cpp
//

#include "stdafx.h"
// ...
#include <vector>
#include "tree.h"
#include <stdexcept>
// ...

template<typename T, typename ContentT>
static ContentT& get_v_impl(T& rThis, ContentT*)
{
  constexpr auto aoc = alignof(ContentT);
  static_assert(T::Checker<T::aligner - aoc>::ok, "...");
  auto p = reinterpret_cast<uint64_t>(rThis.m_buffer.data());
  constexpr auto myAlign = alignof(ContentT);
  auto pi = p % myAlign;
  if (pi)
    p = p + myAlign - pi;
  return *reinterpret_cast<ContentT*>(p);
}

template<typename Content>
struct ContentNode : INode
{
  Content& get_v()
  {
    return get_v_impl(*this, (Content*)nullptr);
  }

  const Content& get_v() const
  {
    return get_v_impl(*this, (const Content*)nullptr);
  }

  const void* content() const { return &get_v(); }

  unsigned contentAlignof() const
  {
    return alignof(Content);
  }

  ContentNode()
  {
    static_assert(Checker<N - sizeof(Content)>::ok, "...");
    new(&get_v()) Content();
  }

  ~ContentNode()
  {
    get_v().~Content();
  }
};

struct Holder
{
  INode* m_pParent = nullptr;
  std::vector<std::shared_ptr<const INode>> m_v;
};

struct HolderNode : ContentNode<Holder>
{
  struct Content
  {
    INode* m_pParent = nullptr;
    std::vector<std::shared_ptr<const INode>> m_v;
  };

  bool is_leaf() const override { return false; }

  const INode& at(unsigned n) const override { return *get_v().m_v.at(n); }

  INode* parent() const override { return get_v().m_pParent; }

  void add_child(std::shared_ptr<const INode> node) override
  {
    get_v().m_v.push_back(std::move(node));
  }
};

std::unique_ptr<INode> MakeHolderNode()
{
  return std::unique_ptr<INode>(new HolderNode());
}

// ...

struct Leaf
{
  INode* m_pParent = nullptr;
  struct XYC { int x, y; bool c; };
  std::shared_ptr<const std::vector<XYC>> m_v;
};

struct LeafNode : ContentNode<Leaf>
{
  bool is_leaf() const override { return true; }

  const INode& at(unsigned n) const override { throw std::out_of_range{ "!!!" }; }

  INode* parent() const override { return get_v().m_pParent; }

  void add_child(std::shared_ptr<const INode> node) override
  {
    throw std::logic_error{ "!!!" };
  }
};

std::unique_ptr<INode> MakeLeafNode()
{
  return std::unique_ptr<INode>(new LeafNode());
}

LeafNode* dynamic_cast_to_LeafNode(INode* p)
{
  return dynamic_cast<LeafNode*>(p);
}

const LeafNode* dynamic_cast_to_LeafNode(const INode* p)
{
  return dynamic_cast<const LeafNode*>(p);
}

// ...

#if 0

struct MassiveLeaf
{
  INode* m_pParent;
  std::array<char, 96> m_v;
};

struct MassiveLeafNode : ContentNode<MassiveLeaf>
{
  bool is_leaf() const override { return true; }

  const INode& at(unsigned n) const override { throw std::out_of_range{ "!!!" }; }

  INode* parent() const override { return get_v().m_pParent; }

  void add_child(std::shared_ptr<const INode> node) override
  {
    throw std::logic_error{ "!!!" };
  }
};

std::unique_ptr<INode> MakeMassiveNode()
{
  return std::unique_ptr<INode>(new MassiveLeafNode());
}

#endif