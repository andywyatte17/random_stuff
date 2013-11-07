#pragma once

#include <initializer_list>

struct hand
{
  hand() : is_flush(false) {}
  hand(const hand& rhs) = default;
  hand& operator=(const hand& rhs) = default;
  hand( std::initializer_list<int> il, bool is_flush_in ) : is_flush(is_flush_in)
  {
    copy(begin(il), end(il), h);
  }
  const string& S() const
  {
  	static const string s="23456789TJQKA";
  	return s;
  };
  string Dbx() const
  {
    return (is_flush ? std::string("IsF") : std::string("!F ")) +
     S()[h[0]]+S()[h[1]]+S()[h[2]]+S()[h[3]]+S()[h[4]];
  }
  hand& Sort()
  {
  	sort( begin(h), end(h), [](int a, int b) -> bool { return a>b; } );
  	return *this;
  }
  int h[5];
  bool is_flush;
  bool operator<(const hand& rhs) const;
};

typedef std::pair<hand,hand> Hand_Seq_t;

Hand_Seq_t pair_sorter(hand h)
{
  hand seq;
  std::fill_n(std::begin(seq.h), 5, 0);
  seq.h[0] = 1;
  for(int i=1, c=0; i<5; i++) {
    if(h.h[i-1]==h.h[i])
      seq.h[c]++;
    else
      seq.h[++c]++;
  }
  return make_pair(h,seq);
}

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

int card_to_high_value_ace_low(int card)
{
  if(card==12) return -1;
  return card;
}

int card_to_high_value_x(int card, int x)
{
  return card==x ? 1000 : card;
}

int card_to_high_value_xy(int card, int x, int y)
{
  return card==x ? 2000 : card==y ? 1000 : card;
}

template<typename T>
inline bool Eq(const hand& h, std::initializer_list<T> il)
{
  int c = 0;
  for(auto i=begin(il), e=end(il); i!=e; ++i, ++c)
    if(*i != h.h[c])
      return false;
  return true;
}

template<typename F>
inline hand sorted(hand hand_, F f)
{
  sort(begin(hand_.h), end(hand_.h), f);
  return hand_;
}

std::pair<bool,hand> is_four_of_kind(Hand_Seq_t hsq)
{
  auto& hand = hsq.first;
  auto& cards = hand.h;
  if ( Eq(hsq.second, {4,1}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_x(a, cards[0]) > card_to_high_value_x(b, cards[0]);
    });
    return make_pair(true, sortd);
  }
  if ( Eq(hsq.second, {1,4}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_x(a, cards[4]) > card_to_high_value_x(b, cards[4]);
    });
    return make_pair(true, sortd);
  }
  return make_pair(false, hand);
}

std::pair<bool,hand> is_full_house(Hand_Seq_t hsq)
{
  auto& hand = hsq.first;
  auto& cards = hand.h;
  if ( Eq(hsq.second, {3,2}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_xy(a, cards[3], cards[4]) > card_to_high_value_xy(b, cards[3], cards[4]);
    });
    return make_pair(true, sortd);
  }
  if ( Eq(hsq.second, {2,3}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_xy(a, cards[3], cards[2]) > card_to_high_value_xy(b, cards[3], cards[2]);
    });
    return make_pair(true, sortd);
  }
  return make_pair(false, hand);
}

std::pair<bool,hand> is_straight_impl(Hand_Seq_t hsq) {
  auto& hand = hsq.first;
  auto& cards = hand.h;
  for(int i : {1,2,3,4}) {
    if( (cards[i-1]-1)!=cards[i] )
      return make_pair(false, hsq.first);
  }
  // pprint.pprint( ("straight!", g4p[1]) )
  return make_pair(true, hsq.first);
}

std::pair<bool,hand> is_straight(Hand_Seq_t hsq)
{
  auto rv = is_straight_impl(hsq);
  if(rv.first) return rv;
  if(hsq.first.h[0]==12 /* Ace */)
  {
    std::rotate(hsq.first.h, hsq.first.h+1, hsq.first.h+5);
    hsq.first.h[4] = -1;
    if( is_straight_impl(hsq).first )
    {
      rv.first = true;
      return rv;
    }
  }
  rv.first = false;
  return rv;
}

std::pair<bool,hand> is_straight_flush(Hand_Seq_t hsq, bool is_flush) {
  if(is_straight(hsq).first && is_flush)
    return make_pair(true, hsq.first);
  return make_pair(false, hsq.first);
}

