//
// variant.cpp
//

#include <tuple>
#include <type_traits>
#include <string>
#include <iostream>

class V
{
private:
  template <class T, class Tuple>
  struct Index;

  template <class T, class... Types>
  struct Index<T, std::tuple<T, Types...>> {
    static const std::size_t value = 0;
  };

  template <class T, class U, class... Types>
  struct Index<T, std::tuple<U, Types...>> {
    static const std::size_t value = 1 + Index<T, std::tuple<Types...>>::value;
};

public:
  using T1 = std::string;
  using T2 = int;
  using T3 = std::pair<int, float>;
  using TL = std::tuple<T1, T2, T3>;

private:
  typename std::aligned_union<3, T1, T2, T3>::type buf;
  int8_t type = -1;

  template<typename T>
  void init_t(int8_t n) { new (&get_t<T>(false)) T(); type = n; }

  void cleanup() {
    if(type==0) { (get_t<T1>(false)).~T1(); }
    if(type==1) { (get_t<T2>(false)).~T2(); }
    if(type==2) { (get_t<T3>(false)).~T3(); }
    type = -1;
  }

private:
  template<typename T>
  T& get_t(bool check) {
    const auto n = Index<T, TL>::value;
    if(check && type != n)
      throw std::runtime_error{"Bad type!"};
    return *reinterpret_cast<T*>(&buf);
  }

public:
  template<typename T>
  T& get() { return get_t<T>(true); }

public:
  V() {}
  template<typename T>
  V(const T& t) {
    *this = t;
  }
  template<typename T>
  V& operator=(const T& t) {
    const auto n = Index<T, TL>::value;
    if(type!=n) {
      cleanup();
      init_t<T>(n);
    }
    get_t<T>(true) = t;
    return *this;
  }
};

// clang-3.5 --std=c++11 --stdlib=libc++ variant.cpp -lc++ && ./a.out

int main()
{
  V v;
  v = std::string{"string"};
  for(int i=0; i<100; ++i) {
    v = std::string(120, 'v');
    v = 42;
  }
  v = std::make_pair(42, 9.59f);
  std::cout << v.get<std::pair<int,float>>().second << "\n";
  v = std::string(120,'v');
  std::cout << v.get<std::string>() << "\n";
  v = 42;
  std::cout << v.get<int>() << "\n";
  std::cout << "sizeof(v) = " << sizeof(v) << "\n";
  return 0;
}

