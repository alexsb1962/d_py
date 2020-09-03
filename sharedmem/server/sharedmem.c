#include <stdio.h>
#include <io.h>
#include "sharedmem.h"


int main() {

    HANDLE lock_server;
    HANDLE lock_client;
    double complex *data;
    HANDLE hMapFile;
    LPCTSTR pBuf;


    LPVOID lpMsgBuf;
    LPVOID lpDisplayBuf;
    DWORD dw;



    printf("Started \n");

    lock_client=CreateMutex(NULL,TRUE,ServerMutexName);
    lock_server=CreateMutex(NULL,TRUE,ClientMutexName);


    printf("открываю файл и связываю с памятью\n");

    // в дальнейшем надо определиться с местом для файла

    hMapFile = CreateFileMapping(
            INVALID_HANDLE_VALUE,    // use paging file
            NULL,                    // default security
            PAGE_READWRITE,          // read/write access
            0,                       // maximum object size (high-order DWORD)
            DataLen,                // maximum object size (low-order DWORD)
            szName);                 // name of mapping object

    if (hMapFile == NULL)
    {
        printf(TEXT("Could not create file mapping object (%d).\n"), GetLastError());
        exit(1);
    }
     pBuf = (LPSTR) MapViewOfFile(hMapFile,   // handle to map object
                           FILE_MAP_ALL_ACCESS, // read/write permission
                           0,
                           0,
                           DataLen*sizeof(double complex));

    if (pBuf == NULL) {
        dw = GetLastError();
        printf( "Could not map view of file (%d).\n",   dw);
        FormatMessage(
                FORMAT_MESSAGE_ALLOCATE_BUFFER |
                FORMAT_MESSAGE_FROM_SYSTEM |
                FORMAT_MESSAGE_IGNORE_INSERTS,
                NULL,
                dw,
                MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
                (LPTSTR) &lpMsgBuf,
                0, NULL );



        CloseHandle(hMapFile);
        CloseHandle(lock_server);
        CloseHandle(lock_client);
        exit(1);
    }


    while (TRUE){
        ReleaseMutex( lock_server ); //  сервер готов
        WaitForSingleObject(lock_client,INFINITE); // клиент данные подготовил
        // do some work
    }


    CloseHandle(lock_server);
    CloseHandle(lock_client);
    CloseHandle(hMapFile);

    return 0;
}
