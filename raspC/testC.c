#include <stdio.h>
#include <stdlib.h>
#include <wiringSerial.h>

#define SER_PORT "/dev/ttyUSB0"
#define BAUD_RATE 115200

void main() {
  int dev;
  dev = serialOpen(SER_PORT, BAUD_RATE);
  if(dev == -1){
    fprintf(stderr, "Port Open Err.\n");
    exit(-1);
  }
  fprintf(stdout,"Port Opend\n");
  serialFlush(dev);
  while(1){
    int c;
    c = serialGetchar(dev);
    if(c != -1 && c != 'x'){
      fputc(c, stderr);
      serialPutchar(dev,(unsigned char)c);
    }
    else if(c == 'x'){
      break;
    }
  }
  fprintf(stdout, "Port Closed. \n");
  serialClose(dev);
  // return 0;
}

// compile method
// gcc -o testC testC.c -lwiringPi
