#include <pybind11/pybind11.h>

namespace py = pybind11;

int main() {
    py::object Decimal = py::module_::import("xmlrpc.server.SimpleXMLRPCServer");

    return 0;
}
