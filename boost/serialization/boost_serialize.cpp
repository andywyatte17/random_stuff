
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

using namespace boost::serialization;

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
    image_bytes = std::vector<uint8_t>{1,2,3,'4'};
    opts.resize(3);
  }
};

// ...

template<class Archive>
inline void serialize(
    Archive& ar,
    CPictureOptions& opts,
    const unsigned int file_version)
{
  ar & make_nvp("remove", reinterpret_cast<unsigned&>(opts.r));
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
  // clang-3.5 -std=c++11 -stdlib=libstdc++ boost-test.cpp -lstdc++ -lboost_serialization && ./a.out && cat data.txt

  {
    std::ofstream ofs("data.txt");
    //boost::archive::text_oarchive oa(ofs);
    boost::archive::xml_oarchive oa(ofs);
    // write class instance to archive
    ITCP itcp;
    oa & make_nvp("itcp", itcp);
  }
  if(0){
    std::ifstream ifs("data.txt");
    //boost::archive::text_oarchive oa(ofs);
    boost::archive::xml_iarchive ia(ifs);
    // write class instance to archive
    ITCP itcp;
    serialize(ia, itcp, 0);
  }  
  return 0;
}
