#include "windows.h"
 
int main()
{
    MessageBox(0, "Hi " __DATE__ " " __TIME__, "MinGW", 0);
    return 1;
}