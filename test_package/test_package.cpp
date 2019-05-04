#include <pprint.hpp>

#include <iostream>

int main()
{
    std::stringstream stream;
    pprint::PrettyPrinter printer(stream);
    printer.print(3.14f);
    const std::string result = stream.str();
    std::cout << "Result = [" << result << "]" << std::endl;
    return result == "3.14f" ? 0 : 1;
}
