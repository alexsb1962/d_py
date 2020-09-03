//
// Created by Alex on 23.06.2020.
//

#include "client.h"
#include "..\server\sharedmem.h"


void main(void ){
    HANDLE lock_server,lock_client;
    LPCTSTR pBuf;
    HANDLE hMapFile;

    int k;
    for( k=10;k>0;k-- ) {

        lock_server = OpenMutex(MUTEX_ALL_ACCESS, FALSE, ServerMutexName);
        lock_server = OpenMutex(MUTEX_ALL_ACCESS, FALSE, ClientMutexName);
        if ((lock_server == NULL) | (lock_client == NULL)) {
            printf("Ошибка связи с сервером");
            printf("Осталось  %d  попыток",k);
            Sleep(1000);
        }
        else break;
    }

    if( k==0) exit(1);

    hMapFile = OpenFileMapping(
            FILE_MAP_ALL_ACCESS,   // read/write access
            FALSE,                 // do not inherit the name
            szName);               // name of mapping object

    if (hMapFile == NULL)
    {
        printf("Could not open file mapping object .\n", GetLastError());
        exit(1);
    }

    pBuf = (LPTSTR) MapViewOfFile(hMapFile, // handle to map object
                                  FILE_MAP_ALL_ACCESS,  // read/write permission
                                  0,
                                  0,
                                  DataLen*sizeof(complex)*2);

    if (pBuf == NULL)    {
        printf(TEXT("Could not map view of file (%d).\n"),  GetLastError());
        MessageBox(NULL, pBuf, TEXT("Could not map view of file (%d).\n"), MB_OK);
        CloseHandle(hMapFile);
        exit(1);
    }

    for (int i=0;i<=9;i++){
        WaitForSingleObject(lock_server,INFINITE);
        // fill data ram
        ReleaseMutex(lock_client);
    }

    UnmapViewOfFile(pBuf);
    CloseHandle(hMapFile);
    return ;

}

