#include <map>
#include <iostream>
#include <algorithm>
#include <utility>
#include <iterator>
#include <tuple>
#include <cmath>
#include <vector>
#include <initializer_list>
#include <set>
#include <unordered_set>

using namespace std;

// eg { 1,1,2,3,3,4 } -> {2,1,2,1}
template<typename Iter, typename OutIt>
OutIt adjacent_count(Iter begin, Iter end, OutIt outCount)
{
  if( begin==end ) return outCount;
  int c = 1;
  for(auto it=next(begin), last=begin; it!=end; ++it, ++last) {
    if(*last==*it) c++;
    else { *outCount++ = c; c = 1; }
  }
  *outCount++ = c;
  return outCount;
}

struct Hand
{
  Hand() : is_flush(false), cards(), sequence(), is_straight(false) {}
  Hand(const Hand& rhs) = default;
  Hand& operator=(const Hand& rhs) = default;
  Hand( initializer_list<int> il, bool is_flush_in )
   : is_flush(is_flush_in), is_straight(false), sequence()
  {
    copy(begin(il), end(il), cards);
    Process();
  }
  string Dbx() const
  {
    return (is_flush ? string("F  ") : string("!F ")) +
     S()[cards[0]]+S()[cards[1]]+S()[cards[2]]+S()[cards[3]]+S()[cards[4]];
  }
  uint64_t Prime() const
  {
    const uint64_t Pr[]{2,3,5,7,11,13,17,19,23,29,31,37,41,43};
    auto* h = cards;
    auto prime = Pr[h[0]] * Pr[h[1]] * Pr[h[2]] * Pr[h[3]] * Pr[h[4]];
    return is_flush ? prime * Pr[13] : prime;
  }
  int cards[5];
  unsigned sequence[5];
  bool is_flush;
  bool operator>(const Hand& rhs) const
  {
    auto bv = BaseValue(), bv2 = rhs.BaseValue();
    if( bv > bv2 ) return true;
    if( bv2 > bv ) return false;
    for(int i=0; i<5; i++) {
      if( cards[i] > rhs.cards[i] ) return true;
      if( rhs.cards[i] > cards[i] ) return false;
    }
    return false;
  }
protected:
  bool is_straight;
private:
  int BaseValue() const
  {
/*
    High card - hand_type = hi...lo
    One pair - XXhi?lo
    Two pairs - YYXX.
    Three of a kind - XXX hi.lo
    Straight (number sequence) - hi...lo
    Flush (all same suit) - hi...lo
    Full house - XXX,YY
    Four of a kind - XXXX?
    Straight flush - hi...lo
*/
    auto Eq = [&](initializer_list<int> il) { return equal(begin(il), end(il), sequence); };
    if( is_flush && is_straight ) return 9;
    if( Eq({4,1}) ) return 8;
    if( Eq({3,2}) ) return 7;
    if( is_flush ) return 6;
    if( is_straight ) return 5;
    if( Eq({3,1,1}) ) return 4;
    if( Eq({2,2,1}) ) return 3;
    if( Eq({2,1,1,1}) ) return 2;
    return 1;
  }
  const string& S() const
  {
  	static const string s="23456789TJQKA";
  	return s;
  }
  bool IsStraight() const
  {
    const int AceLoStraight[] = { 12,3,2,1,0 };
    if( equal(AceLoStraight, AceLoStraight+5, cards) )
      return true;
    for( size_t i=1; i<5; i++)
      if( cards[i-1]-1 != cards[i] )
        return false;
    return true;
  }
  void Process()
  {
  	sort( begin(cards), end(cards), [](int a, int b) -> bool { return a>b; } );

    int frequency[13] = { 0,0,0,0,0,0,0,0,0,0,0,0,0 };
    for_each( begin(cards), end(cards), [&](int card) { ++frequency[card]; } );
    stable_sort(begin(cards), end(cards),
                [&](const int& cardA, const int& cardB)
                { return frequency[cardA] > frequency[cardB]; } );
    
    fill_n(sequence, 5, 0);
    adjacent_count( begin(cards), end(cards), sequence );
    
    if(sequence[4]==1)
      is_straight = IsStraight();
  }
};

int main()
{
  {
    auto h1 = Hand({9,9,9,11,10},false);   // JJJKQ
    auto h2 = Hand({11,11,10,10,9},false);   // KKQQJ
    auto comp = h1>h2;
    cout << h1.Dbx() << " > " << h2.Dbx() << " = " << !!comp << endl;
  }

  unordered_set<uint64_t> primes;
  vector< pair<Hand,int> > hands;
  hands.reserve(10000);
  for(int i=0; i<52; i++)
    for(int j=i+1; j<52; j++)
      for(int k=j+1; k<52; k++)
        for(int l=k+1; l<52; l++)
          for(int m=l+1; m<52; m++)
            for(int is_flush=0; is_flush<=1; ++is_flush)
            {
              const auto hand = Hand({i%13,j%13,k%13,l%13,m%13}, !!is_flush);
              const auto prime = hand.Prime();
              if( primes.end()!=primes.find(prime) )
                continue;
                
              primes.insert(prime);
              hands.push_back( make_pair(hand,0) );
            }

  std::sort(hands.begin(), hands.end(),
   [](const pair<Hand,int>& a, const pair<Hand,int>& b) { return b.first>a.first; } );

  // Assign values to each hand
  hands[0].second = 0;
  for(auto i=next(hands.begin()), l=hands.begin(), e=hands.end(); i!=e; ++i, ++l)
  {
    if( !(i->first > l->first) && !(l->first > i->first) )
      i->second = l->second;
    else
      i->second = l->second+1;
  }
  
  //for(auto i=hands.begin(), e=hands.end(); i!=e; ++i)
  //  cout << i->first.Dbx() << " " << i->second << " " << i->first.Prime() << endl;

  for(auto i=hands.begin(), e=hands.end(); i!=e; ++i)
    cout << i->first.Prime() << "," << i->second << endl;
    
  cout << "Number of unique hands = " << hands.size() << endl;

  return 0;
}
