#include <pprint.hpp>

#include <algorithm>
#include <cctype>
#include <iostream>
#include <locale>

void rtrim(std::string &s)
{
    const auto isNotSpace = [](const int ch) {
        return !std::isspace(ch);
    };

    s.erase(std::find_if(std::rbegin(s), std::rend(s), isNotSpace).base(), std::end(s));
}

int main()
{
    std::stringstream stream;
    pprint::PrettyPrinter printer(stream);
    printer.print(3.14f);
    std::string result = stream.str();
    rtrim(result);
    std::cout << "Result = [" << result << "]" << std::endl;
    return result == "3.14f" ? 0 : 1;
}
