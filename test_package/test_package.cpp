#include <pprint.hpp>

int main()
{
    std::stringstream stream;
    pprint::PrettyPrinter printer(stream);
    printer.print(3.14f);
    return stream.str() == "3.14f" ? 0 : 1;
    `
}
