//
// main.cpp
//
// AStyle - Linux, indent = 2 spaces
//

#include <iostream>
#include <random>
#include <iomanip>
#include "PhotoStitchCreator.h"
#include <chrono>
#include <memory>
#include <limits.h>
#include <algorithm>

using namespace std;

auto ProfileScope = [](std::string s)
{
  auto start = chrono::high_resolution_clock::now();
  std::unique_ptr<void,std::function<void(void*)>> sp((void*)1,
  [=](void* p) {
    auto end = chrono::high_resolution_clock::now();
    auto dur = chrono::duration_cast<chrono::milliseconds>(end-start);
    printf("%s = %dms\n", s.c_str(), (int)dur.count());
  });
  return sp;
};

template<typename PointContainer_t>
void dump(const PointContainer_t& pts)
{
  int n = 8;
  for(auto& x : pts) {
    cout << setw(5) << x.x << "," << x.y;
    if(n--==0)
      (cout << endl), n = 8;
  }
};

template<typename PointContainer_t>
unsigned distance(const PointContainer_t& pts)
{
  unsigned n = 0;
  PointI pt = pts[0];
  for(auto& p : pts) {
    n += hypot(pt.x-p.x, pt.y-p.y);
    pt = p;
  }
  return n;
};

template<typename PointIContainer_t>
void NearestNeighbour(PointIContainer_t& c)
{
  auto D = [](const PointI& a, const PointI& b) {
    auto dx = std::abs(a.x-b.x);
    auto dy = std::abs(a.y-b.y);
    if(dy>dx) return dy + dx/2;
    return dx + dy/2;
  };

  for(auto i = c.begin(), e = std::prev(c.end()); i!=e; ++i) {
    auto i2 = std::next(i);
    auto e2 = c.end();
    auto minE = std::min_element(i2, e2,
    [&](const PointI& a, const PointI& b) {
      return D(a,*i) < D(b,*i);
    });
    std::swap(*minE, *i2);
  }
}

template<typename T> using UniInt_t = std::uniform_int_distribution<T>;

template<typename T>
std::pair<T,int> Pts1();

template<typename T>
std::pair<T,int> PtsChain1();

int main()
{
  //auto pts_thresh = Pts1<std::vector<PointI>>();
  auto pts_thresh = PtsChain1<std::vector<PointI>>();
  auto& pts = pts_thresh.first;
  const auto& THRESH = pts_thresh.second;

  //std::random_shuffle(pts.begin(), pts.end());
  //auto pts = Pts1<std::list<PointI>>();

  cout << "|pts| = " << pts.size() << "; THRESH=" << THRESH << endl;

  auto copy_ = pts;
  cout << "Before: " << distance(pts) << endl;

  if(1) {
    cout << "---\nNN:" << endl;

    auto tmp = pts;
    {
      auto ps = ProfileScope("\tNearestNeighbour");
      NearestNeighbour(tmp);
      cout << "\tNearNb: " << distance(tmp) << endl;
    }
    {
      auto ps = ProfileScope("\tNearestNeighbour - BasicLK");
      BasicLK(tmp, THRESH);
      cout << "\tBefore: " << distance(tmp) << endl;
    }

    cout << "---" << endl << endl;
  }

  {
    auto ps = ProfileScope("BasicLK");
    BasicLK(pts, THRESH);
  }
  cout << "After:  " << distance(pts) << endl;
  cout << "copy==pts - " << boolalpha << (copy_==pts) << endl;
  //dump(pts);

  cout << "Hello world!" << endl;
  return 0;
}

template<typename T>
void reserver(T& t) {}

template<>
void reserver(std::vector<PointI>& t)
{
  t.reserve(16*1024);
}

template<typename T>
std::pair<T,int> Pts1()
{
  T pts;
  reserver(pts);
  std::mt19937 r;
  auto xr = UniInt_t<int>(1,6);
  auto xd = UniInt_t<int>(0,50);
  auto xw = UniInt_t<int>(0,15);
  for(int y=0; y<500; y++) {
    int x = 0;
    for(int xc = xr(r); --xc;) {
      x += xd(r);
      auto x2 = x + xw(r);
      for(; x!=x2; ++x)
        pts.push_back( PointI {x,y} );
    }
  }
  return std::make_pair(std::move(pts),10);
}


#include "ptsChain1.h"
