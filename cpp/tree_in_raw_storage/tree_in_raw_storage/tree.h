//
// tree.h
//

#pragma once

#include <memory>
#include <array>
#include <memory>

struct INode
{
  template<int N> struct Checker {
    const char v[N]; static constexpr bool ok = true;
  };
  template<int N> struct CheckerZ {
    const char v[!N]; static constexpr bool ok = true;
  };
#if _WIN64
  static constexpr unsigned N = 56U, aligner = 16U, HopedSize = 80U;
#else
  static constexpr unsigned N = 52U, aligner = 8U, HopedSize = 64U;
#endif
  std::array<char, N + aligner> m_buffer;
  virtual ~INode() {}
  virtual bool is_leaf() const = 0;
  virtual const INode& at(unsigned n) const = 0;
  virtual INode* parent() const = 0;
  virtual void add_child(std::shared_ptr<const INode> node) = 0;
  virtual const void* content() const = 0;
  virtual unsigned contentAlignof() const = 0;
};

static_assert(INode::CheckerZ<sizeof(INode)-INode::HopedSize>::ok, "...");

std::unique_ptr<INode> MakeHolderNode();
std::unique_ptr<INode> MakeLeafNode();

struct LeafNode;

LeafNode* dynamic_cast_to_LeafNode(INode* p);
const LeafNode* dynamic_cast_to_LeafNode(const INode* p);
