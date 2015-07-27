
#include <boost/serialization/serialization.hpp>
#include <boost/serialization/binary_object.hpp>
#include <boost/serialization/vector.hpp>

#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/archive/xml_iarchive.hpp>
#include <boost/archive/xml_oarchive.hpp>
 
#include <boost/archive/xml_iarchive.hpp>
#include <vector>
#include <stdint.h>
#include <fstream>
#include <type_traits>
#include <initializer_list>

using namespace boost::serialization;

// ...

template< class EnumT >
typename std::enable_if<
    std::is_enum<EnumT>::value,
    typename std::underlying_type<EnumT>::type*
>::type enum_as_pointer(EnumT& e)
{
  return reinterpret_cast<typename std::underlying_type<EnumT>::type*>(&e);
}

// ...

struct CPictureOptions
{
  enum class Remove : unsigned { main, all };
  Remove r = Remove::main;
  int threshold = 0;
};

struct ITCP
{
  std::vector<CPictureOptions> opts;
  int something_else = 0;
  std::vector<uint8_t> image_bytes;
  ITCP() {
  }
  ITCP(std::initializer_list<int> x,
       std::initializer_list<uint8_t> b)
  {
    image_bytes = std::vector<uint8_t>(b);
    for(auto&& i : x)
    {
      opts.resize(opts.size()+1);
      opts.back().threshold = i;
    }
  }
};

// ...

template<class Archive>
inline void serialize(
    Archive& ar,
    CPictureOptions& opts,
    const unsigned int file_version)
{
  ar & make_nvp("threshold", opts.threshold);
  ar & make_nvp("remove", *enum_as_pointer(opts.r));
}

template<class Archive>
inline void serialize(
    Archive & ar, 
    ITCP & t, 
    const unsigned int file_version
)
{
  ar & make_nvp("opts",t.opts);
  ar & make_nvp("something_else", t.something_else);
  ar & make_nvp("image_bytes", make_binary_object(t.image_bytes.data(), t.image_bytes.size()));
}

// ...

int main()
{
  // clang-3.5 -std=c++11 -stdlib=libstdc++ boost_serialize.cpp -lstdc++ -lboost_serialization && ./a.out && cat data.txt

  {
    std::ofstream ofs("data.txt");
    //boost::archive::text_oarchive oa(ofs);
    boost::archive::xml_oarchive oa(ofs);
    // write class instance to archive
    ITCP itcp({1,66,173000,-5},{0xff,0x00,0xa0});
    oa & make_nvp("itcp", itcp);
  }
  {
    std::ifstream ifs("data.txt");
    //boost::archive::text_oarchive oa(ofs);
    boost::archive::xml_iarchive ia(ifs);
    // write class instance to archive
    ITCP itcp;
    ia & make_nvp("itcp", itcp);
  }  
  return 0;
}
