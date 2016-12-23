#include <boost/python.hpp>
#include <Python.h>
#include <thread>
#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <boost/coroutine/asymmetric_coroutine.hpp>

/*
clear && boost=/usr/lib/i386-linux-gnu g++ client.cpp -std=c++11 -I/usr/include/python2.7/ $boost/libboost_python-py27.so.1.58.0 $boost/libpython2.7.so $boost/libboost_context.so.1.58.0 $boost/libboost_system.so.1.58.0 $boost/libboost_thread.so.1.58.0 $boost/libboost_coroutine.a
*/

using namespace boost::python;

#if PY_MAJOR_VERSION >= 3
#define INIT_MODULE PyInit_mymodule
extern "C" PyObject *INIT_MODULE();
#else
#define INIT_MODULE initmymodule
extern "C" void INIT_MODULE();
#endif

using coro_t = boost::coroutines::coroutine<std::string>;

std::unique_ptr<coro_t::push_type> MakeSink(int argc, char **argv) {
  std::vector<std::string> v;
  for (int i = 0; i < argc; ++i)
    v.push_back(argv[i]);

  return std::unique_ptr<coro_t::push_type>(
      new coro_t::push_type([v, argc](coro_t::pull_type &source) {
        Py_Initialize();
        std::unique_ptr<char *[]> argv;
        argv.reset(new char *[argc]);
        for (int i = 0; i < argc; ++i)
          argv[i] = const_cast<char *>(v[i].c_str());

        PySys_SetArgv(argc, argv.get());
#if 0
    PyRun_SimpleString("import turtle");
    PyRun_SimpleString("turtle.setpos(50,50)");
#endif
        auto main_module = import("__main__");
        auto main_ns = extract<dict>(main_module.attr("__dict__"));
        auto res = exec("import turtle", main_ns, main_ns);
        for (;;) {
          std::string s = source.get();
          if (s.empty())
            break;
          exec(s.c_str(), main_ns, main_ns);
        }
      }));
}

int main(int argc, char **argv) {
  if (auto sink = MakeSink(argc, argv)) {
    (*sink)("turtle.setpos(50,50)");
    (*sink)("turtle.setpos(100,50)");
    std::this_thread::sleep_for(std::chrono::seconds(3));
    (*sink)("");
  }
  return 0;
}