std::pair<bool,hand> is_three_of_kind(Hand_Seq_t hsq) {
  auto& hand = hsq.first;
  auto& cards = hand.h;
  if ( Eq(hsq.second, {3,1,1}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_x(a, cards[3]) > card_to_high_value_x(b, cards[3]);
    });
    return make_pair(true, sortd);
  }
  if ( Eq(hsq.second, {1,3,1}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_x(a, cards[4]) > card_to_high_value_x(b, cards[4]);
    });
    return make_pair(true, sortd);
  }
  if ( Eq(hsq.second, {1,1,3}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_x(a, cards[5]) > card_to_high_value_x(b, cards[5]);
    });
    return make_pair(true, sortd);
  }
  return make_pair(false, hand);
}

std::pair<bool,hand> is_two_pairs(Hand_Seq_t hsq) {
  auto& hand = hsq.first;
  auto& cards = hand.h;
  if ( Eq(hsq.second, {1,2,2}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_xy(a, cards[1], cards[3]) > card_to_high_value_xy(b, cards[1], cards[3]);
    });
    return make_pair(true, sortd);
  }
  if ( Eq(hsq.second, {2,1,2}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_xy(a, cards[1], cards[4]) > card_to_high_value_xy(b, cards[1], cards[4]);
    });
    return make_pair(true, sortd);
  }
  if ( Eq(hsq.second, {2,2,1}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_xy(a, cards[1], cards[3]) > card_to_high_value_xy(b, cards[1], cards[3]);
    });
    return make_pair(true, sortd);
  }
  return make_pair(false, hand);
}

std::pair<bool,hand> is_pair(Hand_Seq_t hsq) {
  auto& hand = hsq.first;
  auto& cards = hand.h;
  if ( Eq(hsq.second, {2,1,1,1}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_x(a, cards[1]) > card_to_high_value_x(b, cards[1]);
    });
    return make_pair(true, sortd);
  }
  if ( Eq(hsq.second, {1,2,1,1}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_x(a, cards[2]) > card_to_high_value_x(b, cards[2]);
    });
    return make_pair(true, sortd);
  }
  if ( Eq(hsq.second, {1,1,2,1}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_x(a, cards[3]) > card_to_high_value_x(b, cards[3]);
    });
    return make_pair(true, sortd);
  }
  if ( Eq(hsq.second, {1,1,1,2}) ) {
    auto sortd = sorted(hand, [&](int a, int b) {
      return card_to_high_value_x(a, cards[4]) > card_to_high_value_x(b, cards[4]);
    });
    return make_pair(true, sortd);
  }
  return make_pair(false, hand);
}

std::tuple<int,std::string,hand> find_poker_value(Hand_Seq_t hsq)
{
  typedef std::tuple<int,std::string,hand> T;
  const bool is_flush = hsq.first.is_flush;
  auto sorted = is_straight_flush(hsq, is_flush);
  if (sorted.first) return T( 9, "Straight Flush", sorted.second );
  sorted = is_four_of_kind(hsq);
  if( sorted.first ) return T( 8, "Four of a kind", sorted.second );
  sorted = is_full_house(hsq);
  if( sorted.first ) return T( 7, "Full House", sorted.second );
  sorted = is_four_of_kind(hsq);
  if( sorted.first ) return T( 6, "Four of a kind", sorted.second );
  if( is_flush ) return T( 5, "Flush", hsq.first );
  sorted = is_straight(hsq);
  if( sorted.first ) return T( 4, "Straight", sorted.second );
  sorted = is_three_of_kind(hsq);
  if( sorted.first ) return T( 3, "Three of a kind", sorted.second );
  sorted = is_two_pairs(hsq);
  if( sorted.first ) return T( 2, "Two pairs", sorted.second );
  sorted = is_pair(hsq);
  if( sorted.first ) return T( 1, "Pair", sorted.second );
  return T( 0, "High card", hsq.first );
}

std::tuple<int,std::string,hand> find_poker_value(hand h)
{
  return find_poker_value(pair_sorter(h));
}

bool hand::operator<(const hand& rhs) const
{
  auto pv = find_poker_value( pair_sorter(*this) );
  auto pv2 = find_poker_value( pair_sorter(rhs) );
  if( std::get<0>(pv) < std::get<0>(pv2) ) return true;
  if( std::get<0>(pv2) < std::get<0>(pv) ) return false;
  return make_tuple(
    get<2>(pv).h[0],
    get<2>(pv).h[1],
    get<2>(pv).h[2],
    get<2>(pv).h[3],
    get<2>(pv).h[4]) <
      make_tuple(
    get<2>(pv2).h[0],
    get<2>(pv2).h[1],
    get<2>(pv2).h[2],
    get<2>(pv2).h[3],
    get<2>(pv2).h[4]);
}
