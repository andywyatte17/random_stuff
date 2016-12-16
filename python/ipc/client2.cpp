#include <boost/python.hpp>
#include <Python.h>
#include <thread>
#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <boost/coroutine/asymmetric_coroutine.hpp>
#include <sstream>

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
        auto main_module = import("__main__");
        auto main_ns = extract<dict>(main_module.attr("__dict__"));
        auto init = std::string(R"...(
import socket
HOST = '127.0.0.1'        # The remote host
PORT = 50008              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
)...");
        //std::istringstream ss(init);
        //while(ss) {
        //  std::string line;
        //  std::getline(ss, line, '\n');
        //  if(!line.empty())
        //      PyRun_SimpleString(line.c_str());
        //}        
        auto res = exec(init.c_str(), main_ns, main_ns);
        for (;;) {
          std::string s = source.get();
          if (s.empty())
            break;
          s = "s.sendall('" + s + "\\n')";
          source();
          std::cout << clock() / (float)(CLOCKS_PER_SEC) << "\n";
          exec(s.c_str(), main_ns, main_ns);
        }
      }));
}

#include <cmath>

int main(int argc, char **argv) {
  if (auto sink = MakeSink(argc, argv)) {
    for(int x=0; x<=100; ++x)
    {
      std::ostringstream oss;
      if(x==0) (*sink)( "turtle.penup()" );
      oss << "turtle.setpos(" << std::sin(6.283*x/100.0) * 100
          << "," << std::cos(6.283*x/100.0) * 100 << ")";
      (*sink)( oss.str().c_str() );
      if(x==0) (*sink)( "turtle.pendown()" );
    }
    (*sink)("");
    std::this_thread::sleep_for(std::chrono::seconds(3));
  }
  return 0;
}
