#include <map>
#include <iostream>
#include <algorithm>
#include <utility>
#include <iterator>
#include <tuple>
#include <cmath>
#include <initializer_list>

using namespace std;

#include "poker_ranks.h"

const uint64_t Primes[]{2,3,5,7,11,13,17,19,23,29,31,37,41,43};

int main()
{

#define FOR(start,var,ix_) for(int var=start; var<52; var++) {

  {
    hand h = hand({0,1,2,3,12},false).Sort();
    cout << h.Dbx() << endl;
    find_poker_value(h);
  }

  auto Hand_Prime = [&](hand h, bool is_flush)
  {
    uint64_t v = Primes[h.h[0]]*Primes[h.h[1]]*Primes[h.h[2]]*Primes[h.h[3]]*Primes[h.h[4]];
    if(is_flush)
      v*=Primes[13];
    return v;
  };

  try
  {
      map<int,hand> s;
      vector<hand> s2;
      FOR(0,i,0)
        FOR(i+1,j,1)
          FOR(j+1,k,2)
            FOR(k+1,l,3)
              FOR(l+1,m,4)
      for(int is_flush=0; is_flush<=1; ++is_flush) {
              {
                const auto h = [&]()
                {
                  hand h = hand({i%13,j%13,k%13,l%13,m%13}, !!is_flush);
                  h.Sort();
                  return h;
                }();

                int p=Hand_Prime(h, !!is_flush);
                auto thePair = make_pair(p, h);
                auto thePair2 = make_pair(thePair.second, thePair.first);
                if( s.end()==s.find(thePair.first) )
                {
                  s.insert( thePair );
                  s2.push_back( h );
                }
              }
      }}}}}}

      std::sort(s2.begin(), s2.end());
      cout << s.size() << endl;

      //for(auto i=s.begin(), e=s.end(); i!=e; ++i)
      //  cout << i->second.Dbx() << endl;

      for(auto i=s2.begin(), e=s2.end(); i!=e; ++i)
        cout << i->Dbx() << " " << Hand_Prime(*i, i->is_flush) << endl;
  }
  catch(...) { cout << "Exception!\n"; }
  return 0;
}
